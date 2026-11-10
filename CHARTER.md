# CRT TRACK CHARTER — handoff document for the dedicated CRT chat

Written by the MAIN crypto-quant desk session (Nov 10, 2026, Session 10.6.2).
READ THIS ENTIRE FILE BEFORE DOING ANYTHING. This is your memory, not a
suggestion. Your job: deep, honest, iterative evaluation of the CRT
framework per the user's contract — as a CONTINUATION of this desk, not a
new start. The user chose "Echo, no quiz": you must read + echo back, and
may then proceed; but wrong facts = wrong verdicts, so the reading list
below is mandatory in full.

## 0. WHO THE DESK IS (read JOURNAL.md tails before trusting any number)

The workspace root is the parent of crypto-quant/. Everything lives under
crypto-quant/. This desk builds automated crypto trading strategies for
REAL INCOME (eventually) with a $100 pilot starting capital that remains
UNTOUCHED through every session to date (paper/testing only; no live
account exists anywhere). Discipline: pre-registered gates verbatim BEFORE
any compute; one simulation pass per pre-registered cell; realized-only
verdicts; mandatory regime splits; honest expectations; failures are
stamped, never buried. The desk's ONLY certified live edge is funding
carry (H09): gated rule net +23.81 per $100 notional (+4.77%/yr), stream
MDD -$0.31, 2 trips, full-span 5y basis-truth gauntlet; always-in
comparator +34.08 (+6.82%/yr). Per-capital correction: at 1x USDT-M,
per-capital yield ~ HALF the per-notional figures (COIN-M doubles it).

Evidence anchors you inherit (do not re-test these; build on them):
- S10 CLOSURE MATRIX: 5 dead price families x {15m,1h,4h,weekly} x
  {bull,sideways,bear} = 18 cells, ALL dead; cost x cadence law empirical
  (nets worsen monotonically toward faster bars; 15m cells lost up to
  ~3x account/yr on $100 notional; weekly cells statistically EMPTY).
- P1/E3 rotation: gated rotation +3.80%/yr book FAILED its own
  complexity-value gate; static gated funding blend stays the deliverable.
- P2 pairs: 22/45 pairs pass in-sample ADF screens (illusion), frozen
  winners pooled -64.99%/yr gross OOS; z-STOP exits dominate (spreads
  BREAK, they do not revert at 1h cadence).
- Dead families on record: H01/H02b/H03/H04/H05 (all TFs + regimes),
  H06 maker-bolt-ons (banned as rescue path), H07 marginal, H08 class-kill,
  RSPEED transfer-fail. USDT-M 10-coin universe = the standing data set.

## 1. READ-FIRST MAP (in this order)

1. crypto-quant/JOURNAL.md — TAIL SECTIONS ONLY, in this order:
   "SESSION 10.6.2 - P3 PROGRAM PRE-REGISTRATION PART 1" (your contract),
   "SESSION 10.6.1" (P2 pairs results + why stat-arb died),
   "RESULTS - Session 10" (the closure matrix + cost x cadence law),
   "Session 9" / H09 certification blocks (the income floor),
   "PRE-REGISTRATIONS / STANDING RULES" (fundings, folds, settlements,
   accounting conventions - pre-registered verbatim at S6/S9; do not
   re-invent them, inherit them).
2. crypto-quant/README.md — status ledger + hypothesis rows (parked /
   closed / certified statuses).
3. crypto-quant/out/STRATEGY_CATALOG.md — the 36-family map + P-queue.
4. crypto-quant/out/P2_pairs_report.md, out/E3_rotation_report.md,
   out/closure_matrix_report.md — recent verdict dossiers (engine style).
5. Engine patterns you MAY import (read-only): crypto-quant/p2_pairs.py
   (custom perp-perp state machine + EG screen + regime map),
   crypto-quant/closure_battery.py (TF matrix lens + per-trade haircut),
   crypto-quant/audit.py + data.py (loaders: A.load(sym,"1h","_deep"),
   A.daily_df), crypto-quant/config.py (CASH=100, fee constants,
   PRICE_SCALE=1e6 in the deep CSV price columns; Date index = open time).

## 2. YOUR CRT CONTRACT (user-ratified Nov 10 — binding, verbatim)

1. BOTH LAYERS: every mechanical component tested in isolation AND the
   complete composite bundle as practitioners trade it. Attribution
   duality: no component may be falsely closed by its bundle, and no
   bundle may claim an edge its components lack.
2. FULL SUB-HOUR FROM START: cadence lanes 1m / 5m / 15m / 1h / 4h /
   daily ALL open in the first pass. Sub-hour data comes ONLY through
   the stream-aggregate-discard pattern (fetch window -> in-memory
   session aggregates -> raw discarded; ONLY KB-scale artifacts persist).
