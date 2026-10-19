# Automatic onset (07_auto_onset.py)

500 natural episodes: 28 failures, 472 successes.
stuck_n = 8 boundaries (64 policy steps) without an eef move > 0.01 m. Share of successes with a stuck event per n: 5: 0.108, 6: 0.070, 7: 0.055, 8: 0.049.
Thresholds: fully closed < 5 mm, lifted > 3 cm, held within 10 cm, drop > 2 cm relative to the eef.

| version | failures with onset | silent failures (no event) |
|---|---|---|
| onset_any | 28 of 28 | 0:  |
| onset_strict | 21 of 28 | 7: t06_e20_n0, t06_e23_n0, t06_e25_n0, t06_e28_n0, t08_e47_n0, t09_e25_n0, t09_e34_n0 |

| event | failures with it | first event in failures (onset_any) | successes with it (recovered slips) |
|---|---|---|---|
| missed_grasp | 21 | 15 | 38 |
| drop | 1 | 0 | 2 |
| stuck | 24 | 10 | 23 |
| wrong_object | 3 | 3 | 0 |

Successes with at least one event: 56 of 472; with a strict event: 39 of 472.

Intervention window onset - t_pnr (steps; tau 0.5; t_pnr 0 = doomed from start):

| episode | t_pnr | onset_any | window_any | onset_strict | window_strict | onset_after_pnr (event) | window_after_pnr |
|---|---|---|---|---|---|---|---|
| t00_e08_n0 | 0 | 72 | 72 | 72 | 72 | 72 (wrong_object) | 72 |
| t00_e14_n0 | 368 | 112 | -256 | 112 | -256 | 376 (missed_grasp) | 8 |
| t00_e27_n0 | 0 | 120 | 120 | 120 | 120 | 120 (wrong_object) | 120 |
| t00_e42_n0 | 0 | 72 | 72 | 72 | 72 | 72 (wrong_object) | 72 |
| t01_e41_n0 | 152 | 288 | 136 | 288 | 136 | 288 (missed_grasp) | 136 |
| t02_e10_n0 | 184 | 208 | 24 | 208 | 24 | 208 (missed_grasp) | 24 |
| t03_e37_n0 | None | 88 | None | 88 | None | None () | None |
| t03_e43_n0 | None | 96 | None | 96 | None | None () | None |
| t04_e11_n0 | 176 | 112 | -64 | 112 | -64 | None () | None |
| t06_e20_n0 | None | 304 | None | None | None | None () | None |
| t06_e23_n0 | 432 | 344 | -88 | None | None | None () | None |
| t06_e25_n0 | 392 | 296 | -96 | None | None | None () | None |
| t06_e26_n0 | 376 | 176 | -200 | 400 | 24 | 400 (missed_grasp) | 24 |
| t06_e27_n0 | 472 | 128 | -344 | 128 | -344 | None () | None |
| t06_e28_n0 | None | 296 | None | None | None | None () | None |
| t08_e04_n0 | 488 | 360 | -128 | 504 | 16 | 504 (missed_grasp) | 16 |
| t08_e06_n0 | None | 144 | None | 144 | None | None () | None |
| t08_e08_n0 | None | 336 | None | 336 | None | None () | None |
| t08_e11_n0 | None | 288 | None | 288 | None | None () | None |
| t08_e12_n0 | None | 304 | None | 304 | None | None () | None |
| t08_e20_n0 | None | 168 | None | 208 | None | None () | None |
| t08_e27_n0 | None | 312 | None | 312 | None | None () | None |
| t08_e30_n0 | None | 352 | None | 352 | None | None () | None |
| t08_e38_n0 | 232 | 304 | 72 | 304 | 72 | 304 (missed_grasp) | 72 |
| t08_e45_n0 | None | 288 | None | 288 | None | None () | None |
| t08_e47_n0 | None | 376 | None | None | None | None () | None |
| t09_e25_n0 | 192 | 304 | 112 | None | None | 304 (stuck) | 112 |
| t09_e34_n0 | None | 248 | None | None | None | None () | None |

Failures with a t_pnr: 14 of 28 scanned (3 doomed from start). With an event at or after t_pnr: 10. Onset before t_pnr (window < 0): onset_any 7, onset_strict 3.
