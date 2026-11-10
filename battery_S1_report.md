# CRT BATTERY S1 REPORT (Scope S1, spec v1.0)

Pre-registered 2026-11-10 in crt/REGISTRY.md; judge = [2025-11-05 ->
data end], ABSOLUTE anchor (S6/S10 precedent). One simulation pass per
combo; all lines reported; no train-selected pick biases anything.

**Conventions (registry spec v1.0, verbatim):**
- Unit per $100 NOTIONAL per position, BTC primary (ETH cross-check only
  on a survivor -> later scope). Per-capital = /2 (1x USDT-M).
- 7bp/side taker per fill (entry fee share proportional per portion);
  3bp/day haircut per $1 held per portion; no funding credit (S10).
- MDD = trade-exit-stream NAV ($; monitor, not a bar). PF on NET.
- Trade rows are PORTION records; T2 midpoint-split trips appear as two
  rows; floor = >= 8 closed JUDGE rows.
- Bars: A net>0 | B >= +4.77%/yr | C >= +6.82%/yr | D >= +20%/yr notional
  (D = double-digit per capital at 1x).
- Execution: mkt fills next trigger-bar open; limit fills at sweep-bar
  midpoint; stop fills at sweep-bar near side; gap-through fills at bar
  open; STOP-first under same-bar conflicts; sweep precedence 'hi' then
  'lo'; careers ignored while a position/pend is alive; pendings cancel
  at window end (unfilled = no fee); KZ cells require the sweep confirm
  bar's open-time inside the window (ET clock, DST-native).
- Anchors: T3/monitoring window = the CURRENT anchor-TF candle; A1 anchor
  levels from the PRIOR candle; first-candle anchors valid from candle
  close; PA2 rolling prior-N trigger-bar range has no void and no time
  stop (declared); structure invalidation fires with the anchor-TF close
  (reason labeled void vs t3).

**Judge span:** enabled 73 cells / 352 lines; span 364.667 days; data end 2026-11-04 16:00:00


### PA1-D1UT x 1m

(prior UTC D1 candle | trigger 1m | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### PA1-D1UT x 5m

(prior UTC D1 candle | trigger 5m | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### PA1-D1UT x 15m

(prior UTC D1 candle | trigger 15m | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -24.56 | -99.99 | -24.60 | +0.61 | 177 / 765 | -29.24 | -1.56 / -18.11 / -4.90 / -99.99 | stop=141,t1=15,t3=21 | F F F F | OK | open=0 | COST-DEATH |
| D1-e1bp-b0bp-tT1 | -26.99 | -100.23 | -27.03 | +0.56 | 167 / 730 | -31.66 | -2.57 / -17.39 / -7.03 / -100.23 | stop=134,t1=13,t3=20 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT1 | -26.97 | -100.61 | -27.01 | +0.59 | 175 / 749 | -31.20 | -2.08 / -19.24 / -5.65 / -100.61 | stop=139,t1=15,t3=21 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-e1bp-b2bp-tT1 | -29.46 | -100.43 | -29.51 | +0.54 | 166 / 715 | -33.70 | -3.09 / -18.60 / -7.77 / -100.43 | stop=133,t1=13,t3=20 | F F F F | OK | open=0 | PREMISE-DEATH |

### PA1-D1UT x 1h

(prior UTC D1 candle | trigger 1h | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -15.89 | -55.77 | -15.92 | +0.79 | 186 / 833 | -27.31 | -0.10 / -20.96 / +5.17 / -55.77 | stop=130,t1=26,t3=29,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +5.17] |
| D1-e1bp-b0bp-tT1 | -17.22 | -57.06 | -17.24 | +0.77 | 177 / 810 | -28.92 | -0.90 / -20.61 / +4.30 / -57.06 | stop=124,t1=24,t3=28,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +4.30] |
| D1-b2bp-tT1 | -18.49 | -58.38 | -18.52 | +0.76 | 186 / 822 | -29.33 | -0.54 / -22.45 / +4.49 / -58.38 | stop=130,t1=26,t3=29,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +4.49] |
| D1-e1bp-b2bp-tT1 | -19.70 | -59.31 | -19.73 | +0.74 | 177 / 799 | -30.84 | -1.32 / -22.01 / +3.64 / -59.31 | stop=124,t1=24,t3=28,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +3.64] |

### PA1-D1UT x 4h

(prior UTC D1 candle | trigger 4h | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -19.94 | -83.24 | -19.97 | +0.77 | 182 / 773 | -37.53 | +0.79 / -23.50 / +2.77 / -83.24 | stop=102,t1=33,t3=42,void=5 | F F F F | OK | open=0 | COST-DEATH | FLAG[bull +0.79; bear +2.77] |
| D1-e1bp-b0bp-tT1 | -19.91 | -83.77 | -19.94 | +0.77 | 175 / 761 | -38.19 | -0.12 / -22.58 / +2.80 / -83.77 | stop=98,t1=31,t3=41,void=5 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +2.80] |
| D1-b2bp-tT1 | -21.98 | -87.94 | -22.01 | +0.76 | 182 / 771 | -39.18 | +0.49 / -24.70 / +2.23 / -87.94 | stop=102,t1=33,t3=42,void=5 | F F F F | OK | open=0 | COST-DEATH | FLAG[bull +0.49; bear +2.23] |
| D1-e1bp-b2bp-tT1 | -21.87 | -88.33 | -21.91 | +0.75 | 175 / 759 | -39.79 | -0.42 / -23.72 / +2.28 / -88.33 | stop=98,t1=31,t3=41,void=5 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +2.28] |

### PA1-W1 x 1m