3. YOU BUILD YOUR OWN STREAMING ENGINE (user-delegated isolation; the
   main desk does not hand you one). Keep its code under crypto-quant/crt/.
4. BOTH SESSION ANCHORS as separate pre-registered variants and reported
   separately: UTC (data-native) and EST-with-DST (practitioner clock).
   A timing edge hiding in a local-session window gets no guess-death.
5. UNLIMITED review-cycle revisions per the review outcomes — ALL under
   the new-scope-only rule: a revision is a FRESH pre-registration ADDING
   new testable scope (deeper components, new tolerance anchors, new
   variant families). Re-running any dead cell of a used scope is banned
   forever. The registry (crt/REGISTRY.md) logs every used scope to
   enforce this.
6. CLOSURE RULE: DEAD ONLY IF ALL DIES. The CRT file closes ONLY if every
   component dies at every cadence/anchor AND every composite dies
   through all revision rounds. ANY survivor anywhere keeps CRT OPEN as a
   flagged candidate (flag -> possible fresh pre-registered line; never a
   verdict overturn).
7. THREE FIXED USER CHECKPOINTS (you are co-piloted; the user wants to
   be IN this loop):
   CP1 - formalization dossier review: before any battery compute;
   CP2 - after every battery readout: user sees results before any
         revision is proposed; and
   CP3 - before each revision round: you present the new scope and the
         user ratifies it before compute.
8. Four-bar standard per verdict (per $100 NOTIONAL; per-capital = /2
   USDT-M 1x): A net > 0; B >= +4.77%/yr; C >= +6.82%/yr; D >= +20%/yr
   (double-digit per capital). Report every line per-bar against all four.
9. BTC primary; ETH cross-check row ONLY if a BTC candidate survives.
   ETH 15m/1h deep data already on disk if needed.
