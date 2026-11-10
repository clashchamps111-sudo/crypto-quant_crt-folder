# CRT REGISTRY

Per crt/CHARTER.md §6. Columns: date | spec version | scope cells declared |
cells run | verdict per cell | survival flags | revision reason codes.

Rules (verbatim inheritance):
- A scope is declared BEFORE compute with its FULL cell list. No compute
  outside a declared scope. No cell list may overlap a USED scope's cells
  (the audit below runs at every future pre-registration).
- Unlimited revisions permitted; each is a FRESH pre-registration adding
  new testable scope. Re-running any dead cell of a used scope is BANNED
  forever.
- Every dead cell is stamped with its autopsy line:
  PREMISE-DEATH (logic falsified OOS) | COST-DEATH (edge < costs after
  7bp/side + 3bp/day accounting) | STAT-STERILE (< 8 closed judge trades) |
  REGIME-FLAG (positive non-empty bucket exists - flagged, never buried).
- Any surviving cell keeps CRT OPEN as a flagged candidate.

## CONTRACT RATIFICATION LOG

| date | event | record |
|---|---|---|
| 2026-11-10 | CP1 ratification | Ground truth = the CHARTER §4 + dossier v1.0 public-definition draft set (prior-candle + first-candle + N-bar anchors; strict/eps sweeps with close-void semantics; D1-D4 entries; stop=sweep extreme + buffer; targets T1=anchor opposite side / T2=midpoint-partial / T3=time-stop-at-anchor-close; structure invalidation = anchor-TF close beyond level voids; killzones optional). User answers: draft set ratified; killzones = defaults (America/New_York clock, DST-native: London KZ 02:00-05:00, NY AM KZ 07:00-10:00; G0 24h control rows kept); "None - freeze v1.0". Spec v1.0 FROZEN. |
| 2026-11-10 | Scope S1 declared | Full cell list below. NO COMPUTE RUN YET. |

## SPEC v1.0 — FROZEN CONSTANTS (inherit; never drift onward)

- Unit: per $100 NOTIONAL, single position, BTC only (ETH cross-check row
  only on a BTC survivor, later scope). Per-capital = /2 (USDT-M 1x).
- Costs: 7bp/side taker every fill; haircut 3bp/day per $1 held notional
  (no funding credit; direction-agnostic, standing S10 convention).
- Execution realism: decision at trigger-bar close; D1-market entries fill
  next trigger-bar OPEN; D2 limit fills at level when bar range touches
  (bar OPENS beyond level -> fill at open); D3 stop fills at level when
  touched (gap -> fill at open). Same-bar stop+target both touched ->
  STOP counted first (conservatism). Time-stop (T3) fills at the closing
  trigger-bar close of the anchor candle, taker.
- Judge: train [data start -> 2025-11-05), judge [2025-11-05 -> data end
  (~2026-11-09)], ABSOLUTE anchor (S6/S10 precedent). In-window entries
  only; realized-only (open-at-cutoff unbooked); annualization net% x
  365.25/judge_span_days. Four-bar per line: A net>0; B >= +4.77%/yr;
  C >= +6.82%/yr; D >= +20%/yr (= double-digit per capital at 1x).
- Per-combo lines ALL reported (no train selection bias; frozen transfer
  not needed because nothing is picked onto the judge). MDD = close-to-
  close NAV stream while positioned. Stat floor: >= 8 closed judge trades
  else the line is STAT-STERILE.
- Regime split (mandatory): month = bull >= +10% / bear <= -10% else
  sideways, by BTC trailing-30d at month end (regime_map pattern; pandas
  3.x "ME").
- Session anchors run SEPARATELY, never blended: UTC (data-native,
  bar open times) vs EST (America/New_York day boundary 08:00 ET,
  DST-native). Killzone clock = America/New_York (DST-native). Weekly
  anchor = W-SUN resample (label-left, closed-left, closure_battery
  pattern); daily anchor daily_df pattern (1D resample of 1h deep).
- Data: BTC deep spot files (15m/1h/4h on disk, PRICE_SCALE=1e6 divided
  at load); daily/weekly resampled from 1h deep; 5m/1m fetched WINDOWED
  -> in-memory aggregates -> raw discarded; only KB-scale per-anchor-candle
  range tables + realized trade lists persist under crt/data_agg/.
- Price source note (declared): standing spot-kline series, same lens as
  the S10 closure matrix; 5m/1m from the same spot endpoints.
- Degenerate exclusion (declared): trigger TF coarser than or equal to the
  anchor TF is not a cell. Anchor-TF close for invalidation reads the
  anchor's own completed-bar close (D1/W1 resample close).
