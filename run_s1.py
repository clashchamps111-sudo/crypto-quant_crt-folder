"""RUN SCOPE S1 (crt/REGISTRY.md, declared 2026-11-10, spec v1.0, user GO).
Wires the 73 declared cells / 352 parameter runs VERBATIM (assert in code).
One simulation pass per combo; shared stream per lane (5m/1m fetched windowed,
in-RAM, raw discarded); forensics gate (0 tolerance); writes
crt/battery_S1_report.md + KB-scale crt/data_agg artifacts. BTC primary only.
Own-files-only: nothing outside crypto-quant/crt/ is written."""
import collections
import os
import sys
import time

import numpy as np
import pandas as pd

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import stream_engine as SE                                   # noqa: E402
from stream_engine import (ANCHOR_BUILDERS, JUDGE_NS, kz_mask, sweep_scan,   # noqa: E402
                           anchor_roll, base_1h_df, daily_utc_table,
                           daily_est_table, weekly_table, et_0800_starts,
                           load_bars, agg_from)

OUT = os.path.join(_HERE, "battery_S1_report.md")
AGG_D = SE.AGG
NSD = 86_400.0
TRIGGER_LANES = ["1m", "5m", "15m", "1h", "4h", "daily"]
ENTRY_NAME = {"mkt": "D1", "limit": "D2", "stop": "D3"}
EPS_DEFAULT = "strict"

ANG_TXT = {
    "d1ut": "prior UTC D1 candle", "d1est": "prior EST(DST) D1 candle",
    "w1": "prior W1 candle (W-SUN)", "a4h": "prior 4h candle",
    "a1h": "prior 1h candle", "fc_utc": "first 1h of UTC day",
    "fc_est": "first 1h of ET day (08:00-09:00 ET)",
}


# ------------------------------------------------------------------ regime map

def regime_map():
    """p2_pairs.regime_map inheritance: BTC trailing-30d return at month end;
    >= +10% bull, <= -10% bear, else sideways. pandas 3.x 'ME'."""
    d = agg_from(load_bars("BTCUSDT", "1h"), "1D")
    ret30 = d["Close"].pct_change(30)
    month_end = d.groupby(pd.Grouper(freq="ME"))["Close"].last().dropna()
    lab = {}
    for m in month_end.index:
        r = float(ret30.asof(m))
        lab[pd.Timestamp(m).to_period("M")] = ("bull" if r >= 0.10 else
                                               "bear" if r <= -0.10 else "sideways")
    return lab


# ------------------------------------------------------------------ stats core

def line_stats(trades, events, rmap, span_days):
    closed = [t for t in trades if t["reason"] != "OPEN@cutoff"]
    jrows = [t for t in closed if t["entry_ts"] >= JUDGE_NS]
    trows = [t for t in closed if t["entry_ts"] < JUDGE_NS]
    net_j = sum(t["net"] for t in jrows)
    gross_j = sum(t["gross"] for t in jrows)
    net_t = sum(t["net"] for t in trows)
    wins = sum(t["net"] for t in jrows if t["net"] > 0)
    losses = sum(-t["net"] for t in jrows if t["net"] < 0)
    if losses > 1e-12:
        pf = wins / losses
    else:
        pf = float("inf") if wins > 0 else float("nan")
    exits = collections.Counter(t["reason"] for t in jrows)
    jevents = sorted((ts, amt) for (ts, amt) in events if ts >= JUDGE_NS)
    cum = peak = 0.0
    mdd = 0.0
    for _ts, amt in jevents:
        cum += amt
        if cum > peak:
            peak = cum
        mdd = min(mdd, cum - peak)
    bk = {k: [0.0, 0] for k in ("bull", "sideways", "bear")}
    for t in jrows:
        b = rmap.get(pd.Timestamp(t["entry_ts"]).to_period("M"), "sideways")
        bk[b][0] += t["net"]
        bk[b][1] += 1
    ypct = net_j * 365.25 / span_days if span_days > 0 else float("nan")
    return dict(net_j=net_j, gross_j=gross_j, net_t=net_t, n_j=len(jrows),
                n_t=len(trows), pf=pf, y=ypct, mdd=mdd, exits=dict(exits),
                bull=bk["bull"][0], bull_n=bk["bull"][1],
                sideways=bk["sideways"][0], sideways_n=bk["sideways"][1],
                bear=bk["bear"][0], bear_n=bk["bear"][1],
                bar_a=net_j > 0, bar_b=ypct >= 4.77, bar_c=ypct >= 6.82,
                bar_d=ypct >= 20.0, floor=len(jrows) >= 8)