10. RECORDING: own-files-only. You create and maintain files ONLY under
   crypto-quant/crt/: CHARTER.md (this file), REGISTRY.md (scope
   registry + revision log), battery reports (crt/battery_*.md), engines
   (crt/*.py), streamed aggregates (crt/data_agg/*.csv, KB-scale).
   DO NOT edit any main-desk file (JOURNAL.md, README.md, catalog,
   engine scripts). The MAIN desk holds a pointer row for you in its
   ledger; when your verdicts land, TELL THE USER to relay them to the
   main desk chat for a port summary — do not write them yourself.

## 3. STANDING NUMBERS & CONVENTIONS (inherit; never drift)

- Costs: 7bp/side taker on every fill both legs; maker-passive execution
  ONLY where the signal is structurally limit-order-native (H06 rule:
  maker bolt-ons cannot be used to rescue a taker verdict).
- Haircut: 3bp/day per $1 of held notional (day-in-market).
- Judge protocol: train [data start -> 2025-11-05), judge [2025-11-05 ->
  data end (~2026-11-09)], ABSOLUTE anchor (S6 precedent). Trades labeled
  by ENTRY timestamp; in-window entries only; realized-only verdicts
  (open-at-cutoff positions unbooked).
- Parameter grids <= 16 combos per spec version per cell; frozen
  train-picks judged OOS; neighbors informational (reported, never
  verdict-bearing); judge trade floor = 8 closed trades minimum (2-trip
  verdicts are statistically sterile - H07 lesson).
- Funding conventions: carry engine - entry at print i accrues i+1
  through exit j-1 (exit print dropped); perp-perp structures - signed
  net accrual per print while held with the exit-bar print INCLUDED
  (bar close settles after the 8h print). Funding data:
  crypto-quant/data/funding_breadth/usdt_*.csv (10 coins x 5y, 5,490
  prints each, printed Nov 10).
- Regime split (mandatory per verdict): each month classified by BTC's
  trailing-30d return at month end: >= +10% bull, <= -10% bear, else
  sideways. Working code pattern: regime_map() in p2_pairs.py — pandas
  3.x: freq "ME" (not "M"); PeriodIndex .astype(np.int64).
- Data quirks: deep CSV price columns are scaled (PRICE_SCALE=1e6 in
  config.py — read it); the 1h loader pattern is A.load(sym, "1h",
  "_deep"); BTC 15m/1h deep files span 2021-11 -> 2026-11-09 (~44k/175k
  bars; ETH same). If you fetch 5m/1m history, fetch it WINDOWED and
  aggregate immediately (storage rule; the PC is storage-poor).
- Expectation language: pre-declare expectations ONLY where evidence
  exists. The S10 closure covers PRICE-GEOMETRY cores (candle patterns,
  sweeps, breakouts, MA systems at 7bp taker) — a strong prior of death
  that you must still test cleanly rather than collapse into assumption.
  The NOVEL layers (anchor-range fractals, session-timing variants,
  composite confluence statistics) have NO evidence either way yet — no
  expectation is committed for them. That boundary is the discipline.

## 4. CRT ANATOMY INVENTORY (draft v0.5 — your first work item is refining
this into the formalization dossier for CP1)

Mechanical components practitioners trade, each needing an explicit
rule definition before compute:
1. Anchor-range construction: the "candle" whose high/low define the
   range. Variants: prior candle of anchor TF {D1, W1, M1}; the FIRST
   candle of a period (00:00 UTC daily open candle); N-bar intraday
   range at the trigger TF. Anchor TF lane: {1h, 4h, D1, W1}.
2. Sweep/liquidity-grab detection: price TRADING THROUGH the anchor
   high/low then closing back inside. Tolerance axis: wick-through
   (strict) vs epsilon-through (declared tick tolerance) vs close-
   through-invalid (a CLOSE beyond the level voids the setup).
3. Displacement/confirmation layer (optional per variant): opposite
   break of structure with a body/velocity threshold after the sweep.
4. Entry pattern: (a) immediate re-cross of the swept level; (b) retrace
   to the swept candle's 50%; (c) break of the sweep candle's near side;
   (d) confirmation-then-entry variants. Stop: the sweep extreme
   (+declared buffer). 
5. Targets: opposite side of the anchor range (full) / range midpoint
   (partial book variants); structure invalidation: anchor-TF close
   beyond the level = setup voided (position management rule).
6. Session/timing filters: killzones as an OPTIONAL signal layer;
   UTC vs EST-DST anchor variants (both pre-registered).
7. Composite bundle: full practitioner form = anchor range at HTF ->
   sweep detection at LTF via anchor's H/L -> entry variant -> target/
   invalidation management. Trigger TF lane: {5m, 15m, 1h} per the
   full-sub-hour contract.
8. Cadence x anchor matrix: components at each of their lanes;
   composites across {trigger TF} x {anchor TF} x {session anchor};
   <= 16 combos per spec version per cell; report ALL cells.
Unknowns to resolve at CP1: the user names the practitioner variant/line
they want as ground truth (or ratifies the public-definition draft set
above as the tested definition). THIS IS THE SINGLE MOST IMPORTANT CP1
OUTPUT — formalization IS the hypothesis.

## 5. YOUR WAKE RITUAL (first message you ever send in the CRT chat)

1. Verify context: open crypto-quant/JOURNAL.md from the workspace. If
   the file does not exist in your working directory, HALT and tell the
   user plainly: wrong folder — continuity is broken.
2. Read: this charter fully; the JOURNAL tail sections listed in
   section 1; README.md; STRATEGY_CATALOG.md; the three verdict reports.
3. ECHO BACK (no quiz, but be right): a compact state summary — (a) desk
   purpose + $100 untouched + venue rule; (b) the certified floor numbers
   (H09); (c) the three evidence anchors in one line each; (d) your CRT
   contract's six binding items; (e) what is newly opened vs inherited-
   dead for CRT specifically; (f) proposed plan to CP1.
4. Rename your session title early (session tooling) so both chats are
   recognizable in history: e.g., "CRT track".
5. THEN produce the formalization dossier v1.0 inline (no new battery
   code yet) and ask the user: which variant/source is ground truth, and
   corrections to the anatomy inventory. That is checkpoint CP1. No
   battery compute before CP1 is resolved.

## 6. REGISTRY FORMAT (crt/REGISTRY.md — create at first use)

Columns: date | spec version | scope cells declared | cells run |
verdict per cell | survival flags | revision reason codes (if any).
Rules: a scope is declared BEFORE compute with its full cell list; no
cell list may overlap a USED scope's cells (the registry audit does this
lookup every pre-registration); unlimited revisions permitted; every
dead cell is stamped with its autopsy line (premise death vs cost death).

## 7. FAILSAFES

- Missing files -> report and stop; never improvise out-of-charter.
- Compute budget: heavy is fine; storage is NOT — any sub-hour fetch
  must be windowed and aggregated in memory; persist aggregates only.
- If the user asks for something conflicting with this charter, stop and
  surface the conflict (the charter is the ratified contract; changing
  it is a user decision recorded in YOUR registry).
- The main desk's failure taxonomy you must respect and cite: premise
  death (logic falsified OOS), cost death (edge < costs after all
  accounting), stat-sterile (trade floor unmet), regime-locked survival
  (positive bucket exists — flag, never bury).
- Money: NO live-money work of any kind. Everything you do is paper.
  The $100 has never moved; do not propose to move it.

— end of charter —