- Sweeps: first valid sweep per side per anchor candle registers; re-arm
  only when flat AND a new valid sweep registers. One position at a time.

## CONTRACT AMENDMENT A1 — GROUND-TRUTH SOURCE REDEFINITION (2026-11-11, user-ratified)

Ratified verbatim scope of A1:
- SOURCE CORPUS = exactly three YouTube channels, entire CRT knowledge
  depends on them: (1) MadoCRT, (2) Romeotpt (https://www.youtube.com/@Romeotpt),
  (3) ShamCRT (https://www.youtube.com/@SpeculatorFL). ORDER: MadoCRT ->
  Romeotpt -> ShamCRT, sequentially, one video at a time. Complete one
  channel fully first; cross-channel references are resolved when their
  channel's turn arrives (user directive 3).
- Corpus boundary (user statement): "all of these channels have only crt
  based long form videos, no shorts or personal content" -> all public
  long-form videos of each channel are in scope.
- Method must treat each source as teacher notes: "each and every video,
  each and every example shown in each video... understand every second";
  re-verifications via full transcript re-reads + direct frame viewing.
- FIDELITY BAR (user, binding): "even the minute detail should not be
  missed even if it lies in sub second part of video". Accepted method:
  literal-global frame coverage via dense sweeps + full transcript +
  targeted re-pulls at example segments; resolution = MAXIMUM the video
  carries ("low res is not fine for reading charts").
- TEST-RUN PROTOCOL (user answer 1 = option (a)): pipeline built + proven
  on video #1 -> timestamped notes delivered -> PAUSE for user review
  before video #2. NO backtesting on an unverified formalization.
- TOOLING (user answer 4): yt-dlp + ffmpeg in system Temp, user-approved,
  deleted after use; workspace storage rule honored (only KB-scale notes
  persist, under crt/notes/<channel>/<videoid>.md + master index; every
  extracted rule numbered/quoted; per-video MODE stamps declared).
- Standing backtest conventions (7bp/side, 3bp/day haircut, absolute
  judge window, four-bar, >=8-trade floor, regime split): UNCHANGED.
- CONSEQUENCES: spec v1.0 draft-set anatomy is DEMOTED from ground truth
  to unverified initial guess. Scope S1 (declared 2026-11-10) is HELD/
  VOIDED pre-compute (0 cells run, 0 cells used) — superseded pending the
  source-grounded spec v1.1. New scopes may be declared only after the
  user reviews the source notes and ratifies the derived rule set.
- Notes custody flag: registry will log one SOURCE-INTEGRATION row per
  processed video: date | channel | video title | ID | duration/frames |
  mode | rule deltas vs v1.0 draft set (for the record only; v1.0 rows
  carry no verdict significance).

## USED / DECLARED SCOPES

### Scope S1 (declared 2026-11-10, spec v1.0, pre-compute) — VOIDED PRE-COMPUTE by Amendment A1

Layer 1 — component probes (premise tests; four-bar + regime split applied).

PA1 "anchor sweep-resolution premise" — 16 cells x 4 combos each
(buffer {0bp,2bp} x penetration {strict, 1bp} = 4). Probe rule body:
B1/B3 sweep of prior-candle anchor level -> next-bar-open entry in
reversal direction; stop = sweep extreme +/- buffer; target = opposite
side of anchor range; T3 time stop at anchor close; structure
invalidation exits. Cells:
- PA1-D1UT x trigger {1m, 5m, 15m, 1h, 4h}.................... 5 cells
- PA1-W1   x trigger {1m, 5m, 15m, 1h, 4h, daily}............. 6 cells
- PA1-D1EST x trigger {1m, 5m, 15m, 1h, 4h}................... 5 cells

PA2 "N-bar rolling-range premise" (fractal component) — 18 cells x
2 combos (buffer {0bp,2bp}). Probe rule: sweep of the completed prior
N-bar [max-high, min-low] -> reversal entry next bar open; stop beyond
the swept side +/- buffer; target = range opposite side fixed at entry;
no time stop (run to stop/target/invalidation). Cells:
- PA2 x trigger {1m, 5m, 15m, 1h, 4h, daily} x N {3, 5, 12}... 18 cells

Layer 2 — composite practitioner bundles.

V1 "classic prior-D1 sweep" (UTC anchor) — 3 cells x 12 combos
(entry {D1, D2, D3} x buffer {0bp, 2bp} x target {T1, T2}; eps strict;
G0). Cells: trigger {5m, 15m, 1h}................................ 3 cells

V1-E "prior-D1-EST sweep" (EST anchor, same rule body) — 3 cells x 12
combos (same grid). Cells: trigger {5m, 15m, 1h}................ 3 cells

V1-KZ "killzone-gated V1 (UTC)" — 6 cells x 6 combos (entry {D1, D2,
D3} x target {T1, T2}; buffer fixed 2bp). Semantics: sweep must occur
with trigger-bar open-time inside the KZ window; entries then follow
normally; no other career filtering. Cells: {London KZ, NY AM KZ} x
trigger {5m, 15m, 1h}........................................... 6 cells

V2 "first-candle open-range" — 4 cells x 8 combos (entry {D1, D3} x
buffer {0bp, 2bp} x target {T1, T2}; eps strict; G0). Anchor = the
first 1h candle of the period (UTC: 00:00-01:00 UTC high/low; EST:
08:00-09:00 ET high/low), valid for the day. Cells: anchor {D1-UTC-1h,
D1-EST-1h} x trigger {5m, 15m}................................. 4 cells

V2-KZ "killzone-gated V2" — 8 cells x 4 combos (entry {D1, D3} x
target {T1, T2}; buffer fixed 2bp). Cells: {UTC, EST anchors} x
trigger {5m, 15m} x {London, NY AM}............................. 8 cells

V3 "HTF prior-candle x LTF trigger" — 5 cells x 8 combos (entry {D1,
D3} x buffer {0bp, 2bp} x target {T1, T2}; eps strict; G0). Cells:
anchor D1-4h-prior x trigger {5m, 15m}; anchor D1-1h-prior x trigger
{1m, 5m, 15m}................................................... 5 cells

V3-KZ "killzone-gated V3" — 10 cells x 4 combos (entry {D1, D3} x
target {T1, T2}; buffer fixed 2bp). Cells: 1h-prior anchor x trigger
{1m, 5m, 15m} x {London, NY AM}; 4h-prior anchor x trigger {5m, 15m}
x {London, NY AM}.............................................. 10 cells

SCOPE S1 TOTALS: 73 cells declared, 352 parameter runs, 0 cells run,
0 verdicts. Compute begins only after the user GO.

### Execution log (Scope S1)

| date | event |
|---|---|
| 2026-11-10 | User GO received. Run 1 launched; killed by an import bug (NameError: sweep_scan) after the 1m fetch phase; raw in-RAM data discarded per the storage rule (52 min fetch cost, honest). |
| 2026-11-11 | Engine hardening: pre-fetch smoke over every anchor family on disk lanes found + fixed (a) lane truncation type bug, (b) ns/us timestamp-precision bug, (c) est_day_ids missing ET-floor (broke d1est AND fc_est anchors), (d) floor("W-SUN") non-fixed-frequency crash -> exact epoch-day W-SUN bucketing, (e) et_floor aware-index guard. Diagnostics (not registry cells, no verdicts): fc_utc 0.958 / fc_est 0.625 valid fractions exactly as designed; forensics 0 mismatches over all sampled fills incl. D2/T2 and KZ paths; full-pipeline smoke (report + aggregates + drop-raw) PASS. |
| 2026-11-11 | Run 2 launched (re-fetch 1m/5m windowed in-RAM, then all 73 cells / 352 lines). |
| 2026-11-11 | Run 2 killed mid-1m-fetch: both endpoints failed all 6 quick retries at the 2023-10-06 window (network outage beyond retry budget). Raw in-RAM data discarded per storage rule (~15 min honest loss). Fix: fetch retry hardened to 8 attempts, exponential backoff 1s->90s (~6.5 min stall tolerance per window, alternating mirrors, logged). |
| 2026-11-11 | Run 3 killed mid-1m-fetch at the 2025-03-05 window despite full backoff (8 attempts, ~13 min of retry, both endpoints). ~21 min of fetch work lost under the strict in-RAM rule. |
| 2026-11-11 | **USER AMENDMENT (charter §7 conflict surface, user instruction: "make any scripts resumable if such network error happens")**: sub-hour raw fetch progress MAY be checkpointed to disk so network errors no longer destroy whole fetches. Scope of the amendment: checkpoint arrays only under crt/cache_raw/*.npz (ts + OHLC, uncompressed npz), working-data only, flushed every ~100k rows (~2-2.5 min of fetch), DELETED immediately after a successful full S1 battery; KB-scale aggregates remain the only standing persistent outputs; no GB-scale data ever remains on disk; checkpoint never feeds any verdict (it is raw source data passing the same windowed pattern). |
| 2026-11-11 | Run 4 launched with resumable fetch (same scope/semantics; fetch-side only). |

STATUS: RUN 4 IN PROGRESS.