def autopsy_of(st):
    """PREMISE-DEATH if judge gross <= 0; COST-DEATH if gross > 0 but net <= 0;
    STAT-STERILE if floor unmet. REGIME-FLAGS appended for positive non-empty
    buckets (flagged, never buried; flags do NOT change the death tags)."""
    if not st["floor"]:
        tag = "STAT-STERILE"
    elif st["gross_j"] <= 0:
        tag = "PREMISE-DEATH"
    elif st["net_j"] <= 0:
        tag = "COST-DEATH"
    else:
        tag = "ALIVE"
    flags = []
    if st["bull_n"] and st["bull"] > 0:
        flags.append("bull +%0.2f" % st["bull"])
    if st["sideways_n"] and st["sideways"] > 0:
        flags.append("side +%0.2f" % st["sideways"])
    if st["bear_n"] and st["bear"] > 0:
        flags.append("bear +%0.2f" % st["bear"])
    if flags:
        tag += " | FLAG[" + "; ".join(flags) + "]"
    return tag


def alive_line(st, at):
    return st["floor"] and st["bar_a"]


# ------------------------------------------------------------ cell definition

def _probe1():
    return [dict(entry="mkt", target="t1", time_stop=True, invalidation=True,
                 buf=b, eps=e, lbl="D1")
            for b in (0, 2) for e in ("strict", "1bp")]            # PA1: 4


def _probe2():
    return [dict(entry="mkt", target="t1", time_stop=False, invalidation=False,
                 buf=b, eps="strict", lbl="D1") for b in (0, 2)]    # PA2: 2


def _full(entries):
    return [dict(entry=e, buf=b, target=t, time_stop=True, invalidation=True,
                 eps="strict",lbl=ENTRY_NAME[e])
            for e in entries for b in (0, 2) for t in ("t1", "t2")]


def _kzfull(entries, buffers):
    out = []
    for e in entries:
        for t in ("t1", "t2"):
            for b in buffers:
                out.append(dict(entry=e, buf=b, target=t, time_stop=True,
                                invalidation=True, eps="strict",
                                lbl=ENTRY_NAME[e]))
    return out


def build_cells(only_lanes=None):
    cells = []
    for ak, label, lanes in (
            ("d1ut", "D1UT", ["1m", "5m", "15m", "1h", "4h"]),
            ("w1", "W1", ["1m", "5m", "15m", "1h", "4h", "daily"]),
            ("d1est", "D1EST", ["1m", "5m", "15m", "1h", "4h"])):
        for ln in lanes:
            cells.append(dict(id="PA1-%s x %s" % (label, ln), family="PA1",
                              anchor=ak, lane=ln, cfgs=_probe1(), kz=None, N=None))
    for ln in TRIGGER_LANES:
        for N in (3, 5, 12):
            cells.append(dict(id="PA2-N%d x %s" % (N, ln), family="PA2",
                              anchor=("roll", N), lane=ln, cfgs=_probe2(),
                              kz=None, N=N))
    for ln in ("5m", "15m", "1h"):
        cells.append(dict(id="V1 x %s" % ln, family="V1", anchor="d1ut", lane=ln,
                          cfgs=_full(("mkt", "limit", "stop")), kz=None, N=None))
        cells.append(dict(id="V1-E x %s" % ln, family="V1", anchor="d1est", lane=ln,
                          cfgs=_full(("mkt", "limit", "stop")), kz=None, N=None))
        for kz in ("London", "NYAM"):
            cells.append(dict(id="V1-KZ(%s) x %s" % (kz, ln), family="V1-KZ",
                              anchor="d1ut", lane=ln,
                              cfgs=_kzfull(("mkt", "limit", "stop"), (2,)),
                              kz=kz, N=None))
    for ak, alab in (("fc_utc", "D1.UTC-1h"), ("fc_est", "D1.EST-1h")):
        for ln in ("5m", "15m"):
            cells.append(dict(id="V2(%s) x %s" % (alab, ln), family="V2",
                              anchor=ak, lane=ln, cfgs=_full(("mkt", "stop")),
                              kz=None, N=None))
            for kz in ("London", "NYAM"):
                cells.append(dict(id="V2-KZ(%s,%s) x %s" % (alab, kz, ln),
                                  family="V2-KZ", anchor=ak, lane=ln,
                                  cfgs=_kzfull(("mkt", "stop"), (2,)), kz=kz, N=None))
    for ak, alab, lanes in (("a4h", "4h-prior", ("5m", "15m")),
                            ("a1h", "1h-prior", ("1m", "5m", "15m"))):
        for ln in lanes:
            cells.append(dict(id="V3(%s) x %s" % (alab, ln), family="V3",
                              anchor=ak, lane=ln, cfgs=_full(("mkt", "stop")),
                              kz=None, N=None))
    for ak, alab, lanes in (("a1h", "1h-prior", ("1m", "5m", "15m")),
                            ("a4h", "4h-prior", ("5m", "15m"))):
        for ln in lanes:
            for kz in ("London", "NYAM"):
                cells.append(dict(id="V3-KZ(%s,%s) x %s" % (alab, kz, ln),
                                  family="V3-KZ", anchor=ak, lane=ln,
                                  cfgs=_kzfull(("mkt", "stop"), (2,)), kz=kz, N=None))
    if only_lanes is not None:
        cells = [c for c in cells if c["lane"] in only_lanes]
        print("[s1] lane-filtered smoke: %d cells / %d runs (diagnostic, not a scope)"
              % (len(cells), sum(len(c["cfgs"]) for c in cells)), flush=True)
    else:
        assert len(cells) == 73, "cell count drift: %d" % len(cells)
        assert sum(len(c["cfgs"]) for c in cells) == 352, "run count drift"
    return cells


