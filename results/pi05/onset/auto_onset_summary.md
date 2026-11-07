# Automatic onset (07_auto_onset.py)

1288 natural episodes: 90 failures, 1198 successes.
stuck_n = 7 boundaries (56 policy steps) without an eef move > 0.01 m. Share of successes with a stuck event per n: 5: 0.084, 6: 0.055, 7: 0.048.
Thresholds: fully closed < 5 mm, lifted > 3 cm, held within 10 cm, drop > 2 cm relative to the eef.

| version | failures with onset | silent failures (no event) |
|---|---|---|
| onset_any | 86 of 90 | 4: t04_e04_p0, t08_e28_p0, t08_e33_p0, t08_e43_p0 |
| onset_strict | 51 of 90 | 39: t00_e14_n0, t08_e00_n0, t08_e02_n0, t08_e03_n0, t08_e09_n0, t08_e13_n0, t08_e15_n0, t08_e28_n0, t08_e29_n0, t08_e41_n0, t09_e18_n0, t09_e47_n0, t00_e18_p0, t00_e04_p0_s1, t00_e06_p0_s1, t00_e10_p0_s1, t01_e23_p0_s1, t01_e32_p0_s1, t03_e11_p0, t04_e04_p0, t04_e07_p0, t04_e35_p0_s1, t06_e11_p0, t06_e44_p0_s1, t07_e48_p0, t07_e28_p0_s1, t07_e31_p0_s1, t07_e42_p0_s1, t07_e49_p0_s1, t08_e10_p0, t08_e17_p0, t08_e28_p0, t08_e29_p0, t08_e31_p0, t08_e33_p0, t08_e41_p0, t08_e43_p0, t09_e37_p0, t09_e48_p0 |

| event | failures with it | first event in failures (onset_any) | successes with it (recovered slips) |
|---|---|---|---|
| missed_grasp | 50 | 26 | 127 |
| drop | 4 | 0 | 7 |
| stuck | 78 | 60 | 58 |
| wrong_object | 2 | 0 | 0 |

Successes with at least one event: 169 of 1198; with a strict event: 131 of 1198.

Intervention window onset - t_pnr (steps; tau 0.5; t_pnr 0 = doomed from start):

| episode | t_pnr | onset_any | window_any | onset_strict | window_strict | onset_after_pnr (event) | window_after_pnr |
|---|---|---|---|---|---|---|---|
| t00_e14_n0 | 0 | 112 | 112 | None | None | 112 (stuck) | 112 |
| t00_e49_n0 | 64 | 112 | 48 | 336 | 272 | 112 (stuck) | 48 |
| t06_e21_n0 | 304 | 192 | -112 | 352 | 48 | 352 (missed_grasp) | 48 |
| t06_e32_n0 | 56 | 168 | 112 | 368 | 312 | 168 (stuck) | 112 |
| t06_e39_n0 | 128 | 160 | 32 | 328 | 200 | 160 (stuck) | 32 |
| t06_e46_n0 | 56 | 280 | 224 | 456 | 400 | 280 (stuck) | 224 |
| t07_e03_n0 | None | 168 | None | 480 | None | None () | None |
| t07_e16_n0 | None | 176 | None | 464 | None | None () | None |
| t07_e33_n0 | None | 184 | None | 472 | None | None () | None |
| t00_e24_p0 | 0 | 72 | 72 | 72 | 72 | 72 (missed_grasp) | 72 |
| t00_e04_p0_s1 | 0 | 112 | 112 | None | None | 112 (stuck) | 112 |
| t00_e06_p0_s1 | 0 | 240 | 240 | None | None | 240 (stuck) | 240 |
| t00_e07_p0_s1 | 0 | 64 | 64 | 64 | 64 | 64 (missed_grasp) | 64 |
| t00_e10_p0_s1 | 0 | 256 | 256 | None | None | 256 (stuck) | 256 |
| t00_e32_p0_s1 | 184 | 184 | 0 | 328 | 144 | 184 (stuck) | 0 |
| t00_e41_p0_s1 | 0 | 96 | 96 | 96 | 96 | 96 (missed_grasp) | 96 |
| t01_e16_p0 | 296 | 256 | -40 | 256 | -40 | 312 (missed_grasp) | 16 |
| t01_e34_p0 | 152 | 264 | 112 | 352 | 200 | 264 (stuck) | 112 |
| t01_e40_p0 | 104 | 256 | 152 | 256 | 152 | 256 (missed_grasp) | 152 |
| t01_e23_p0_s1 | 400 | 224 | -176 | None | None | None () | None |
| t01_e32_p0_s1 | 0 | 232 | 232 | None | None | 232 (stuck) | 232 |
| t04_e07_p0 | 120 | 360 | 240 | None | None | 360 (stuck) | 240 |
| t04_e21_p0 | 56 | 48 | -8 | 48 | -8 | 304 (missed_grasp) | 248 |
| t04_e42_p0 | 488 | 56 | -432 | 56 | -432 | None () | None |
| t04_e35_p0_s1 | 48 | 392 | 344 | None | None | 392 (stuck) | 344 |
| t06_e05_p0 | 216 | 200 | -16 | 200 | -16 | 248 (missed_grasp) | 32 |
| t06_e09_p0 | 88 | 264 | 176 | 280 | 192 | 264 (stuck) | 176 |
| t06_e11_p0 | 296 | 168 | -128 | None | None | 384 (stuck) | 88 |
| t06_e40_p0 | 344 | 72 | -272 | 72 | -272 | 384 (missed_grasp) | 40 |
| t06_e11_p0_s1 | 408 | 176 | -232 | 488 | 80 | 488 (missed_grasp) | 80 |
| t06_e21_p0_s1 | 0 | 160 | 160 | 240 | 240 | 160 (stuck) | 160 |
| t06_e26_p0_s1 | 64 | 64 | 0 | 64 | 0 | 64 (missed_grasp) | 0 |
| t06_e27_p0_s1 | 240 | 120 | -120 | 120 | -120 | 328 (missed_grasp) | 88 |
| t06_e29_p0_s1 | 344 | 200 | -144 | 200 | -144 | 344 (missed_grasp) | 0 |
| t06_e43_p0_s1 | 0 | 160 | 160 | 496 | 496 | 160 (stuck) | 160 |
| t06_e44_p0_s1 | 192 | 288 | 96 | None | None | 288 (stuck) | 96 |
| t07_e28_p0_s1 | 232 | 400 | 168 | None | None | 400 (stuck) | 168 |
| t07_e29_p0_s1 | 416 | 80 | -336 | 80 | -336 | 456 (stuck) | 40 |
| t07_e42_p0_s1 | 184 | 320 | 136 | None | None | 320 (stuck) | 136 |
| t07_e49_p0_s1 | 72 | 192 | 120 | None | None | 192 (stuck) | 120 |

Failures with a t_pnr: 37 of 40 scanned (10 doomed from start). With an event at or after t_pnr: 35. Onset before t_pnr (window < 0): onset_any 12, onset_strict 8.