(prior W1 candle (W-SUN) | trigger 1m | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### PA1-W1 x 5m

(prior W1 candle (W-SUN) | trigger 5m | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### PA1-W1 x 15m

(prior W1 candle (W-SUN) | trigger 15m | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -4.58 | +3.29 | -4.59 | +0.73 | 30 / 106 | -7.43 | -1.70 / +0.49 / -3.37 / +3.29 | stop=25,t3=5 | F F F F | OK | open=0 | COST-DEATH | FLAG[side +0.49] |
| D1-e1bp-b0bp-tT1 | -4.58 | +3.98 | -4.59 | +0.73 | 30 / 105 | -7.43 | -1.70 / +0.49 / -3.37 / +3.98 | stop=25,t3=5 | F F F F | OK | open=0 | COST-DEATH | FLAG[side +0.49] |
| D1-b2bp-tT1 | -6.59 | +7.07 | -6.60 | +0.66 | 32 / 104 | -8.26 | -2.37 / -0.76 / -3.45 / +7.07 | stop=27,t3=5 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-e1bp-b2bp-tT1 | -6.59 | +7.78 | -6.60 | +0.66 | 32 / 103 | -8.26 | -2.37 / -0.76 / -3.45 / +7.78 | stop=27,t3=5 | F F F F | OK | open=0 | PREMISE-DEATH |

### PA1-W1 x 1h

(prior W1 candle (W-SUN) | trigger 1h | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -0.63 | -23.58 | -0.63 | +0.98 | 35 / 122 | -14.35 | +1.25 / +7.30 / -9.17 / -23.58 | stop=27,t1=1,t3=7 | F F F F | OK | open=0 | COST-DEATH | FLAG[bull +1.25; side +7.30] |
| D1-e1bp-b0bp-tT1 | -0.63 | -23.00 | -0.63 | +0.98 | 35 / 121 | -14.35 | +1.25 / +7.30 / -9.17 / -23.00 | stop=27,t1=1,t3=7 | F F F F | OK | open=0 | COST-DEATH | FLAG[bull +1.25; side +7.30] |
| D1-b2bp-tT1 | -1.17 | -24.45 | -1.17 | +0.96 | 35 / 120 | -14.71 | +1.19 / +6.98 / -9.33 / -24.45 | stop=27,t1=1,t3=7 | F F F F | OK | open=0 | COST-DEATH | FLAG[bull +1.19; side +6.98] |
| D1-e1bp-b2bp-tT1 | -1.17 | -23.85 | -1.17 | +0.96 | 35 / 119 | -14.71 | +1.19 / +6.98 / -9.33 / -23.85 | stop=27,t1=1,t3=7 | F F F F | OK | open=0 | COST-DEATH | FLAG[bull +1.19; side +6.98] |

### PA1-W1 x 4h

(prior W1 candle (W-SUN) | trigger 4h | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -1.43 | -17.98 | -1.43 | +0.96 | 38 / 113 | -16.07 | +0.40 / +7.78 / -9.61 / -17.98 | stop=27,t1=2,t3=9 | F F F F | OK | open=1 | COST-DEATH | FLAG[bull +0.40; side +7.78] |
| D1-e1bp-b0bp-tT1 | -1.43 | -17.98 | -1.43 | +0.96 | 38 / 113 | -16.07 | +0.40 / +7.78 / -9.61 / -17.98 | stop=27,t1=2,t3=9 | F F F F | OK | open=1 | COST-DEATH | FLAG[bull +0.40; side +7.78] |
| D1-b2bp-tT1 | -1.97 | -15.40 | -1.97 | +0.94 | 38 / 111 | -16.35 | +0.34 / +7.44 / -9.75 / -15.40 | stop=27,t1=2,t3=9 | F F F F | OK | open=1 | COST-DEATH | FLAG[bull +0.34; side +7.44] |
| D1-e1bp-b2bp-tT1 | -1.97 | -15.40 | -1.97 | +0.94 | 38 / 111 | -16.35 | +0.34 / +7.44 / -9.75 / -15.40 | stop=27,t1=2,t3=9 | F F F F | OK | open=1 | COST-DEATH | FLAG[bull +0.34; side +7.44] |

### PA1-W1 x daily

(prior W1 candle (W-SUN) | trigger daily | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -3.71 | -24.21 | -3.71 | +0.89 | 28 / 107 | -17.60 | -7.50 / +21.01 / -17.22 / -24.21 | stop=15,t1=2,t3=10,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[side +21.01] |
| D1-e1bp-b0bp-tT1 | -3.71 | -24.21 | -3.71 | +0.89 | 28 / 107 | -17.60 | -7.50 / +21.01 / -17.22 / -24.21 | stop=15,t1=2,t3=10,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[side +21.01] |
| D1-b2bp-tT1 | -4.00 | -20.52 | -4.01 | +0.89 | 28 / 106 | -17.78 | -7.56 / +20.91 / -17.36 / -20.52 | stop=15,t1=2,t3=10,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[side +20.91] |
| D1-e1bp-b2bp-tT1 | -4.00 | -20.52 | -4.01 | +0.89 | 28 / 106 | -17.78 | -7.56 / +20.91 / -17.36 / -20.52 | stop=15,t1=2,t3=10,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[side +20.91] |

### PA1-D1EST x 1m

(prior EST(DST) D1 candle | trigger 1m | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### PA1-D1EST x 5m

(prior EST(DST) D1 candle | trigger 5m | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-e1bp-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### PA1-D1EST x 15m

(prior EST(DST) D1 candle | trigger 15m | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -24.28 | -158.08 | -24.31 | +0.64 | 196 / 828 | -33.14 | -3.25 / -15.00 / -6.02 / -158.08 | stop=156,t1=14,t3=26 | F F F F | OK | open=0 | COST-DEATH |
| D1-e1bp-b0bp-tT1 | -22.99 | -152.85 | -23.02 | +0.64 | 185 / 792 | -32.09 | -3.95 / -13.22 / -5.82 / -152.85 | stop=146,t1=13,t3=26 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT1 | -26.35 | -161.51 | -26.39 | +0.62 | 192 / 809 | -34.78 | -3.56 / -16.03 / -6.76 / -161.51 | stop=152,t1=14,t3=26 | F F F F | OK | open=0 | COST-DEATH |
| D1-e1bp-b2bp-tT1 | -25.04 | -156.03 | -25.08 | +0.63 | 182 / 775 | -33.72 | -4.39 / -14.11 / -6.54 / -156.03 | stop=143,t1=13,t3=26 | F F F F | OK | open=0 | COST-DEATH |

### PA1-D1EST x 1h

(prior EST(DST) D1 candle | trigger 1h | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -28.50 | -118.76 | -28.55 | +0.65 | 193 / 861 | -37.32 | -6.02 / -16.24 / -6.24 / -118.76 | stop=133,t1=17,t3=42,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-e1bp-b0bp-tT1 | -27.83 | -115.90 | -27.88 | +0.65 | 187 / 837 | -36.65 | -7.03 / -15.21 / -5.59 / -115.90 | stop=128,t1=16,t3=42,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT1 | -31.16 | -122.23 | -31.21 | +0.63 | 193 / 854 | -39.68 | -6.42 / -17.86 / -6.87 / -122.23 | stop=133,t1=17,t3=42,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-e1bp-b2bp-tT1 | -30.40 | -118.99 | -30.44 | +0.63 | 187 / 830 | -38.91 | -7.43 / -16.75 / -6.21 / -118.99 | stop=128,t1=16,t3=42,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |

### PA1-D1EST x 4h

(prior EST(DST) D1 candle | trigger 4h | 4 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -27.57 | -91.84 | -27.62 | +0.68 | 179 / 788 | -41.56 | -5.42 / -15.13 / -7.03 / -91.84 | stop=94,t1=25,t3=57,void=3 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-e1bp-b0bp-tT1 | -26.91 | -91.21 | -26.95 | +0.68 | 174 / 778 | -41.13 | -6.33 / -14.19 / -6.39 / -91.21 | stop=90,t1=24,t3=57,void=3 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT1 | -29.45 | -92.59 | -29.50 | +0.66 | 179 / 784 | -43.10 | -5.74 / -16.17 / -7.54 / -92.59 | stop=94,t1=25,t3=57,void=3 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-e1bp-b2bp-tT1 | -28.71 | -91.86 | -28.75 | +0.67 | 174 / 774 | -42.61 | -6.65 / -15.17 / -6.88 / -91.86 | stop=90,t1=24,t3=57,void=3 | F F F F | OK | open=0 | PREMISE-DEATH |

### PA2-N3 x 1m

(rolling prior-3 trigger bars | trigger 1m | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -8840.74 | -40389.87 | -8854.88 | +0.05 | 64739 / 292741 | -8840.74 | -1352.25 / -4438.07 / -3050.42 / -40389.87 | stop=37897,t1=26842 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT1 | -7423.52 | -32994.69 | -7435.39 | +0.06 | 53960 / 237871 | -7423.52 | -1132.38 / -3713.64 / -2577.49 / -32994.69 | stop=27753,t1=26207 | F F F F | OK | open=0 | COST-DEATH |

### PA2-N5 x 1m

(rolling prior-5 trigger bars | trigger 1m | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -6800.63 | -30879.85 | -6811.51 | +0.08 | 50576 / 227134 | -6800.66 | -1060.55 / -3423.36 / -2316.72 / -30879.85 | stop=33575,t1=17001 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT1 | -5576.29 | -24759.42 | -5585.21 | +0.11 | 41269 / 181203 | -5576.31 | -863.77 / -2797.55 / -1914.98 / -24759.42 | stop=24590,t1=16679 | F F F F | OK | open=0 | COST-DEATH |

### PA2-N12 x 1m

(rolling prior-12 trigger bars | trigger 1m | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -4242.36 | -18851.84 | -4249.15 | +0.16 | 31853 / 139977 | -4242.40 | -662.79 / -2127.75 / -1451.83 / -18851.84 | stop=24529,t1=7324 | F F F F | OK | open=1 | COST-DEATH |
| D1-b2bp-tT1 | -3420.39 | -14849.31 | -3425.86 | +0.20 | 25436 / 109705 | -3420.43 | -520.05 / -1714.11 / -1186.23 / -14849.31 | stop=18192,t1=7244 | F F F F | OK | open=1 | COST-DEATH |

### PA2-N3 x 5m

(rolling prior-3 trigger bars | trigger 5m | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -2472.57 | -9600.22 | -2476.53 | +0.18 | 17717 / 70357 | -2472.57 | -381.25 / -1315.57 / -775.75 / -9600.22 | stop=11109,t1=6608 | F F F F | OK | open=1 | COST-DEATH |
| D1-b2bp-tT1 | -2157.02 | -8416.28 | -2160.47 | +0.20 | 15346 / 61483 | -2157.02 | -327.59 / -1130.06 / -699.37 / -8416.28 | stop=8969,t1=6377 | F F F F | OK | open=1 | PREMISE-DEATH |

### PA2-N5 x 5m

(rolling prior-5 trigger bars | trigger 5m | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -1816.88 | -7038.53 | -1819.78 | +0.25 | 13172 / 52587 | -1816.99 | -280.92 / -982.83 / -553.12 / -7038.53 | stop=9193,t1=3979 | F F F F | OK | open=1 | COST-DEATH |
| D1-b2bp-tT1 | -1570.47 | -6117.80 | -1572.98 | +0.29 | 11306 / 45526 | -1570.55 | -244.75 / -837.40 / -488.32 / -6117.80 | stop=7444,t1=3862 | F F F F | OK | open=1 | COST-DEATH |

### PA2-N12 x 5m

(rolling prior-12 trigger bars | trigger 5m | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -1012.42 | -3871.53 | -1014.04 | +0.38 | 7547 / 29257 | -1012.92 | -166.50 / -539.90 / -306.03 / -3871.53 | stop=5901,t1=1646 | F F F F | OK | open=1 | COST-DEATH |
| D1-b2bp-tT1 | -879.05 | -3382.04 | -880.46 | +0.41 | 6450 / 25449 | -879.75 | -143.46 / -455.26 / -280.33 / -3382.04 | stop=4850,t1=1600 | F F F F | OK | open=1 | COST-DEATH |

### PA2-N3 x 15m

(rolling prior-3 trigger bars | trigger 15m | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -830.53 | -3434.59 | -831.86 | +0.35 | 5868 / 23737 | -831.77 | -138.79 / -430.14 / -261.61 / -3434.59 | stop=3731,t1=2137 | F F F F | OK | open=1 | PREMISE-DEATH |
| D1-b2bp-tT1 | -765.71 | -3187.67 | -766.94 | +0.38 | 5331 / 21791 | -766.95 | -122.74 / -387.42 / -255.55 / -3187.67 | stop=3258,t1=2073 | F F F F | OK | open=1 | PREMISE-DEATH |

### PA2-N5 x 15m

(rolling prior-5 trigger bars | trigger 15m | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -610.52 | -2503.46 | -611.49 | +0.44 | 4351 / 17354 | -611.37 | -93.64 / -306.50 / -210.37 / -2503.46 | stop=3062,t1=1289 | F F F F | OK | open=1 | COST-DEATH |
| D1-b2bp-tT1 | -578.17 | -2317.56 | -579.09 | +0.45 | 3969 / 15829 | -579.04 | -81.52 / -286.39 / -210.25 / -2317.56 | stop=2722,t1=1247 | F F F F | OK | open=1 | PREMISE-DEATH |

### PA2-N12 x 15m

(rolling prior-12 trigger bars | trigger 15m | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -350.68 | -1416.57 | -351.24 | +0.55 | 2498 / 10029 | -351.53 | -49.20 / -160.18 / -141.30 / -1416.57 | stop=1948,t1=550 | F F F F | OK | open=1 | COST-DEATH |
| D1-b2bp-tT1 | -341.17 | -1342.83 | -341.71 | +0.56 | 2313 / 9294 | -342.38 | -45.14 / -152.82 / -143.21 / -1342.83 | stop=1782,t1=531 | F F F F | OK | open=1 | PREMISE-DEATH |

### PA2-N3 x 1h

(rolling prior-3 trigger bars | trigger 1h | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -249.79 | -844.90 | -250.19 | +0.52 | 1408 / 5590 | -251.26 | -45.41 / -99.96 / -104.42 / -844.90 | stop=930,t1=478 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT1 | -252.44 | -853.76 | -252.84 | +0.52 | 1358 / 5449 | -253.89 | -43.65 / -103.23 / -105.55 / -853.76 | stop=889,t1=469 | F F F F | OK | open=0 | PREMISE-DEATH |

### PA2-N5 x 1h

(rolling prior-5 trigger bars | trigger 1h | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -154.04 | -691.34 | -154.29 | +0.66 | 1112 / 4235 | -154.89 | -37.66 / -65.43 / -50.95 / -691.34 | stop=774,t1=338 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT1 | -153.86 | -694.45 | -154.11 | +0.66 | 1068 / 4116 | -156.38 | -33.78 / -68.64 / -51.44 / -694.45 | stop=735,t1=333 | F F F F | OK | open=0 | COST-DEATH |

### PA2-N12 x 1h

(rolling prior-12 trigger bars | trigger 1h | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -69.44 | -464.34 | -69.55 | +0.80 | 724 / 2711 | -71.40 | -5.50 / -37.71 / -26.23 / -464.34 | stop=557,t1=167 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT1 | -74.57 | -462.84 | -74.69 | +0.79 | 708 / 2636 | -76.29 | -5.82 / -40.35 / -28.39 / -462.84 | stop=541,t1=167 | F F F F | OK | open=0 | COST-DEATH |

### PA2-N3 x 4h

(rolling prior-3 trigger bars | trigger 4h | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -52.23 | -296.79 | -52.31 | +0.77 | 370 / 1558 | -80.69 | -7.59 / -27.77 / -16.87 / -296.79 | stop=232,t1=138 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT1 | -54.63 | -292.43 | -54.72 | +0.77 | 369 / 1538 | -81.66 | -8.38 / -30.31 / -15.94 / -292.43 | stop=231,t1=138 | F F F F | OK | open=0 | COST-DEATH |

### PA2-N5 x 4h

(rolling prior-5 trigger bars | trigger 4h | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -20.58 | -185.28 | -20.61 | +0.90 | 300 / 1167 | -69.78 | -13.00 / -14.08 / +6.50 / -185.28 | stop=201,t1=99 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +6.50] |
| D1-b2bp-tT1 | -16.33 | -164.59 | -16.35 | +0.92 | 296 / 1146 | -64.17 | -5.53 / -16.20 / +5.40 / -164.59 | stop=196,t1=100 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +5.40] |

### PA2-N12 x 4h

(rolling prior-12 trigger bars | trigger 4h | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **D1-b0bp-tT1** | **+6.09** | -202.96 | +6.10 | +1.05 | 138 / 762 | -43.41 | +2.59 / +4.22 / -0.71 / -202.96 | stop=103,t1=35 | P P F F | OK | open=0 | ALIVE | FLAG[bull +2.59; side +4.22] |
| **D1-b2bp-tT1** | **+7.43** | -190.90 | +7.45 | +1.06 | 134 / 751 | -41.27 | +3.61 / +5.24 / -1.42 / -190.90 | stop=99,t1=35 | P P P F | OK | open=0 | ALIVE | FLAG[bull +3.61; side +5.24] |

**2 line(s) in this cell cleared bar A with the floor -> SURVIVAL FLAG (contract: CRT stays OPEN).**

### PA2-N3 x daily

(rolling prior-3 trigger bars | trigger daily | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -18.18 | -202.67 | -18.21 | +0.77 | 58 / 295 | -21.36 | +4.73 / -14.58 / -8.33 / -202.67 | stop=35,t1=23 | F F F F | OK | open=0 | PREMISE-DEATH | FLAG[bull +4.73] |
| D1-b2bp-tT1 | -18.88 | -181.61 | -18.91 | +0.76 | 58 / 290 | -21.78 | +4.65 / -14.96 / -8.56 / -181.61 | stop=35,t1=23 | F F F F | OK | open=0 | PREMISE-DEATH | FLAG[bull +4.65] |

### PA2-N5 x daily

(rolling prior-5 trigger bars | trigger daily | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -18.73 | -188.51 | -18.76 | +0.74 | 44 / 232 | -33.08 | -2.93 / -3.79 / -12.00 / -188.51 | stop=32,t1=12 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT1 | -25.60 | -167.27 | -25.64 | +0.64 | 42 / 229 | -39.52 | -9.27 / -4.07 / -12.26 / -167.27 | stop=32,t1=10 | F F F F | OK | open=0 | PREMISE-DEATH |

### PA2-N12 x daily

(rolling prior-12 trigger bars | trigger daily | 2 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -53.14 | -42.45 | -53.23 | +0.28 | 24 / 153 | -65.86 | -5.09 / +4.35 / -52.41 / -42.45 | stop=21,t1=3 | F F F F | OK | open=0 | PREMISE-DEATH | FLAG[side +4.35] |
| D1-b2bp-tT1 | -53.56 | -22.49 | -53.64 | +0.28 | 24 / 151 | -66.13 | -5.17 / +4.25 / -52.64 / -22.49 | stop=21,t1=3 | F F F F | OK | open=0 | PREMISE-DEATH | FLAG[side +4.25] |

### V1 x 5m

(prior UTC D1 candle | trigger 5m | 12 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V1-E x 5m

(prior EST(DST) D1 candle | trigger 5m | 12 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V1-KZ(London) x 5m

(prior UTC D1 candle | trigger 5m | 6 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V1-KZ(NYAM) x 5m

(prior UTC D1 candle | trigger 5m | 6 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D2-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V1 x 15m

(prior UTC D1 candle | trigger 15m | 12 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -24.56 | -99.99 | -24.60 | +0.61 | 177 / 765 | -29.24 | -1.56 / -18.11 / -4.90 / -99.99 | stop=141,t1=15,t3=21 | F F F F | OK | open=0 | COST-DEATH |
| D1-b0bp-tT2 | -24.57 | -105.41 | -24.61 | +0.60 | 210 / 933 | -26.19 | -1.18 / -18.35 / -5.05 / -105.41 | stop=141,t1=15,t2=33,t3=21 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT1 | -26.97 | -100.61 | -27.01 | +0.59 | 175 / 749 | -31.20 | -2.08 / -19.24 / -5.65 / -100.61 | stop=139,t1=15,t3=21 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -26.90 | -106.22 | -26.94 | +0.57 | 208 / 919 | -28.14 | -1.68 / -19.44 / -5.78 / -106.22 | stop=139,t1=15,t2=33,t3=21 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b0bp-tT1 | -28.04 | -99.03 | -28.08 | +0.44 | 164 / 682 | -29.76 | -5.40 / -17.57 / -5.06 / -99.03 | stop=139,t1=9,t3=16 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b0bp-tT2 | -24.38 | -107.04 | -24.42 | +0.50 | 187 / 777 | -25.62 | -4.22 / -16.28 / -3.88 / -107.04 | stop=139,t1=9,t2=23,t3=16 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b2bp-tT1 | -30.40 | -99.65 | -30.45 | +0.42 | 162 / 669 | -32.12 | -5.92 / -18.70 / -5.78 / -99.65 | stop=137,t1=9,t3=16 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b2bp-tT2 | -26.68 | -107.80 | -26.72 | +0.48 | 185 / 768 | -27.92 | -4.72 / -17.38 / -4.58 / -107.80 | stop=137,t1=9,t2=23,t3=16 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b0bp-tT1 | -24.56 | -99.99 | -24.60 | +0.61 | 177 / 765 | -29.24 | -1.56 / -18.11 / -4.90 / -99.99 | stop=141,t1=15,t3=21 | F F F F | OK | open=0 | COST-DEATH |
| D3-b0bp-tT2 | -24.57 | -105.41 | -24.61 | +0.60 | 210 / 933 | -26.19 | -1.18 / -18.35 / -5.05 / -105.41 | stop=141,t1=15,t2=33,t3=21 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT1 | -26.97 | -100.61 | -27.01 | +0.59 | 175 / 749 | -31.20 | -2.08 / -19.24 / -5.65 / -100.61 | stop=139,t1=15,t3=21 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -26.90 | -106.22 | -26.94 | +0.57 | 208 / 919 | -28.14 | -1.68 / -19.44 / -5.78 / -106.22 | stop=139,t1=15,t2=33,t3=21 | F F F F | OK | open=0 | PREMISE-DEATH |

### V1-E x 15m

(prior EST(DST) D1 candle | trigger 15m | 12 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -24.28 | -158.08 | -24.31 | +0.64 | 196 / 828 | -33.14 | -3.25 / -15.00 / -6.02 / -158.08 | stop=156,t1=14,t3=26 | F F F F | OK | open=0 | COST-DEATH |
| D1-b0bp-tT2 | -27.04 | -159.58 | -27.08 | +0.59 | 229 / 999 | -32.46 | -2.40 / -17.03 / -7.61 / -159.58 | stop=156,t1=14,t2=33,t3=26 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT1 | -26.35 | -161.51 | -26.39 | +0.62 | 192 / 809 | -34.78 | -3.56 / -16.03 / -6.76 / -161.51 | stop=152,t1=14,t3=26 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT2 | -29.02 | -162.62 | -29.07 | +0.57 | 225 / 980 | -34.05 | -2.68 / -18.03 / -8.31 / -162.62 | stop=152,t1=14,t2=33,t3=26 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b0bp-tT1 | -26.38 | -129.57 | -26.42 | +0.51 | 183 / 747 | -27.75 | -4.04 / -15.62 / -6.72 / -129.57 | stop=154,t1=7,t3=22 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b0bp-tT2 | -26.31 | -137.85 | -26.35 | +0.50 | 203 / 849 | -27.70 | -3.50 / -15.93 / -6.87 / -137.85 | stop=154,t1=7,t2=20,t3=22 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b2bp-tT1 | -28.53 | -132.33 | -28.57 | +0.49 | 179 / 731 | -29.78 | -4.34 / -16.76 / -7.42 / -132.33 | stop=150,t1=7,t3=22 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b2bp-tT2 | -28.40 | -140.21 | -28.45 | +0.48 | 199 / 835 | -29.70 | -3.79 / -17.06 / -7.56 / -140.21 | stop=150,t1=7,t2=20,t3=22 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b0bp-tT1 | -24.28 | -158.08 | -24.31 | +0.64 | 196 / 828 | -33.14 | -3.25 / -15.00 / -6.02 / -158.08 | stop=156,t1=14,t3=26 | F F F F | OK | open=0 | COST-DEATH |
| D3-b0bp-tT2 | -27.04 | -159.58 | -27.08 | +0.59 | 229 / 999 | -32.46 | -2.40 / -17.03 / -7.61 / -159.58 | stop=156,t1=14,t2=33,t3=26 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT1 | -26.35 | -161.51 | -26.39 | +0.62 | 192 / 809 | -34.78 | -3.56 / -16.03 / -6.76 / -161.51 | stop=152,t1=14,t3=26 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT2 | -29.02 | -162.62 | -29.07 | +0.57 | 225 / 980 | -34.05 | -2.68 / -18.03 / -8.31 / -162.62 | stop=152,t1=14,t2=33,t3=26 | F F F F | OK | open=0 | PREMISE-DEATH |

### V1-KZ(London) x 15m

(prior UTC D1 candle | trigger 15m | 6 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -14.20 | -22.43 | -14.22 | +0.05 | 39 / 160 | -14.20 | -1.33 / -9.16 / -3.71 / -22.43 | stop=37,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -11.05 | -23.76 | -11.07 | +0.22 | 42 / 185 | -11.05 | -0.49 / -8.44 / -2.12 / -23.76 | stop=37,t2=3,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b2bp-tT1 | -11.39 | -20.55 | -11.41 | +0.07 | 39 / 152 | -11.39 | -0.86 / -7.44 / -3.09 / -20.55 | stop=37,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b2bp-tT2 | -8.25 | -22.26 | -8.26 | +0.29 | 42 / 168 | -8.25 | -0.02 / -6.72 / -1.50 / -22.26 | stop=37,t2=3,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -14.20 | -22.43 | -14.22 | +0.05 | 39 / 160 | -14.20 | -1.33 / -9.16 / -3.71 / -22.43 | stop=37,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -11.05 | -23.76 | -11.07 | +0.22 | 42 / 185 | -11.05 | -0.49 / -8.44 / -2.12 / -23.76 | stop=37,t2=3,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |

### V1-KZ(NYAM) x 15m

(prior UTC D1 candle | trigger 15m | 6 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -8.89 | -20.06 | -8.90 | +0.53 | 57 / 227 | -8.89 | +0.62 / -6.50 / -3.01 / -20.06 | stop=47,t1=4,t3=6 | F F F F | OK | open=0 | PREMISE-DEATH | FLAG[bull +0.62] |
| D1-b2bp-tT2 | -8.65 | -26.42 | -8.66 | +0.53 | 66 / 279 | -8.65 | +1.33 / -6.67 / -3.31 / -26.42 | stop=47,t1=4,t2=9,t3=6 | F F F F | OK | open=0 | PREMISE-DEATH | FLAG[bull +1.33] |
| D2-b2bp-tT1 | -8.41 | -24.59 | -8.42 | +0.48 | 55 / 211 | -8.41 | -0.73 / -5.98 / -1.69 / -24.59 | stop=47,t1=3,t3=5 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b2bp-tT2 | -8.20 | -27.30 | -8.22 | +0.48 | 62 / 248 | -8.20 | -0.03 / -6.18 / -2.00 / -27.30 | stop=47,t1=3,t2=7,t3=5 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -8.89 | -20.06 | -8.90 | +0.53 | 57 / 227 | -8.89 | +0.62 / -6.50 / -3.01 / -20.06 | stop=47,t1=4,t3=6 | F F F F | OK | open=0 | PREMISE-DEATH | FLAG[bull +0.62] |
| D3-b2bp-tT2 | -8.65 | -26.42 | -8.66 | +0.53 | 66 / 279 | -8.65 | +1.33 / -6.67 / -3.31 / -26.42 | stop=47,t1=4,t2=9,t3=6 | F F F F | OK | open=0 | PREMISE-DEATH | FLAG[bull +1.33] |

### V1 x 1h

(prior UTC D1 candle | trigger 1h | 12 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -15.89 | -55.77 | -15.92 | +0.79 | 186 / 833 | -27.31 | -0.10 / -20.96 / +5.17 / -55.77 | stop=130,t1=26,t3=29,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +5.17] |
| D1-b0bp-tT2 | -19.89 | -70.04 | -19.93 | +0.72 | 242 / 1107 | -28.12 | -2.37 / -21.07 / +3.54 / -70.04 | stop=130,t1=26,t2=56,t3=29,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +3.54] |
| D1-b2bp-tT1 | -18.49 | -58.38 | -18.52 | +0.76 | 186 / 822 | -29.33 | -0.54 / -22.45 / +4.49 / -58.38 | stop=130,t1=26,t3=29,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +4.49] |
| D1-b2bp-tT2 | -22.39 | -71.32 | -22.42 | +0.70 | 242 / 1099 | -30.08 | -2.80 / -22.49 / +2.90 / -71.32 | stop=130,t1=26,t2=56,t3=29,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +2.90] |
| D2-b0bp-tT1 | -23.85 | -53.35 | -23.88 | +0.62 | 168 / 715 | -26.26 | -1.82 / -18.40 / -3.63 / -53.35 | stop=131,t1=14,t3=22,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D2-b0bp-tT2 | -21.45 | -61.83 | -21.48 | +0.64 | 206 / 880 | -22.83 | -2.52 / -16.89 / -2.04 / -61.83 | stop=131,t1=14,t2=38,t3=22,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D2-b2bp-tT1 | -26.47 | -53.72 | -26.51 | +0.59 | 168 / 707 | -28.85 | -2.24 / -19.90 / -4.33 / -53.72 | stop=131,t1=14,t3=22,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b2bp-tT2 | -23.96 | -62.00 | -24.00 | +0.61 | 206 / 877 | -25.30 | -2.93 / -18.34 / -2.69 / -62.00 | stop=131,t1=14,t2=38,t3=22,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D3-b0bp-tT1 | -15.89 | -55.77 | -15.92 | +0.79 | 186 / 833 | -27.31 | -0.10 / -20.96 / +5.17 / -55.77 | stop=130,t1=26,t3=29,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +5.17] |
| D3-b0bp-tT2 | -19.89 | -70.04 | -19.93 | +0.72 | 242 / 1107 | -28.12 | -2.37 / -21.07 / +3.54 / -70.04 | stop=130,t1=26,t2=56,t3=29,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +3.54] |
| D3-b2bp-tT1 | -18.49 | -58.38 | -18.52 | +0.76 | 186 / 822 | -29.33 | -0.54 / -22.45 / +4.49 / -58.38 | stop=130,t1=26,t3=29,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +4.49] |
| D3-b2bp-tT2 | -22.39 | -71.32 | -22.42 | +0.70 | 242 / 1099 | -30.08 | -2.80 / -22.49 / +2.90 / -71.32 | stop=130,t1=26,t2=56,t3=29,void=1 | F F F F | OK | open=0 | COST-DEATH | FLAG[bear +2.90] |

### V1-E x 1h

(prior EST(DST) D1 candle | trigger 1h | 12 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -28.50 | -118.76 | -28.55 | +0.65 | 193 / 861 | -37.32 | -6.02 / -16.24 / -6.24 / -118.76 | stop=133,t1=17,t3=42,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b0bp-tT2 | -27.42 | -124.98 | -27.46 | +0.64 | 243 / 1114 | -32.72 | -4.10 / -17.19 / -6.13 / -124.98 | stop=133,t1=17,t2=50,t3=42,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT1 | -31.16 | -122.23 | -31.21 | +0.63 | 193 / 854 | -39.68 | -6.42 / -17.86 / -6.87 / -122.23 | stop=133,t1=17,t3=42,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -29.94 | -128.29 | -29.99 | +0.62 | 243 / 1110 | -34.95 | -4.47 / -18.75 / -6.72 / -128.29 | stop=133,t1=17,t2=50,t3=42,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b0bp-tT1 | -21.42 | -85.46 | -21.45 | +0.67 | 176 / 753 | -28.47 | -3.95 / -11.74 / -5.73 / -85.46 | stop=131,t1=9,t3=35,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D2-b0bp-tT2 | -16.98 | -85.20 | -17.01 | +0.72 | 214 / 915 | -21.61 | -2.83 / -10.27 / -3.88 / -85.20 | stop=131,t1=9,t2=38,t3=35,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D2-b2bp-tT1 | -24.04 | -89.53 | -24.08 | +0.64 | 176 / 746 | -30.85 | -4.35 / -13.30 / -6.39 / -89.53 | stop=131,t1=9,t3=35,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D2-b2bp-tT2 | -19.45 | -89.23 | -19.49 | +0.69 | 214 / 911 | -23.84 | -3.20 / -11.78 / -4.48 / -89.23 | stop=131,t1=9,t2=38,t3=35,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D3-b0bp-tT1 | -28.50 | -118.76 | -28.55 | +0.65 | 193 / 861 | -37.32 | -6.02 / -16.24 / -6.24 / -118.76 | stop=133,t1=17,t3=42,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b0bp-tT2 | -27.42 | -124.98 | -27.46 | +0.64 | 243 / 1114 | -32.72 | -4.10 / -17.19 / -6.13 / -124.98 | stop=133,t1=17,t2=50,t3=42,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT1 | -31.16 | -122.23 | -31.21 | +0.63 | 193 / 854 | -39.68 | -6.42 / -17.86 / -6.87 / -122.23 | stop=133,t1=17,t3=42,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -29.94 | -128.29 | -29.99 | +0.62 | 243 / 1110 | -34.95 | -4.47 / -18.75 / -6.72 / -128.29 | stop=133,t1=17,t2=50,t3=42,void=1 | F F F F | OK | open=0 | PREMISE-DEATH |

### V1-KZ(London) x 1h

(prior UTC D1 candle | trigger 1h | 6 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -16.57 | -11.72 | -16.60 | +0.25 | 48 / 202 | -17.62 | -2.14 / -9.45 / -4.99 / -11.72 | stop=41,t1=3,t3=4 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -13.35 | -18.50 | -13.37 | +0.34 | 57 / 255 | -14.30 | -1.63 / -8.83 / -2.89 / -18.50 | stop=41,t1=3,t2=9,t3=4 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b2bp-tT1 | -12.06 | -8.83 | -12.08 | +0.33 | 47 / 190 | -13.82 | -1.36 / -6.41 / -4.29 / -8.83 | stop=41,t1=3,t3=3 | F F F F | OK | open=0 | PREMISE-DEATH |
| D2-b2bp-tT2 | -9.82 | -12.24 | -9.84 | +0.42 | 54 / 225 | -11.49 | -0.85 / -6.28 / -2.70 / -12.24 | stop=41,t1=3,t2=7,t3=3 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -16.57 | -11.72 | -16.60 | +0.25 | 48 / 202 | -17.62 | -2.14 / -9.45 / -4.99 / -11.72 | stop=41,t1=3,t3=4 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -13.35 | -18.50 | -13.37 | +0.34 | 57 / 255 | -14.30 | -1.63 / -8.83 / -2.89 / -18.50 | stop=41,t1=3,t2=9,t3=4 | F F F F | OK | open=0 | PREMISE-DEATH |

### V1-KZ(NYAM) x 1h

(prior UTC D1 candle | trigger 1h | 6 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -10.13 | -21.55 | -10.14 | +0.54 | 59 / 248 | -10.88 | -0.27 / -5.18 / -4.67 / -21.55 | stop=40,t1=8,t3=11 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -8.48 | -30.32 | -8.49 | +0.60 | 79 / 329 | -9.24 | +0.11 / -5.27 / -3.32 / -30.32 | stop=40,t1=8,t2=20,t3=11 | F F F F | OK | open=0 | COST-DEATH | FLAG[bull +0.11] |
| D2-b2bp-tT1 | -6.70 | -25.46 | -6.71 | +0.64 | 55 / 228 | -6.91 | -0.32 / -3.82 / -2.56 / -25.46 | stop=40,t1=6,t3=9 | F F F F | OK | open=0 | COST-DEATH |
| D2-b2bp-tT2 | -5.01 | -24.61 | -5.02 | +0.72 | 72 / 286 | -5.21 | +0.06 / -4.06 / -1.00 / -24.61 | stop=40,t1=6,t2=17,t3=9 | F F F F | OK | open=0 | COST-DEATH | FLAG[bull +0.06] |
| D3-b2bp-tT1 | -10.13 | -21.55 | -10.14 | +0.54 | 59 / 248 | -10.88 | -0.27 / -5.18 / -4.67 / -21.55 | stop=40,t1=8,t3=11 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -8.48 | -30.32 | -8.49 | +0.60 | 79 / 329 | -9.24 | +0.11 / -5.27 / -3.32 / -30.32 | stop=40,t1=8,t2=20,t3=11 | F F F F | OK | open=0 | COST-DEATH | FLAG[bull +0.11] |

### V2(D1.UTC-1h) x 5m

(first 1h of UTC day | trigger 5m | 8 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V2-KZ(D1.UTC-1h,London) x 5m

(first 1h of UTC day | trigger 5m | 4 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V2-KZ(D1.UTC-1h,NYAM) x 5m

(first 1h of UTC day | trigger 5m | 4 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V2(D1.UTC-1h) x 15m

(first 1h of UTC day | trigger 15m | 8 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -61.22 | -252.07 | -61.32 | +0.31 | 400 / 1706 | -61.22 | -8.96 / -35.15 / -17.12 / -252.07 | stop=271,t1=127,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b0bp-tT2 | -61.30 | -252.22 | -61.40 | +0.23 | 605 / 2554 | -61.30 | -10.01 / -33.34 / -17.95 / -252.22 | stop=271,t1=127,t2=205,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT1 | -57.72 | -252.43 | -57.82 | +0.34 | 385 / 1656 | -57.72 | -8.28 / -33.76 / -15.69 / -252.43 | stop=245,t1=138,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -58.15 | -251.85 | -58.25 | +0.26 | 600 / 2514 | -58.15 | -9.36 / -32.02 / -16.77 / -251.85 | stop=245,t1=138,t2=215,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b0bp-tT1 | -61.22 | -252.07 | -61.32 | +0.31 | 400 / 1706 | -61.22 | -8.96 / -35.15 / -17.12 / -252.07 | stop=271,t1=127,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b0bp-tT2 | -61.30 | -252.22 | -61.40 | +0.23 | 605 / 2554 | -61.30 | -10.01 / -33.34 / -17.95 / -252.22 | stop=271,t1=127,t2=205,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -57.72 | -252.43 | -57.82 | +0.34 | 385 / 1656 | -57.72 | -8.28 / -33.76 / -15.69 / -252.43 | stop=245,t1=138,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -58.15 | -251.85 | -58.25 | +0.26 | 600 / 2514 | -58.15 | -9.36 / -32.02 / -16.77 / -251.85 | stop=245,t1=138,t2=215,t3=2 | F F F F | OK | open=0 | PREMISE-DEATH |

### V2-KZ(D1.UTC-1h,London) x 15m

(first 1h of UTC day | trigger 15m | 4 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -15.66 | -67.16 | -15.69 | +0.25 | 89 / 460 | -15.66 | -2.27 / -9.23 / -4.16 / -67.16 | stop=66,t1=23 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -15.57 | -63.81 | -15.59 | +0.18 | 127 / 682 | -15.57 | -2.07 / -8.72 / -4.78 / -63.81 | stop=66,t1=23,t2=38 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -15.66 | -67.16 | -15.69 | +0.25 | 89 / 460 | -15.66 | -2.27 / -9.23 / -4.16 / -67.16 | stop=66,t1=23 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -15.57 | -63.81 | -15.59 | +0.18 | 127 / 682 | -15.57 | -2.07 / -8.72 / -4.78 / -63.81 | stop=66,t1=23,t2=38 | F F F F | OK | open=0 | PREMISE-DEATH |

### V2-KZ(D1.UTC-1h,NYAM) x 15m

(first 1h of UTC day | trigger 15m | 4 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -15.80 | -67.98 | -15.83 | +0.45 | 127 / 557 | -19.66 | -4.79 / -6.88 / -4.14 / -67.98 | stop=73,t1=54 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT2 | -17.46 | -74.35 | -17.49 | +0.33 | 201 / 875 | -19.25 | -4.38 / -7.16 / -5.92 / -74.35 | stop=73,t1=54,t2=74 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT1 | -15.80 | -67.98 | -15.83 | +0.45 | 127 / 557 | -19.66 | -4.79 / -6.88 / -4.14 / -67.98 | stop=73,t1=54 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT2 | -17.46 | -74.35 | -17.49 | +0.33 | 201 / 875 | -19.25 | -4.38 / -7.16 / -5.92 / -74.35 | stop=73,t1=54,t2=74 | F F F F | OK | open=0 | COST-DEATH |

### V2(D1.EST-1h) x 5m

(first 1h of ET day (08:00-09:00 ET) | trigger 5m | 8 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V2-KZ(D1.EST-1h,London) x 5m

(first 1h of ET day (08:00-09:00 ET) | trigger 5m | 4 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V2-KZ(D1.EST-1h,NYAM) x 5m

(first 1h of ET day (08:00-09:00 ET) | trigger 5m | 4 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V2(D1.EST-1h) x 15m

(first 1h of ET day (08:00-09:00 ET) | trigger 15m | 8 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -54.10 | -308.58 | -54.19 | +0.41 | 394 / 1867 | -54.18 | -3.44 / -27.67 / -22.99 / -308.58 | stop=215,t1=174,t3=5 | F F F F | OK | open=0 | COST-DEATH |
| D1-b0bp-tT2 | -60.55 | -314.89 | -60.65 | +0.29 | 621 / 2857 | -60.59 | -5.49 / -32.40 / -22.66 / -314.89 | stop=215,t1=174,t2=227,t3=5 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT1 | -53.11 | -306.36 | -53.20 | +0.42 | 378 / 1814 | -53.19 | -2.82 / -27.22 / -23.07 / -306.36 | stop=198,t1=175,t3=5 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT2 | -58.88 | -310.35 | -58.98 | +0.30 | 606 / 2822 | -58.92 | -4.62 / -31.63 / -22.64 / -310.35 | stop=198,t1=175,t2=228,t3=5 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b0bp-tT1 | -54.10 | -308.58 | -54.19 | +0.41 | 394 / 1867 | -54.18 | -3.44 / -27.67 / -22.99 / -308.58 | stop=215,t1=174,t3=5 | F F F F | OK | open=0 | COST-DEATH |
| D3-b0bp-tT2 | -60.55 | -314.89 | -60.65 | +0.29 | 621 / 2857 | -60.59 | -5.49 / -32.40 / -22.66 / -314.89 | stop=215,t1=174,t2=227,t3=5 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -53.11 | -306.36 | -53.20 | +0.42 | 378 / 1814 | -53.19 | -2.82 / -27.22 / -23.07 / -306.36 | stop=198,t1=175,t3=5 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT2 | -58.88 | -310.35 | -58.98 | +0.30 | 606 / 2822 | -58.92 | -4.62 / -31.63 / -22.64 / -310.35 | stop=198,t1=175,t2=228,t3=5 | F F F F | OK | open=0 | PREMISE-DEATH |

### V2-KZ(D1.EST-1h,London) x 15m

(first 1h of ET day (08:00-09:00 ET) | trigger 15m | 4 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V2-KZ(D1.EST-1h,NYAM) x 15m

(first 1h of ET day (08:00-09:00 ET) | trigger 15m | 4 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -31.93 | -166.88 | -31.98 | +0.44 | 222 / 1005 | -32.00 | -0.84 / -15.97 / -15.12 / -166.88 | stop=123,t1=98,t3=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -36.62 | -170.83 | -36.68 | +0.30 | 347 / 1557 | -36.66 | -1.66 / -19.26 / -15.69 / -170.83 | stop=123,t1=98,t2=125,t3=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -31.93 | -166.88 | -31.98 | +0.44 | 222 / 1005 | -32.00 | -0.84 / -15.97 / -15.12 / -166.88 | stop=123,t1=98,t3=1 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -36.62 | -170.83 | -36.68 | +0.30 | 347 / 1557 | -36.66 | -1.66 / -19.26 / -15.69 / -170.83 | stop=123,t1=98,t2=125,t3=1 | F F F F | OK | open=0 | PREMISE-DEATH |

### V3(4h-prior) x 5m

(prior 4h candle | trigger 5m | 8 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V3(4h-prior) x 15m

(prior 4h candle | trigger 15m | 8 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -154.70 | -709.62 | -154.95 | +0.43 | 1140 / 4897 | -154.72 | -33.11 / -63.85 / -57.74 / -709.62 | stop=741,t1=143,t3=244,void=12 | F F F F | OK | open=0 | COST-DEATH |
| D1-b0bp-tT2 | -156.64 | -702.79 | -156.89 | +0.39 | 1498 / 6546 | -156.66 | -31.27 / -71.56 / -53.81 / -702.79 | stop=741,t1=143,t2=358,t3=244,void=12 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT1 | -153.10 | -710.12 | -153.34 | +0.44 | 1094 / 4767 | -153.10 | -33.00 / -60.02 / -60.08 / -710.12 | stop=690,t1=144,t3=247,void=13 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT2 | -154.67 | -701.49 | -154.92 | +0.40 | 1456 / 6441 | -154.67 | -31.01 / -67.76 / -55.89 / -701.49 | stop=690,t1=144,t2=362,t3=247,void=13 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b0bp-tT1 | -154.70 | -709.62 | -154.95 | +0.43 | 1140 / 4897 | -154.72 | -33.11 / -63.85 / -57.74 / -709.62 | stop=741,t1=143,t3=244,void=12 | F F F F | OK | open=0 | COST-DEATH |
| D3-b0bp-tT2 | -156.64 | -702.79 | -156.89 | +0.39 | 1498 / 6546 | -156.66 | -31.27 / -71.56 / -53.81 / -702.79 | stop=741,t1=143,t2=358,t3=244,void=12 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT1 | -153.10 | -710.12 | -153.34 | +0.44 | 1094 / 4767 | -153.10 | -33.00 / -60.02 / -60.08 / -710.12 | stop=690,t1=144,t3=247,void=13 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT2 | -154.67 | -701.49 | -154.92 | +0.40 | 1456 / 6441 | -154.67 | -31.01 / -67.76 / -55.89 / -701.49 | stop=690,t1=144,t2=362,t3=247,void=13 | F F F F | OK | open=0 | PREMISE-DEATH |

### V3(1h-prior) x 1m

(prior 1h candle | trigger 1m | 8 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V3(1h-prior) x 5m

(prior 1h candle | trigger 5m | 8 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b0bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V3(1h-prior) x 15m

(prior 1h candle | trigger 15m | 8 combos)

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b0bp-tT1 | -543.14 | -2293.39 | -544.01 | +0.26 | 3909 / 16301 | -543.27 | -90.98 / -285.62 / -166.54 / -2293.39 | stop=2068,t1=814,t3=959,void=68 | F F F F | OK | open=0 | COST-DEATH |
| D1-b0bp-tT2 | -560.09 | -2359.04 | -560.99 | +0.19 | 5754 / 23994 | -560.13 | -91.45 / -295.98 / -172.65 / -2359.04 | stop=2068,t1=814,t2=1845,t3=959,void=68 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT1 | -533.00 | -2276.08 | -533.85 | +0.27 | 3785 / 15923 | -533.23 | -89.19 / -275.46 / -168.35 / -2276.08 | stop=1835,t1=826,t3=1027,void=97 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -547.90 | -2333.80 | -548.77 | +0.20 | 5672 / 23762 | -547.97 | -88.73 / -285.28 / -173.89 / -2333.80 | stop=1835,t1=826,t2=1887,t3=1027,void=97 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b0bp-tT1 | -543.14 | -2293.39 | -544.01 | +0.26 | 3909 / 16301 | -543.27 | -90.98 / -285.62 / -166.54 / -2293.39 | stop=2068,t1=814,t3=959,void=68 | F F F F | OK | open=0 | COST-DEATH |
| D3-b0bp-tT2 | -560.09 | -2359.04 | -560.99 | +0.19 | 5754 / 23994 | -560.13 | -91.45 / -295.98 / -172.65 / -2359.04 | stop=2068,t1=814,t2=1845,t3=959,void=68 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -533.00 | -2276.08 | -533.85 | +0.27 | 3785 / 15923 | -533.23 | -89.19 / -275.46 / -168.35 / -2276.08 | stop=1835,t1=826,t3=1027,void=97 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -547.90 | -2333.80 | -548.77 | +0.20 | 5672 / 23762 | -547.97 | -88.73 / -285.28 / -173.89 / -2333.80 | stop=1835,t1=826,t2=1887,t3=1027,void=97 | F F F F | OK | open=0 | PREMISE-DEATH |

### V3-KZ(1h-prior,London) x 1m

(prior 1h candle | trigger 1m | 4 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V3-KZ(1h-prior,NYAM) x 1m

(prior 1h candle | trigger 1m | 4 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V3-KZ(1h-prior,London) x 5m

(prior 1h candle | trigger 5m | 4 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V3-KZ(1h-prior,NYAM) x 5m

(prior 1h candle | trigger 5m | 4 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V3-KZ(1h-prior,London) x 15m

(prior 1h candle | trigger 15m | 4 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -69.52 | -287.23 | -69.63 | +0.20 | 471 / 1987 | -69.60 | -8.90 / -38.59 / -22.03 / -287.23 | stop=237,t1=99,t3=123,void=12 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -71.91 | -292.26 | -72.03 | +0.15 | 691 / 3007 | -71.94 | -8.79 / -41.04 / -22.08 / -292.26 | stop=237,t1=99,t2=220,t3=123,void=12 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -69.52 | -287.23 | -69.63 | +0.20 | 471 / 1987 | -69.60 | -8.90 / -38.59 / -22.03 / -287.23 | stop=237,t1=99,t3=123,void=12 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -71.91 | -292.26 | -72.03 | +0.15 | 691 / 3007 | -71.94 | -8.79 / -41.04 / -22.08 / -292.26 | stop=237,t1=99,t2=220,t3=123,void=12 | F F F F | OK | open=0 | PREMISE-DEATH |

### V3-KZ(1h-prior,NYAM) x 15m

(prior 1h candle | trigger 15m | 4 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -87.80 | -384.74 | -87.94 | +0.24 | 555 / 2439 | -87.96 | -11.45 / -45.68 / -30.67 / -384.74 | stop=277,t1=176,t3=93,void=9 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -92.73 | -392.07 | -92.87 | +0.16 | 856 / 3718 | -92.76 | -11.27 / -49.33 / -32.12 / -392.07 | stop=277,t1=176,t2=301,t3=93,void=9 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -87.80 | -384.74 | -87.94 | +0.24 | 555 / 2439 | -87.96 | -11.45 / -45.68 / -30.67 / -384.74 | stop=277,t1=176,t3=93,void=9 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -92.73 | -392.07 | -92.87 | +0.16 | 856 / 3718 | -92.76 | -11.27 / -49.33 / -32.12 / -392.07 | stop=277,t1=176,t2=301,t3=93,void=9 | F F F F | OK | open=0 | PREMISE-DEATH |

### V3-KZ(4h-prior,London) x 5m

(prior 4h candle | trigger 5m | 4 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V3-KZ(4h-prior,NYAM) x 5m

(prior 4h candle | trigger 5m | 4 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D1-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT1 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |
| D3-b2bp-tT2 | +0.00 | +0.00 | +0.00 | n/a | 0 / 0 | +0.00 | +0.00 / +0.00 / +0.00 / +0.00 |  | F F F F | thin | open=0 | STAT-STERILE |

### V3-KZ(4h-prior,London) x 15m

(prior 4h candle | trigger 15m | 4 combos | KZ London (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -23.98 | -126.71 | -24.02 | +0.45 | 211 / 829 | -24.16 | -4.09 / -9.03 / -10.86 / -126.71 | stop=130,t1=23,t3=57,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D1-b2bp-tT2 | -24.94 | -122.05 | -24.98 | +0.40 | 279 / 1105 | -25.19 | -4.47 / -10.06 / -10.41 / -122.05 | stop=130,t1=23,t2=68,t3=57,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT1 | -23.98 | -126.71 | -24.02 | +0.45 | 211 / 829 | -24.16 | -4.09 / -9.03 / -10.86 / -126.71 | stop=130,t1=23,t3=57,void=1 | F F F F | OK | open=0 | COST-DEATH |
| D3-b2bp-tT2 | -24.94 | -122.05 | -24.98 | +0.40 | 279 / 1105 | -25.19 | -4.47 / -10.06 / -10.41 / -122.05 | stop=130,t1=23,t2=68,t3=57,void=1 | F F F F | OK | open=0 | COST-DEATH |

### V3-KZ(4h-prior,NYAM) x 15m

(prior 4h candle | trigger 15m | 4 combos | KZ NYAM (ET clock))

| combo | judge net$ | train net$ | %/yr | PF | rows(j/tr) | MDD$ | net B/S/D | exits | A B C D | floor | row count | autopsy |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| D1-b2bp-tT1 | -39.02 | -167.79 | -39.09 | +0.41 | 238 / 1127 | -40.84 | -6.99 / -18.45 / -13.59 / -167.79 | stop=156,t1=51,t3=25,void=6 | F F F F | OK | open=0 | PREMISE-DEATH |
| D1-b2bp-tT2 | -39.24 | -171.56 | -39.30 | +0.36 | 331 / 1609 | -40.10 | -6.83 / -19.96 / -12.45 / -171.56 | stop=156,t1=51,t2=93,t3=25,void=6 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT1 | -39.02 | -167.79 | -39.09 | +0.41 | 238 / 1127 | -40.84 | -6.99 / -18.45 / -13.59 / -167.79 | stop=156,t1=51,t3=25,void=6 | F F F F | OK | open=0 | PREMISE-DEATH |
| D3-b2bp-tT2 | -39.24 | -171.56 | -39.30 | +0.36 | 331 / 1609 | -40.10 | -6.83 / -19.96 / -12.45 / -171.56 | stop=156,t1=51,t2=93,t3=25,void=6 | F F F F | OK | open=0 | PREMISE-DEATH |

## Forensics gate (bar-level re-derivation, 0 tolerance)

- PA1-D1UT x 1m [D1-b0bp-tT1]: 0 judge rows checked -> PASS
- PA2-N3 x 1m [D1-b0bp-tT1]: 40 judge rows checked -> PASS
- V1 x 5m [D1-b0bp-tT1]: 0 judge rows checked -> PASS
- V1-KZ(London) x 5m [D1-b2bp-tT1]: 0 judge rows checked -> PASS
- V2(D1.UTC-1h) x 5m [D1-b0bp-tT1]: 0 judge rows checked -> PASS
- V2-KZ(D1.UTC-1h,London) x 5m [D1-b2bp-tT1]: 0 judge rows checked -> PASS
- V3(4h-prior) x 5m [D1-b0bp-tT1]: 0 judge rows checked -> PASS
- V3-KZ(1h-prior,London) x 1m [D1-b2bp-tT1]: 0 judge rows checked -> PASS

- TOTAL rows independently re-derived: 40; mismatches: 0

## S1 summary

- Lines judged: 352. Autopsy tags: {'STAT-STERILE': 144, 'COST-DEATH': 99, 'PREMISE-DEATH': 107, 'ALIVE': 2}
- Survivor lines (bar A + floor): 2
  - PA2-N12 x 4h / D1-b0bp-tT1: net $6.09 (+6.10%/yr notional), PF +1.05, B/S/D +2.59/+4.22/-0.71, MDD $-43.41, rows 138
  - PA2-N12 x 4h / D1-b2bp-tT1: net $7.43 (+7.45%/yr notional), PF +1.06, B/S/D +3.61/+5.24/-1.42, MDD $-41.27, rows 134
- Forensics: PASS (all sampled fills re-derived exactly; verdicts stand).

## Data + artifact stamps

- lane 1m: 2,628,881 bars 2021-11-05 00:00:00 -> 2026-11-04 16:00:00 (fetch(in-RAM, raw discarded))
- lane 5m: 525,777 bars 2021-11-05 00:00:00 -> 2026-11-04 16:00:00 (fetch(in-RAM, raw discarded))
- lane 15m: 174,699 bars 2021-11-10 20:15:00 -> 2026-11-04 16:00:00 (disk)
- lane 1h: 43,797 bars 2021-11-05 19:00:00 -> 2026-11-04 16:00:00 (disk)
- lane 4h: 10,950 bars 2021-11-05 20:00:00 -> 2026-11-04 16:00:00 (disk)
- lane daily: 1,826 bars 2021-11-05 00:00:00 -> 2026-11-04 00:00:00 (disk)
- anchors: UTC/EST daily + W-SUN weekly from 1h deep; 4h/1h from source candles; first-candle from the 1h grid; rolling N at trigger
- regime months: {'sideways': 33, 'bear': 14, 'bull': 14}
- artifacts: crt/data_agg/anchors/*.csv (KB-scale), crt/data_agg/s1_lines.csv, crt/data_agg/s1_survivor_trades.csv
- registry: Scope S1 executed; per-line verdicts above; global closure reading deferred to the CP2 review (user owns it)