def cfg_label(cfg):
    buf = cfg["buf"]
    eps = {"strict": "", "-": "", "1bp": "-e1bp"}[cfg["eps"]]
    return "%s%s-b%dbp-t%s" % (cfg["lbl"], eps, buf, cfg["target"].upper())


# ------------------------------------------------------------------ forensics

def verify_rows(lane, an, rows, cfg):
    """Independent bar-level re-derivation for a sample of judge rows. Zero
    tolerance by declaration (audit standard). Returns (checked, mismatches)."""
    ts, o, h, l, c = lane.ts, lane.o, lane.h, lane.l, lane.c
    AH, AL, t3arr = an["AH"], an["AL"], an["t3"]
    cand = [t for t in rows if t["entry_ts"] >= JUDGE_NS
            and t["reason"] != "OPEN@cutoff"]
    cand = cand[:40]
    checked = 0
    bad = []
    for t in cand:
        i = int(t["sw_idx"])
        j = int(t["entry_idx"])
        k = int(t["exit_idx"])
        d = int(t["dir"])
        ah = float(AH[i])
        al = float(AL[i])
        ok = True
        # 1) anchor snapshot matches the anchor arrays at the sweep bar
        if abs(ah - float(t["dAH"])) > 1e-15 or abs(al - float(t["dAL"])) > 1e-15:
            ok = False
        # 2) sweep condition at the sweep bar (re-derived from raw bars)
        if d < 0:
            eps = 0.0 if cfg["eps"] == "strict" else ah * 1e-4
            if not ((h[i] > ah + eps) and (c[i] <= ah)):
                ok = False
        else:
            eps = 0.0 if cfg["eps"] == "strict" else al * 1e-4
            if not ((l[i] < al - eps) and (c[i] >= al)):
                ok = False
        # 3) order levels re-derived (buffer applies to the sweep extreme)
        ext = h[i] if d < 0 else l[i]
        stop_exp = ext * (1.0 + cfg["buf"] * 1e-4) if d < 0 else ext * (1.0 - cfg["buf"] * 1e-4)
        t1_exp = al if d < 0 else ah
        m2_exp = (ah + al) / 2.0
        # 4) fill px per mode + gap rule
        if cfg["entry"] == "mkt":
            exp_px = o[j]
        else:
            lvl = (h[i] + l[i]) / 2.0 if cfg["entry"] == "limit" else \
                  (l[i] if d > 0 else h[i])
            if d > 0:
                exp_px = o[j] if o[j] <= lvl else (lvl if l[j] <= lvl else np.nan)
            else:
                exp_px = o[j] if o[j] >= lvl else (lvl if h[j] >= lvl else np.nan)
        if not np.isfinite(exp_px) or abs(float(t["entry_px"]) - exp_px) > 1e-12:
            ok = False
        # 5) exit px per reason (stop-first conservatism; gap rule)
        if k >= 0:
            r = t["reason"]
            if r == "stop":
                exp = o[k] if ((d > 0 and o[k] <= stop_exp) or
                               (d < 0 and o[k] >= stop_exp)) else stop_exp
                cond = ((l[k] <= stop_exp) if d > 0 else (h[k] >= stop_exp))
            elif r == "t1":
                exp = (o[k] if ((d > 0 and o[k] >= t1_exp) or
                                (d < 0 and o[k] <= t1_exp)) else t1_exp)
                cond = ((h[k] >= t1_exp) if d > 0 else (l[k] <= t1_exp))
            elif r == "t2":
                exp = (o[k] if ((d > 0 and o[k] >= m2_exp) or
                                (d < 0 and o[k] <= m2_exp)) else m2_exp)
                cond = ((h[k] >= m2_exp) if d > 0 else (l[k] <= m2_exp))
                cond = cond and abs(t["portion"] - 50.0) < 1e-9
            elif r in ("t3", "void"):
                exp = c[k]
                cond = (k == int(t3arr[int(t["entry_idx"])]))
            else:
                exp = np.nan
                cond = False
            good = cond and np.isfinite(exp) and abs(float(t["exit_px"]) - exp) <= 1e-9
            if not good:
                ok = False
        checked += 1
        if not ok:
            bad.append((t["entry_ts"], cfg["lbl"], cfg["buf"], cfg["target"]))
    return checked, bad


