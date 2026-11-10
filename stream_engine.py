"""CRT STREAM ENGINE v1.0 FINAL (dedicated CRT track; lives ONLY under crypto-quant/crt/).

Authority for every convention: crt/REGISTRY.md SPEC v1.0 constants.
Provides: bar streams (disk lanes + WINDOWED in-memory fetch for 5m/1m; raw
discarded by the caller), anchor suppliers, and the pre-registered
sweep-reversal state machine. run_s1.py wires the declared cells.

Declared readings (all stamped in the registry/report):
- T3/monitoring window = the CURRENT anchor-TF candle (the candle whose extent
  the trigger monitors). A1 anchor LEVELS come from the completed PRIOR candle.
  First-candle anchors become valid at the first candle's close; window = the
  anchor period (the day). Rolling-range anchors (PA2) have no time stop.
- Pending entries live inside the sweep candle's window; canceled at window end
  or anchor change; unfilled = no fee. PA2 (mkt pend, 1-bar life) is exempted.
- Waiting sweeps while a position or pending order is alive are IGNORED (one
  career at a time; no replacement, no flip). Re-arm only when flat + NEW sweep.
- Void: pre-sweep trigger CLOSE strictly beyond the level voids that side for
  the current anchor candle (eps applies only to the pierce, never the void).
- Execution: decision at trigger-bar close. 'mkt' fills next bar open; 'limit'
  fills at the sweep-bar midpoint (gap rule: bar OPENS beyond -> fill at open);
  'stop' fills at the sweep-bar near side (gap rule same). STOP first when a
  bar touches both stop and target. Side precedence on one bar: 'hi' first.
- Costs: 7bp/side per fill (entry fee share proportional to the portion), exit
  fee per portion; haircut 3bp/day per $1 held per portion (close-time dated).
- MDD = trade-exit-stream NAV (portion nets at exit timestamps).
- PF = on per-trade NET (fees + haircut included). Rows are PORTION records
  (T2 splits one trip into two rows); >=8 judge floor counts rows.
- Killzone gate: sweep must confirm on a trigger bar whose OPEN time-of-day
  (America/New_York clock) lies inside [start,b) of the window; fills then
  follow normally (may lie outside the window).
"""
import os
import time

import numpy as np
import pandas as pd
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
AGG = os.path.join(ROOT, "crt", "data_agg")

PRICE_SCALE = 1_000_000        # config.py convention; deep CSVs are raw dollars
FEE = 0.0007                   # 7bp/side taker, every fill (registry)
HAIR = 0.0003                  # 3bp/day per $1 held (registry)
NOTION = 100.0                 # $100 notional per position (registry)
NS_DAY = 86_400_000_000_000
NS_HOUR = 3_600_000_000_000

JUDGE_TS = pd.Timestamp("2025-11-05")
JUDGE_NS = int(JUDGE_TS.value)

COLS = ["OpenTime", "Open", "High", "Low", "Close", "Volume",
        "CloseTime", "QVol", "Trades", "TakerBase", "TakerQuote", "Ignore"]
ENDPOINTS = ["https://api.binance.com", "https://data-api.binance.vision"]

KZ_WINDOWS = {"London": (120.0, 300.0), "NYAM": (420.0, 600.0)}   # ET minutes [a, b)


# ---------------------------------------------------------------- bar loaders

def load_bars(sym, tf=None, suffix="_deep"):
    """Disk lane loader. audit.load convention: OHLC divided by PRICE_SCALE.
    Date index = bar OPEN time (standing); index normalized to ns."""
    path = os.path.join(DATA, f"{sym}_{tf}{suffix}.csv") if tf is not None else sym
    df = pd.read_csv(path, parse_dates=["Date"], index_col="Date").astype(float)
    df[["Open", "High", "Low", "Close"]] = df[["Open", "High", "Low", "Close"]] / PRICE_SCALE
    try:
        df.index = df.index.as_unit("ns")
    except Exception:
        pass
    return df


def agg_from(df, rule):
    """Standing resample: label-left, closed-left."""
    g = df.resample(rule, label="left", closed="left").agg(
        {"Open": "first", "High": "max", "Low": "min", "Close": "last", "Volume": "sum"})
    return g.dropna()