# --------------------------------------------------------------------- report

def fmt(v, dd=2):
    if v != v:
        return "n/a"
    if v == float("inf"):
        return "inf"
    return ("%+." + str(dd) + "f") % v


def header_md(end_common, n_cells, n_runs, span_days):
    L = ["# CRT BATTERY S1 REPORT (Scope S1, spec v1.0)",
         "",
         "Pre-registered 2026-11-10 in crt/REGISTRY.md; judge = [2025-11-05 ->",
         "data end], ABSOLUTE anchor (S6/S10 precedent). One simulation pass per",
         "combo; all lines reported; no train-selected pick biases anything.",
         "",
         "**Conventions (registry spec v1.0, verbatim):**",
         "- Unit per $100 NOTIONAL per position, BTC primary (ETH cross-check only",
         "  on a survivor -> later scope). Per-capital = /2 (1x USDT-M).",
         "- 7bp/side taker per fill (entry fee share proportional per portion);",
         "  3bp/day haircut per $1 held per portion; no funding credit (S10).",
         "- MDD = trade-exit-stream NAV ($; monitor, not a bar). PF on NET.",
         "- Trade rows are PORTION records; T2 midpoint-split trips appear as two",
         "  rows; floor = >= 8 closed JUDGE rows.",
         "- Bars: A net>0 | B >= +4.77%/yr | C >= +6.82%/yr | D >= +20%/yr notional",
         "  (D = double-digit per capital at 1x).",
         "- Execution: mkt fills next trigger-bar open; limit fills at sweep-bar",
         "  midpoint; stop fills at sweep-bar near side; gap-through fills at bar",
         "  open; STOP-first under same-bar conflicts; sweep precedence 'hi' then",
         "  'lo'; careers ignored while a position/pend is alive; pendings cancel",
         "  at window end (unfilled = no fee); KZ cells require the sweep confirm",
         "  bar's open-time inside the window (ET clock, DST-native).",
         "- Anchors: T3/monitoring window = the CURRENT anchor-TF candle; A1 anchor",
         "  levels from the PRIOR candle; first-candle anchors valid from candle",
         "  close; PA2 rolling prior-N trigger-bar range has no void and no time",
         "  stop (declared); structure invalidation fires with the anchor-TF close",
         "  (reason labeled void vs t3).",
         "",
         "**Judge span:** enabled %d cells / %d lines; span %.3f days; data end %s"
         % (n_cells, n_runs, span_days, pd.Timestamp(end_common)),
         ""]
    return L


def anchor_tables_dump():
    """KB-scale crt/data_agg artifacts: anchor tables (declared aggregates)."""
    pth = os.path.join(AGG_D, "anchors")
    os.makedirs(pth, exist_ok=True)
    did, dh, dl = daily_utc_table()
    ts = (did * SE.NS_DAY).astype("int64")
    pd.DataFrame({"day_start": pd.to_datetime(ts), "anchor_high": dh,
                  "anchor_low": dl}).to_csv(os.path.join(pth, "daily_utc.csv"),
                                            index=False)
    s, eh, el = daily_est_table()
    pd.DataFrame({"et_day_start_utc": pd.to_datetime(s), "anchor_high": eh,
                  "anchor_low": el}).to_csv(os.path.join(pth, "daily_est.csv"),
                                            index=False)
    ws, wh, wl = weekly_table()
    pd.DataFrame({"week_start": pd.to_datetime(ws), "anchor_high": wh,
                  "anchor_low": wl}).to_csv(os.path.join(pth, "weekly.csv"),
                                            index=False)
    d1h = base_1h_df()
    s_ts = d1h.index.values.astype("int64")
    for tag, opens in (("fc_utc", (daily_utc_table()[0] * SE.NS_DAY)),
                       ("fc_est", et_0800_starts())):
        op = pd.DatetimeIndex(opens)
        pos = op.get_indexer(op)
        pos = np.searchsorted(s_ts, opens.astype("int64"), side="left")
        ok = (pos < len(s_ts)) & (s_ts[np.minimum(pos, len(s_ts) - 1)] == opens.astype("int64"))
        posc = np.where(ok, pos, 0)
        pd.DataFrame({"anchor_open": pd.to_datetime(opens.astype("int64")),
                      "anchor_high": np.where(ok, d1h["High"].to_numpy()[np.minimum(posc, len(posc) - 1)], np.nan),
                      "anchor_low": np.where(ok, d1h["Low"].to_numpy()[np.minimum(posc, len(posc) - 1)], np.nan),
                      }).dropna().to_csv(os.path.join(pth, tag + ".csv"), index=False)


# ----------------------------------------------------------------------- main