def _frame_to_arrays(df):
    idx = df.index
    try:
        idx = idx.as_unit("ns")          # pandas 3 may parse to us/ms precision
    except Exception:
        pass
    ts = idx.values.astype("int64")      # epoch ns (open times)
    return ts, (df["Open"].to_numpy(np.float64), df["High"].to_numpy(np.float64),
                df["Low"].to_numpy(np.float64), df["Close"].to_numpy(np.float64))


CACHE_RAW = os.path.join(ROOT, "crt", "cache_raw")    # user-ratified checkpoint
CK_FLUSH = 100_000                                    # rows per checkpoint flush


def _parse_rows(rows):
    """json kline lists -> (ts_ms int64 array, o, h, l, c float arrays)."""
    n = len(rows)
    ts = np.empty(n, dtype=np.int64)
    o = np.empty(n, dtype=np.float64)
    h = np.empty(n, dtype=np.float64)
    l = np.empty(n, dtype=np.float64)
    c = np.empty(n, dtype=np.float64)
    for k, r in enumerate(rows):
        ts[k] = int(r[0])
        o[k] = float(r[1])
        h[k] = float(r[2])
        l[k] = float(r[3])
        c[k] = float(r[4])
    return ts, o, h, l, c


def _ck_write(path, ts, o, h, l, c):
    """atomic-ish checkpoint write (np.savez via file object -> exact name);
    os.replace retried for transient Windows locks (AV/indexer races)."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "wb") as fh:
        np.savez(fh, ts=ts, o=o, h=h, l=l, c=c)
    for attempt in range(6):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            time.sleep(1.5 * (attempt + 1))
    if os.path.exists(tmp):                    # last resort: keep tmp, warn
        print(f"  [ckpt] replace failed persistently for {path}; "
              f"tmp kept as {os.path.basename(tmp)}", flush=True)


def fetch_klines(symbol, interval, start_ms, end_ms=None, ck_path=None):
    """WINDOWED in-memory fetch; optional disk checkpoint for RESUMABILITY
    (user-ratified amendment: crt/cache_raw/*.npz working cache, flushed every
    CK_FLUSH rows, deleted after a successful full battery; never feeds a
    verdict). Paginated spot /api/v3/klines; per-batch retries + mirror
    fallback + exponential backoff."""
    if end_ms is None:
        end_ms = int(time.time() * 1000)
    tsA = np.empty(0, dtype=np.int64)
    oA = np.empty(0, dtype=np.float64)
    hA = np.empty(0, dtype=np.float64)
    lA = np.empty(0, dtype=np.float64)
    cA = np.empty(0, dtype=np.float64)
    cur = int(start_ms)
    if ck_path is not None and os.path.exists(ck_path):
        try:
            with np.load(ck_path, allow_pickle=False) as z:
                tsA, oA, hA, lA, cA = (z["ts"], z["o"], z["h"], z["l"], z["c"])
            if len(tsA):
                cur = int(tsA[-1]) + 1
                print(f"  [fetch {interval}] RESUME from checkpoint: "
                      f"{len(tsA):,} rows @ {pd.Timestamp(tsA[-1], unit='ms')}",
                      flush=True)
        except Exception as e:
            print(f"  [fetch {interval}] checkpoint load failed ({e}); refetching",
                  flush=True)
            tsA = np.empty(0, dtype=np.int64)
            oA = np.empty(0, dtype=np.float64)
            hA = np.empty(0, dtype=np.float64)
            lA = np.empty(0, dtype=np.float64)
            cA = np.empty(0, dtype=np.float64)
            cur = int(start_ms)
    bts = np.empty(0, dtype=np.int64)
    bo = np.empty(0, dtype=np.float64)
    bh = np.empty(0, dtype=np.float64)
    bl = np.empty(0, dtype=np.float64)
    bc = np.empty(0, dtype=np.float64)
    bi = 0
    t0 = time.time()
    BACKOFF = [1.0, 2.0, 4.0, 8.0, 16.0, 30.0, 60.0, 90.0]

    def flush():
        nonlocal tsA, oA, hA, lA, cA, bts, bo, bh, bl, bc
        if len(bts) == 0:
            return
        tsA = np.concatenate([tsA, bts])
        oA = np.concatenate([oA, bo])
        hA = np.concatenate([hA, bh])
        lA = np.concatenate([lA, bl])
        cA = np.concatenate([cA, bc])
        bts = np.empty(0, dtype=np.int64)
        bo = np.empty(0, dtype=np.float64)
        bh = np.empty(0, dtype=np.float64)
        bl = np.empty(0, dtype=np.float64)
        bc = np.empty(0, dtype=np.float64)
        if ck_path is not None:
            _ck_write(ck_path, tsA, oA, hA, lA, cA)

    while cur < end_ms:
        payload = None
        wts = pd.Timestamp(cur, unit="ms")
        for attempt in range(8):
            base = ENDPOINTS[bi % 2]
            bi += 1
            try:
                r = requests.get(f"{base}/api/v3/klines", params=dict(
                    symbol=symbol, interval=interval, startTime=cur,
                    limit=1000, endTime=end_ms), timeout=20)
                r.raise_for_status()
                payload = r.json()
                break
            except Exception as e:
                d = BACKOFF[min(attempt, len(BACKOFF) - 1)]
                if attempt >= 2:
                    print(f"  [fetch {interval}] window {wts} attempt {attempt + 1} "
                          f"failed ({type(e).__name__}); retry in {d:.0f}s", flush=True)
                time.sleep(d)
        if payload is None:
            raise RuntimeError(
                f"klines fetch FAILED after 8 backoff attempts (~6.5 min stall "
                f"tolerance) at {wts} ({symbol} {interval}) - checkpoint keeps "
                f"{(len(tsA) + len(bts)):,} rows; re-run resumes from there")
        pts, po, ph, pl, pc = _parse_rows(payload)
        bts = np.concatenate([bts, pts])
        bo = np.concatenate([bo, po])
        bh = np.concatenate([bh, ph])
        bl = np.concatenate([bl, pl])
        bc = np.concatenate([bc, pc])
        nxt = payload[-1][0] + 1
        if nxt <= cur:
            break
        cur = nxt
        time.sleep(0.03)
        if len(bts) >= CK_FLUSH:
            n_all = len(tsA) + len(bts)
            print(f"  [fetch {interval}] checkpoint {n_all:,} rows "
                  f"@ {pd.Timestamp(cur, unit='ms')} "
                  f"({time.time()-t0:.0f}s)", flush=True)
            flush()
    flush()
    n_all = len(tsA)
    if not n_all:
        raise RuntimeError(f"empty fetch for {symbol} {interval}")
    df = pd.DataFrame({"Open": oA, "High": hA, "Low": lA, "Close": cA},
                      index=pd.to_datetime(tsA, unit="ms"))
    df.index.name = "Date"
    df = df.sort_index()
    df = df[~df.index.duplicated(keep="first")]
    return df[["Open", "High", "Low", "Close"]]


# ------------------------------------------------------------------- 1h base

_1H_CACHE = {}


def base_1h_df():
    if "df" not in _1H_CACHE:
        _1H_CACHE["df"] = load_bars("BTCUSDT", "1h")
    return _1H_CACHE["df"]


def et_floor(idx):
    """America/New_York calendar-day keys (DST-native). Accepts naive (UTC
    assumed) or already-ET-aware indexes."""
    et = idx if getattr(idx, "tz", None) is not None \
        else idx.tz_localize("UTC").tz_convert("America/New_York")
    return et.floor("D")


def daily_utc_table():
    """(day_ids sorted, highs, lows) UTC daily OHLC resampled from 1h deep."""
    if "d" not in _1H_CACHE:
        d = agg_from(base_1h_df(), "1D")
        day_id = d.index.values.astype("int64") // NS_DAY
        _1H_CACHE["d"] = (day_id, d["High"].to_numpy(np.float64),
                          d["Low"].to_numpy(np.float64))
    return _1H_CACHE["d"]


def daily_est_table():
    """(et_day_start_utc_ns sorted, highs, lows) daily-by-ET-day table."""
    if "e" not in _1H_CACHE:
        d1h = base_1h_df()
        key = et_floor(d1h.index)
        g = d1h.groupby(key).agg({"High": "max", "Low": "min"}).sort_index()
        starts = g.index.tz_convert("UTC").tz_localize(None).values.astype("int64")
        _1H_CACHE["e"] = (starts, g["High"].to_numpy(np.float64),
                          g["Low"].to_numpy(np.float64))
    return _1H_CACHE["e"]


def weekly_table():
    """(week_start_ns sorted, highs, lows) W-SUN label-left closed-left, 1h-built."""
    if "w" not in _1H_CACHE:
        w = agg_from(base_1h_df(), "W-SUN")
        starts = w.index.values.astype("int64")
        _1H_CACHE["w"] = (starts, w["High"].to_numpy(np.float64),
                          w["Low"].to_numpy(np.float64))
    return _1H_CACHE["w"]


def et_0800_starts():
    """Naive-UTC ns of 08:00 ET per ET day (EST first-candle anchor closes).
    Wall arithm. on naive ET clock then re-localize -> exact across DST."""
    if "e8" not in _1H_CACHE:
        s, _, _ = daily_est_table()
        aw = pd.DatetimeIndex(s).tz_localize("UTC").tz_convert("America/New_York")
        wall_mid = aw.tz_localize(None)            # ET wall midnights
        wall8 = wall_mid + pd.Timedelta(hours=8)   # 08:00 ET wall (never ambiguous)
        utc8 = wall8.tz_localize("America/New_York").tz_convert("UTC").tz_localize(None)
        _1H_CACHE["e8"] = utc8.values.astype("int64")
    return _1H_CACHE["e8"]


# ---------------------------------------------------------------------- lane

class Lane:
    """One trigger cadence's raw bar arrays (open-time indexed, epoch ns)."""

    def __init__(self, sym, tf, start_ts=None, end_ts=None):
        self.sym, self.tf, self.source = sym, tf, "disk"
        self.df = None
        if tf in ("1h", "15m", "4h"):
            df = load_bars(sym, tf)
        elif tf == "daily":
            df = agg_from(load_bars(sym, "1h"), "1D")
        elif tf in ("5m", "1m"):
            self.source = "fetch(in-RAM, raw discarded)"
            ms0 = (start_ts if start_ts is not None
                   else pd.Timestamp("2021-11-05")).value // 10**6
            ms1 = (int(time.time() * 1000) if end_ts is None
                   else int(end_ts.value) // 10**6)
            ck = os.path.join(CACHE_RAW, f"{sym}_{tf}.npz")
            df = self.df = fetch_klines(sym, tf, ms0, ms1, ck_path=ck)
        else:
            raise ValueError(f"unknown trigger lane {tf}")
        if self.df is None:
            self.df = df
        end_ns = int(end_ts.value) if end_ts is not None else None
        ts, (o, h, l, c) = _frame_to_arrays(df)
        if end_ns is not None:
            m = ts <= end_ns
            ts, o, h, l, c = ts[m], o[m], h[m], l[m], c[m]
        self.ts, self.o, self.h, self.l, self.c = ts, o, h, l, c
        self.n = int(len(ts))
        dif = np.diff(ts)
        self.tf_ns = int(np.median(dif)) if len(dif) else NS_HOUR
        self._et = None
        self._disc = {}

    def truncate_to_common_end(self, end_ns):
        m = self.ts <= int(end_ns)
        self.ts, self.o, self.h, self.l, self.c = (self.ts[m], self.o[m], self.h[m],
                                                   self.l[m], self.c[m])
        self.n = int(len(self.ts))

    def et_index(self):
        if self._et is None:
            self._et = (pd.DatetimeIndex(self.ts).tz_localize("UTC")
                        .tz_convert("America/New_York"))
        return self._et

    def est_day_ids(self):
        """per-bar ET-day start, naive UTC ns (floor D in the ET clock first)."""
        if "estd" not in self._disc:
            self._disc["estd"] = (et_floor(self.et_index())
                                  .tz_convert("UTC").tz_localize(None)
                                  .values.astype("int64"))
        return self._disc["estd"]

    def utc_day_ids(self):
        if "utcd" not in self._disc:
            self._disc["utcd"] = self.ts // NS_DAY
        return self._disc["utcd"]

    def week_ids(self):
        if "wk" not in self._disc:
            # W-SUN bucket starts via epoch-day arithmetic: day 0 = 1970-01-01
            # (Thursday); Sundays are (day-3) % 7 == 0 -> bucket start.
            day = self.ts // NS_DAY
            wk_day = ((day - 3) // 7) * 7 + 3
            self._disc["wk"] = wk_day * NS_DAY
        return self._disc["wk"]

    def minute_of_day_et(self):
        if "mod" not in self._disc:
            et = self.et_index()
            self._disc["mod"] = ((et - et.floor("D")).total_seconds()
                                 .to_numpy(np.float64) / 60.0)
        return self._disc["mod"]

    def drop_raw(self):
        """Storage rule: discard the raw fetched frame."""
        self.df = None
        self._disc = {}


def kz_mask(lane, name):
    lo, hi = KZ_WINDOWS[name]
    mod = lane.minute_of_day_et()
    return (mod >= lo) & (mod < hi)


# --------------------------------------------------------- anchor suppliers

def _t3_from_win(lane, win_end_arr):
    """Last trigger bar with open < window end (the T3 bar). -1 where NaN."""
    we = np.asarray(win_end_arr, dtype=np.float64)
    t3 = np.searchsorted(lane.ts, np.nan_to_num(we, nan=2.0**62), side="right") - 1
    t3 = np.where(np.isfinite(we), t3, -1)
    return t3.astype(np.int64)


def _lookup_prior(table_ids, t_hi, t_lo, per_bar_ids):
    """Anchor = table entry BEFORE the per-bar id. Returns AH, AL, pos."""
    pos = np.searchsorted(table_ids, per_bar_ids)
    good = (pos < len(table_ids)) & \
           (table_ids[np.minimum(pos, len(table_ids) - 1)] == per_bar_ids)
    pos_ok = np.where(good, pos, 0)
    has_prior = good & (pos > 0)
    idx = np.maximum(pos_ok - 1, 0)
    AH = np.where(has_prior, t_hi[idx], np.nan)
    AL = np.where(has_prior, t_lo[idx], np.nan)
    return AH, AL, pos, good


def anchor_d1ut(lane):
    day_id = lane.utc_day_ids()
    did, dh, dl = daily_utc_table()
    AH, AL, pos, good = _lookup_prior(did, dh, dl, day_id)
    win = np.where(good, (day_id + 1).astype(np.float64) * NS_DAY, np.nan)
    return dict(AH=AH, AL=AL, aid=day_id, t3=_t3_from_win(lane, win))


def anchor_d1est(lane):
    ds = lane.est_day_ids()
    s, dh, dl = daily_est_table()
    AH, AL, pos, good = _lookup_prior(s, dh, dl, ds)
    nxt = s[np.minimum(pos + 1, len(s) - 1)]
    win = np.where(good & (pos + 1 < len(s)), nxt.astype(np.float64), np.nan)
    return dict(AH=AH, AL=AL, aid=ds, t3=_t3_from_win(lane, win))


def anchor_w1(lane):
    wk = lane.week_ids()
    s, dh, dl = weekly_table()
    AH, AL, pos, good = _lookup_prior(s, dh, dl, wk)
    nxt = s[np.minimum(pos + 1, len(s) - 1)]
    win = np.where(good & (pos + 1 < len(s)), nxt.astype(np.float64), np.nan)
    return dict(AH=AH, AL=AL, aid=wk, t3=_t3_from_win(lane, win))


def _anchor_prior_candle(lane, src_df):
    """Prior-candle anchors on an explicit source frame (a4h / a1h families)."""
    s_ts = src_df.index.values.astype("int64")      # candle OPEN times, sorted
    ah = src_df["High"].to_numpy(np.float64)
    al = src_df["Low"].to_numpy(np.float64)
    step = float(np.median(np.diff(s_ts))) if len(s_ts) > 2 else NS_HOUR
    cur = np.searchsorted(s_ts, lane.ts, side="right") - 1   # bucket containing ts
    has_anchor = cur >= 1
    AH = np.where(has_anchor, ah[np.maximum(cur - 1, 0)], np.nan)
    AL = np.where(has_anchor, al[np.maximum(cur - 1, 0)], np.nan)
    win_end = np.where(cur >= 0,
                       np.where(cur + 1 < len(s_ts),
                                s_ts[np.minimum(cur + 1, len(s_ts) - 1)].astype(np.float64),
                                float(s_ts[-1]) + step),
                       np.nan)
    aid = np.where(cur >= 0, cur, -1).astype(np.int64)
    return dict(AH=AH, AL=AL, aid=aid, t3=_t3_from_win(lane, win_end))


def anchor_a4h(lane):
    return _anchor_prior_candle(lane, load_bars("BTCUSDT", "4h"))


def anchor_a1h(lane):
    return _anchor_prior_candle(lane, base_1h_df())


def _anchor_first_candle(lane, which):
    """First-candle-of-period anchor. 'utc': 00:00-01:00 UTC candle.
    'est': 08:00-09:00 ET candle. Valid from candle close; window = anchor day."""
    d1h = base_1h_df()
    s_ts = d1h.index.values.astype("int64")
    ah = d1h["High"].to_numpy(np.float64)
    al = d1h["Low"].to_numpy(np.float64)
    if which == "utc":
        day_id = lane.utc_day_ids()
        anchor_open = day_id.astype(np.float64) * NS_DAY
        nxt_start = (day_id + 1).astype(np.float64) * NS_DAY
        aid_base = day_id.astype(np.int64)
    else:
        ds = lane.est_day_ids()
        s_et, _, _ = daily_est_table()
        seg_pos = np.searchsorted(s_et, ds)
        good_day = (seg_pos < len(s_et)) & \
                   (s_et[np.minimum(seg_pos, len(s_et) - 1)] == ds)
        eight = et_0800_starts()
        anchor_open = np.where(good_day,
                               eight[np.minimum(seg_pos, len(eight) - 1)].astype(np.float64),
                               np.nan)
        aid_base = np.where(good_day, ds, -1).astype(np.int64)
        nxt = s_et[np.minimum(seg_pos + 1, len(s_et) - 1)]
        nxt_start = np.where(good_day & (seg_pos + 1 < len(s_et)),
                             nxt.astype(np.float64), np.nan)
    nan_open = np.nan_to_num(anchor_open, nan=-1.0)
    posx = np.searchsorted(s_ts, nan_open, side="left")
    found = np.isfinite(anchor_open) & (posx < len(s_ts)) & \
            (s_ts[np.minimum(posx, len(s_ts) - 1)] == nan_open)
    posf = np.where(found, posx, 0)
    AH0 = np.where(found, ah[np.minimum(posf, len(ah) - 1)], np.nan)
    AL0 = np.where(found, al[np.minimum(posf, len(al) - 1)], np.nan)
    valid_from = np.where(found, anchor_open + NS_HOUR, np.nan)
    ok = found & (lane.ts >= np.nan_to_num(valid_from, nan=2.0**62).astype(np.int64))
    AH = np.where(ok, AH0, np.nan)
    AL = np.where(ok, AL0, np.nan)
    aid = np.where(ok, aid_base, -1).astype(np.int64)
    win = np.where(ok, nxt_start, np.nan)
    return dict(AH=AH, AL=AL, aid=aid, t3=_t3_from_win(lane, win))


def anchor_fc_utc(lane):
    return _anchor_first_candle(lane, "utc")


def anchor_fc_est(lane):
    return _anchor_first_candle(lane, "est")


def anchor_roll(lane, N):
    """PA2 rolling PRIOR-N-bar range (fractal probe). No void, no time stop."""
    AH = pd.Series(lane.h).rolling(N).max().shift(1).to_numpy(np.float64)
    AL = pd.Series(lane.l).rolling(N).min().shift(1).to_numpy(np.float64)
    aid = np.arange(len(AH), dtype=np.int64)     # per-bar context (resets each bar)
    t3 = np.full(len(AH), -1, dtype=np.int64)
    return dict(AH=AH, AL=AL, aid=aid, t3=t3, sticky_pend=True)


ANCHOR_BUILDERS = {
    "d1ut": anchor_d1ut, "d1est": anchor_d1est, "w1": anchor_w1,
    "a4h": anchor_a4h, "a1h": anchor_a1h,
    "fc_utc": anchor_fc_utc, "fc_est": anchor_fc_est,
}


# ------------------------------------------------------------------ scanner

def sweep_scan(lane, an, entry_mode, eps_mode, buf_bp, target_mode,
               time_stop=True, invalidation=True, kz=None):
    """ONE pre-registered simulation pass. Returns (portion trade rows, NAV events).
    entry_mode: 'mkt'|'limit'|'stop'; eps_mode 'strict'|'1bp'; buf_bp {0,2};
    target_mode 't1'|'t2'; kz: optional boolean array gating sweep confirmation."""
    ts, o, h, l, c = lane.ts, lane.o, lane.h, lane.l, lane.c
    n = lane.n
    AH, AL, aid, t3arr = an["AH"], an["AL"], an["aid"], an["t3"]
    trades = []
    events = []
    pos = None
    pend = None
    last_aid = None
    void_hi = void_lo = False
    strict = eps_mode == "strict"
    use_t3 = time_stop and an.get("t3") is not None
    buf = float(buf_bp) * 1e-4

    for i in range(n):
        aid_i = aid[i]
        if aid_i != last_aid:
            last_aid = aid_i
            void_hi = void_lo = False
            if not an.get("sticky_pend", False):
                pend = None                       # new candle: no carry-over

        ah = AH[i]
        al = AL[i]
        ok_ah = ah == ah and ah > 0
        ok_al = al == al and al > 0

        # -- (a) manage the open position (stop -> t2 half -> t1 rest -> t3)
        pos = _manage_pos(pos, i, o, h, l, c, ts, trades, events, lane,
                          target_mode, use_t3, invalidation)

        # -- (b) pending order
        if pos is None and pend is not None:
            lvl = pend["lvl"]
            d = pend["dir"]
            if pend["mode"] == "mkt":
                pos = _open_pos(pend, i, o[i], an, ts, lane, buf)
                pend = None
            elif pend["mode"] == "limit":
                if (d > 0 and o[i] <= lvl) or (d < 0 and o[i] >= lvl):
                    pos = _open_pos(pend, i, o[i], an, ts, lane, buf)
                    pend = None
                elif (d > 0 and l[i] <= lvl) or (d < 0 and h[i] >= lvl):
                    pos = _open_pos(pend, i, lvl, an, ts, lane, buf)
                    pend = None
            else:                                  # near-side stop
                if (d > 0 and o[i] >= lvl) or (d < 0 and o[i] <= lvl):
                    pos = _open_pos(pend, i, o[i], an, ts, lane, buf)
                    pend = None
                elif (d > 0 and h[i] >= lvl) or (d < 0 and l[i] <= lvl):
                    pos = _open_pos(pend, i, lvl, an, ts, lane, buf)
                    pend = None
            if pos is not None:
                pos = _manage_pos(pos, i, o, h, l, c, ts, trades, events, lane,
                                  target_mode, use_t3, invalidation, allow_t3=False)
            elif (pend is not None and pend["t3idx"] >= 0 and i > pend["t3idx"]):
                pend = None

        # -- (c) sweep detection (flat + no pending order + optional KZ gate)
        if pos is None and pend is None and (kz is None or kz[i]):
            if ok_ah:
                pierce = (h[i] > ah) if strict else (h[i] > ah + ah * 1e-4)
                if c[i] > ah and invalidation:
                    void_hi = True
                elif pierce and not void_hi and c[i] <= ah:
                    pend = _schedule(entry_mode, "hi", i, h[i], l[i], ah, al, an, buf, ts)
                    continue
            if ok_al:
                pierce = (l[i] < al) if strict else (l[i] < al - al * 1e-4)
                if c[i] < al and invalidation:
                    void_lo = True
                elif pierce and not void_lo and c[i] >= al:
                    pend = _schedule(entry_mode, "lo", i, h[i], l[i], ah, al, an, buf, ts)

    if pos is not None:
        trades.append(dict(entry_ts=int(pos["entry_ts"]), exit_ts=None, dir=pos["dir"],
                           side=pos["side"], portion=pos["not_rem"], gross=np.nan,
                           fees=np.nan, hair=np.nan, net=np.nan, reason="OPEN@cutoff",
                           entry_idx=int(pos["entry_idx"]), exit_idx=-1,
                           entry_px=float(pos["entry_px"]), exit_px=np.nan,
                           sw_idx=int(pos["sw_idx"]), sw_ts=int(pos["sw_ts"]),
                           dAH=pos["AH"], dAL=pos["AL"]))
    return trades, events


def _schedule(entry_mode, side, i, hg, lw, ah, al, an, buf, ts):
    d = -1 if side == "hi" else +1
    pend = dict(mode=entry_mode, dir=d, side=side, buf=buf,
                hg=hg, lw=lw, ah=ah, al=al, wi=int(i), sw_ts=int(ts[i]))
    if entry_mode == "mkt":
        pend["lvl"] = None
    elif entry_mode == "limit":
        pend["lvl"] = (hg + lw) / 2.0
    else:
        pend["lvl"] = (lw if d > 0 else hg)
    pend["t3idx"] = int(an["t3"][i])
    return pend


def _open_pos(pend, i, px, an, ts, lane, buf_unused):
    side = pend["side"]
    d = pend["dir"]
    ah, al = pend["ah"], pend["al"]
    buf = float(pend["buf"])
    if side == "hi":                        # buyside swept -> SHORT
        stop = pend["hg"] * (1.0 + buf)
        t1 = al
        level = ah
    else:                                   # sellside swept -> LONG
        stop = pend["lw"] * (1.0 - buf)
        t1 = ah
        level = al
    m2 = (ah + al) / 2.0
    return dict(side=side, dir=d, entry_px=float(px), entry_idx=int(i),
                entry_ts=int(ts[i]), stop=float(stop), T1=float(t1),
                M2=float(m2), level=float(level), not_rem=NOTION, half_done=False,
                t3idx=int(an["t3"][i]), sw_idx=pend["wi"],
                sw_ts=pend["sw_ts"] if pend["sw_ts"] >= 0 else int(ts[i]),
                AH=float(ah), AL=float(al))


def _manage_pos(pos, i, o, h, l, c, ts, trades, events, lane,
                target_mode, use_t3, invalidation, allow_t3=True):
    if pos is None:
        return None
    d = pos["dir"]
    stop = pos["stop"]
    hit_stop = (l[i] <= stop) if d > 0 else (h[i] >= stop)
    if hit_stop:
        px = (o[i] if ((d > 0 and o[i] <= stop) or (d < 0 and o[i] >= stop)) else stop)
        _exit(pos, i, px, pos["not_rem"], "stop", trades, events, ts, lane)
        return None
    if target_mode == "t2" and not pos["half_done"]:
        m2 = pos["M2"]
        hit_t2 = (h[i] >= m2) if d > 0 else (l[i] <= m2)
        if hit_t2:
            px = (o[i] if ((d > 0 and o[i] >= m2) or (d < 0 and o[i] <= m2)) else m2)
            _exit(pos, i, px, 50.0, "t2", trades, events, ts, lane)
            pos["half_done"] = True
    t1 = pos["T1"]
    hit_t1 = (h[i] >= t1) if d > 0 else (l[i] <= t1)
    if hit_t1 and pos["not_rem"] > 1e-9:
        px = (o[i] if ((d > 0 and o[i] >= t1) or (d < 0 and o[i] <= t1)) else t1)
        _exit(pos, i, px, pos["not_rem"], "t1", trades, events, ts, lane)
    ti = pos["t3idx"]
    if use_t3 and allow_t3 and ti >= 0 and i >= ti and pos["not_rem"] > 1e-9:
        lv = pos["level"]
        void = (c[i] < lv) if d > 0 else (c[i] > lv)
        reason = "void" if invalidation and void else "t3"
        _exit(pos, i, c[i], pos["not_rem"], reason, trades, events, ts, lane)
    return None if pos["not_rem"] <= 1e-9 else pos


def _exit(pos, i, px, portion, reason, trades, events, ts, lane):
    d = pos["dir"]
    entry_px = pos["entry_px"]
    exit_ts = int(ts[i]) + int(lane.tf_ns)
    days = (exit_ts - pos["entry_ts"]) / NS_DAY
    gross = d * portion * (px / entry_px - 1.0)
    fee_ent = portion * FEE                 # proportional entry share
    fee_ext = portion * FEE
    hair = portion * HAIR * days
    net = gross - fee_ent - fee_ext - hair
    trades.append(dict(entry_ts=int(pos["entry_ts"]), exit_ts=exit_ts, dir=d,
                       side=pos["side"], portion=portion, gross=float(gross),
                       fees=float(fee_ent + fee_ext), hair=float(hair),
                       net=float(net), reason=reason, entry_idx=int(pos["entry_idx"]),
                       exit_idx=int(i), entry_px=float(entry_px), exit_px=float(px),
                       sw_idx=int(pos["sw_idx"]), sw_ts=int(pos["sw_ts"]),
                       dAH=pos["AH"], dAL=pos["AL"]))
    events.append((exit_ts, float(net)))
    pos["not_rem"] = max(0.0, pos["not_rem"] - portion)