def main(only_lanes=None):
    t0 = time.time()
    cells = build_cells(only_lanes)
    n_runs = sum(len(c["cfgs"]) for c in cells)
    rmap = regime_map()
    rcnt = collections.Counter(rmap.values())
    print("[s1] regime months: %s (S10 continuity expects 33/14/14)" % dict(rcnt),
          flush=True)

    # common absolute end = last bar ts over the disk lanes
    end_common = None
    for tf in ("1h", "15m", "4h"):
        idx = load_bars("BTCUSDT", tf).index
        v = int(idx[-1].value)
        end_common = v if end_common is None else min(end_common, v)
    span_days = (end_common - JUDGE_NS) / 1e9 / NSD
    print("[s1] common end %s | judge span %.3f d" % (pd.Timestamp(end_common), span_days),
          flush=True)

    lanes = {}
    anchors = {}

    def get_lane(tf):
        if tf not in lanes:
            tl = time.time()
            print("[s1] building lane %s ..." % tf, flush=True)
            lane = SE.Lane("BTCUSDT", tf, start_ts=pd.Timestamp("2021-11-05"),
                           end_ts=pd.Timestamp(end_common))
            lane.truncate_to_common_end(end_common)   # uniform common end (declared)
            lanes[tf] = lane
            print("[s1] lane %s: %s bars %s -> %s (%.0fs, %s)"
                  % (tf, format(lane.n, ","), pd.Timestamp(lane.ts[0]),
                     pd.Timestamp(lane.ts[-1]), time.time() - tl, lane.source),
                  flush=True)
        return lanes[tf]

    def get_anchor(ak, lane, N=None):
        key = ("roll%d" % N if N else ak, lane.tf)
        if key not in anchors:
            tl = time.time()
            if N:
                anchors[key] = anchor_roll(lane, N)
            else:
                anchors[key] = ANCHOR_BUILDERS[ak](lane)
            print("[s1] anchor %s @%s ready (%.1fs)" % (key[0], lane.tf,
                                                        time.time() - tl), flush=True)
        return anchors[key]

    surv = []
    tags = collections.Counter()
    surv_detail = []
    summary_rows = []
    report = header_md(end_common, len(cells), n_runs, span_days)

    for cidx, cel in enumerate(cells, 1):
        lane = get_lane(cel["lane"])
        an = get_anchor(cel["anchor"], lane, cel["N"])
        kz = kz_mask(lane, cel["kz"]) if cel["kz"] else None
        atext = ("rolling prior-%d trigger bars" % cel["N"]
                 if cel["N"] else ANG_TXT[cel["anchor"]])
        hdr = ["", "### %s" % cel["id"], "",
               "(%s | trigger %s | %d combos%s)"
               % (atext, cel["lane"], len(cel["cfgs"]),
                  " | KZ %s (ET clock)" % cel["kz"] if cel["kz"] else ""),
               "",
               "| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ |"
               " net B/S/D | exits | A B C D | floor | row count | autopsy |",
               "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        a_of_cell = 0
        for cfg in cel["cfgs"]:
            trades, events = sweep_scan(
                lane, an, entry_mode=cfg["entry"], eps_mode=cfg["eps"],
                buf_bp=cfg["buf"], target_mode=cfg["target"],
                time_stop=cfg["time_stop"], invalidation=cfg["invalidation"],
                kz=kz)
            st = line_stats(trades, events, rmap, span_days)
            at = autopsy_of(st)
            tags[at.split(" |")[0]] += 1
            bars = "%s %s %s %s" % tuple(("P" if ok else "F") for ok in
                                         (st["bar_a"], st["bar_b"], st["bar_c"],
                                          st["bar_d"]))
            netbsc = "%+.2f / %+.2f / %+.2f / %+.2f" % (st["bull"], st["sideways"],
                                                        st["bear"], st["net_t"])
            pf_s = fmt(st["pf"])
            live = st["floor"] and st["bar_a"]
            if live:
                a_of_cell += 1
                surv.append((cel["id"], cfg["lbl"], cfg["eps"], cfg["buf"],
                             cfg["target"], st))
                jr = [t for t in trades if t["entry_ts"] >= JUDGE_NS
                      and t["reason"] != "OPEN@cutoff"]
                for t in jr:
                    if len(surv_detail) < 200000:
                        surv_detail.append(dict(cell=cel["id"], combo=cfg_label(cfg),
                                                entry_ts=int(t["entry_ts"]),
                                                exit_ts=(None if t["exit_ts"] is None
                                                         else int(t["exit_ts"])),
                                                dir=t["dir"], side=t["side"],
                                                portion=t["portion"], net=t["net"],
                                                reason=t["reason"],
                                                entry_px=t["entry_px"],
                                                exit_px=t["exit_px"]))
            exits_s = ",".join("%s=%d" % (k, v) for k, v in sorted(st["exits"].items()))
            op = sum(1 for t in trades if t["reason"] == "OPEN@cutoff"
                     and t["entry_ts"] >= JUDGE_NS)
            bold = "**" if live else ""
            hdr.append("| %s%s%s | %s%s%s | %s | %s | %s | %d / %d | %s | %s | %s | %s | %s | open=%d | %s |"
                       % (bold, cfg_label(cfg), bold,
                          bold, fmt(st["net_j"]), bold, fmt(st["net_t"]),
                          fmt(st["y"]), pf_s, st["n_j"], st["n_t"], fmt(st["mdd"]),
                          netbsc, exits_s, bars,
                          ("OK" if st["floor"] else "thin"), op, at))
            summary_rows.append(dict(cell=cel["id"], family=cel["family"],
                                     combo=cfg_label(cfg),
                                     net_j=round(st["net_j"], 4),
                                     net_t=round(st["net_t"], 4),
                                     y_j=round(st["y"], 3), rows_j=st["n_j"],
                                     autopsy=at))
        if a_of_cell:
            hdr.append("")
            hdr.append("**%d line(s) in this cell cleared bar A with the floor ->"
                       " SURVIVAL FLAG (contract: CRT stays OPEN).**" % a_of_cell)
        report.extend(hdr)
        print("[s1] cell %d/%d %s done (t+%.0fs, alive=%d)"
              % (cidx, len(cells), cel["id"], time.time() - t0, a_of_cell), flush=True)

    # ---- forensics gate (fixed representative set; zero tolerance)
    fore = ["", "## Forensics gate (bar-level re-derivation, 0 tolerance)", ""]
    fully_checked = 0
    fails = []
    want = []
    seenf = set()
    for cel in cells:
        keyc = (cel["family"], cel["cfgs"][0]["entry"])
        if keyc in seenf:
            continue
        seenf.add(keyc)
        want.append(cel)
    want = want[:16]
    for cel in want:
        lane = get_lane(cel["lane"])
        an = get_anchor(cel["anchor"], lane, cel["N"])
        kz = kz_mask(lane, cel["kz"]) if cel["kz"] else None
        cfg = cel["cfgs"][0]
        trades, _ = sweep_scan(lane, an, cfg["entry"], cfg["eps"], cfg["buf"],
                               cfg["target"], cfg["time_stop"],
                               cfg["invalidation"], kz)
        n_ok, bad = verify_rows(lane, an, trades, cfg)
        fully_checked += n_ok
        note = "PASS" if not bad else "FAIL(%d)" % len(bad)
        fore.append("- %s [%s]: %d judge rows checked -> %s"
                    % (cel["id"], cfg_label(cfg), n_ok, note))
        if bad:
            fails.extend([(cel["id"], b) for b in bad])
    fore.append("")
    fore.append("- TOTAL rows independently re-derived: %d; mismatches: %d"
                % (fully_checked, len(fails)))
    report.extend(fore)

    # ---- summary
    report += ["", "## S1 summary", "",
               "- Lines judged: %d. Autopsy tags: %s" % (len(summary_rows), dict(tags))]
    report.append("- Survivor lines (bar A + floor): %d" % len(surv))
    for s in surv[:50]:
        cid, ent, eps, buf, tgt, st = s
        report.append("  - %s / %s%s-b%dbp-t%s: net $%.2f (%+.2f%%/yr notional), "
                      "PF %s, B/S/D %+.2f/%+.2f/%+.2f, MDD $%.2f, rows %d"
                      % (cid, ent, {"strict": "", "1bp": "-e1bp"}[eps], buf,
                         tgt.upper(), st["net_j"], st["y"], fmt(st["pf"]),
                         st["bull"], st["sideways"], st["bear"], st["mdd"],
                         st["n_j"]))
    if len(surv) > 50:
        report.append("  - ... (+%d more survivor lines)" % (len(surv) - 50))
    if not fails:
        report.append("- Forensics: PASS (all sampled fills re-derived exactly; "
                      "verdicts stand).")
    else:
        report.append("- Forensics: **FAIL** -> verdicts frozen; fix before trust.")
    report += ["", "## Data + artifact stamps", ""]
    for tf, ln in lanes.items():
        report.append("- lane %s: %s bars %s -> %s (%s)"
                      % (tf, format(ln.n, ","), pd.Timestamp(ln.ts[0]),
                         pd.Timestamp(ln.ts[-1]), ln.source))
    report += ["- anchors: UTC/EST daily + W-SUN weekly from 1h deep; 4h/1h from "
               "source candles; first-candle from the 1h grid; rolling N at trigger",
               "- regime months: %s" % dict(rcnt),
               "- artifacts: crt/data_agg/anchors/*.csv (KB-scale), "
               "crt/data_agg/s1_lines.csv, crt/data_agg/s1_survivor_trades.csv",
               "- registry: Scope S1 executed; per-line verdicts above; global "
               "closure reading deferred to the CP2 review (user owns it)"]

    # ---- write artifacts
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(report))
    os.makedirs(AGG_D, exist_ok=True)
    pd.DataFrame(summary_rows).to_csv(os.path.join(AGG_D, "s1_lines.csv"), index=False)
    if surv_detail:
        pd.DataFrame(surv_detail[:60000]).to_csv(
            os.path.join(AGG_D, "s1_survivor_trades.csv"), index=False)
    else:
        open(os.path.join(AGG_D, "s1_survivor_trades.csv"), "w").close()
    try:
        anchor_tables_dump()
    except Exception as e:      # artifact failure is NOT verdict-threatening
        print("[s1] anchor-table dump warn: %s" % e, flush=True)
    for tf, ln in lanes.items():
        if tf in ("1m", "5m"):
            ln.drop_raw()
            print("[s1] raw %s discarded (storage rule)" % tf, flush=True)
    if only_lanes is None:
        removed = 0
        if os.path.isdir(SE.CACHE_RAW):
            for fname in os.listdir(SE.CACHE_RAW):
                p = os.path.join(SE.CACHE_RAW, fname)
                try:
                    if os.path.isfile(p):
                        os.remove(p)
                        removed += 1
                except Exception:
                    pass
        print("[s1] user-ratified raw fetch checkpoints deleted after success: "
              "%d file(s)" % removed, flush=True)
    print("[s1] S1 COMPLETE -> %s (%.0fs wall; %d lines; %d survivors; "
          "forensics %s)" % (OUT, time.time() - t0, len(summary_rows), len(surv),
                             "PASS" if not fails else "FAIL"), flush=True)


if __name__ == "__main__":
    main()
