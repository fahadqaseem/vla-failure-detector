# Automatic onset (07_auto_onset.py)

1238 natural episodes: 167 failures, 1071 successes.
stuck_n = 8 boundaries (64 policy steps) without an eef move > 0.01 m. Share of successes with a stuck event per n: 5: 0.092, 6: 0.065, 7: 0.053, 8: 0.047.
Thresholds: fully closed < 5 mm, lifted > 3 cm, held within 10 cm, drop > 2 cm relative to the eef.

| version | failures with onset | silent failures (no event) |
|---|---|---|
| onset_any | 163 of 167 | 4: t01_e34_p0, t04_e03_p0, t04_e16_p0, t04_e41_p0 |
| onset_strict | 137 of 167 | 30: t06_e20_n0, t06_e23_n0, t06_e25_n0, t06_e28_n0, t08_e47_n0, t09_e25_n0, t09_e34_n0, t00_e43_p0, t00_e44_p0, t01_e31_p0, t01_e34_p0, t04_e03_p0, t04_e16_p0, t04_e41_p0, t04_e47_p0, t04_e49_p0, t06_e11_p0, t06_e13_p0, t08_e10_p0, t08_e23_p0, t08_e32_p0, t08_e37_p0, t00_e16_p0_s1, t00_e27_p0_s2, t00_e33_p0_s2, t01_e32_p0_s1, t04_e01_p0_s2, t04_e21_p0_s1, t07_e33_p0_s1, t07_e33_p0_s2 |

| event | failures with it | first event in failures (onset_any) | successes with it (recovered slips) |
|---|---|---|---|
| missed_grasp | 126 | 94 | 82 |
| drop | 10 | 3 | 5 |
| stuck | 131 | 48 | 50 |
| wrong_object | 25 | 18 | 1 |

Successes with at least one event: 117 of 1071; with a strict event: 85 of 1071.

Intervention window onset - t_pnr (steps; tau 0.5; t_pnr 0 = doomed from start):

| episode | t_pnr | onset_any | window_any | onset_strict | window_strict | onset_after_pnr (event) | window_after_pnr |
|---|---|---|---|---|---|---|---|
| t00_e08_n0 | 0 | 72 | 72 | 72 | 72 | 72 (wrong_object) | 72 |
| t00_e14_n0 | 288 | 112 | -176 | 112 | -176 | 296 (missed_grasp) | 8 |
| t00_e27_n0 | 0 | 120 | 120 | 120 | 120 | 120 (wrong_object) | 120 |
| t00_e42_n0 | 0 | 72 | 72 | 72 | 72 | 72 (wrong_object) | 72 |
| t01_e41_n0 | 176 | 288 | 112 | 288 | 112 | 288 (missed_grasp) | 112 |
| t02_e10_n0 | 184 | 208 | 24 | 208 | 24 | 208 (missed_grasp) | 24 |
| t03_e37_n0 | None | 88 | None | 88 | None | None () | None |
| t03_e43_n0 | None | 96 | None | 96 | None | None () | None |
| t04_e11_n0 | 184 | 112 | -72 | 112 | -72 | None () | None |
| t06_e20_n0 | None | 304 | None | None | None | None () | None |
| t06_e23_n0 | 472 | 344 | -128 | None | None | None () | None |
| t06_e25_n0 | 464 | 296 | -168 | None | None | None () | None |
| t06_e26_n0 | 312 | 176 | -136 | 400 | 88 | 400 (missed_grasp) | 88 |
| t06_e27_n0 | 464 | 128 | -336 | 128 | -336 | None () | None |
| t06_e28_n0 | None | 296 | None | None | None | None () | None |
| t08_e04_n0 | 488 | 360 | -128 | 504 | 16 | 504 (missed_grasp) | 16 |
| t08_e06_n0 | None | 144 | None | 144 | None | None () | None |
| t08_e08_n0 | None | 336 | None | 336 | None | None () | None |
| t08_e11_n0 | None | 288 | None | 288 | None | None () | None |
| t08_e12_n0 | None | 304 | None | 304 | None | None () | None |
| t08_e20_n0 | None | 168 | None | 208 | None | None () | None |
| t08_e27_n0 | None | 312 | None | 312 | None | None () | None |
| t08_e30_n0 | None | 352 | None | 352 | None | None () | None |
| t08_e38_n0 | 264 | 304 | 40 | 304 | 40 | 304 (missed_grasp) | 40 |
| t08_e45_n0 | None | 288 | None | 288 | None | None () | None |
| t08_e47_n0 | None | 376 | None | None | None | None () | None |
| t09_e25_n0 | 176 | 304 | 128 | None | None | 304 (stuck) | 128 |
| t09_e34_n0 | None | 248 | None | None | None | None () | None |
| t00_e07_p0 | 0 | 96 | 96 | 96 | 96 | 96 (missed_grasp) | 96 |
| t00_e09_p0 | 24 | 144 | 120 | 168 | 144 | 144 (stuck) | 120 |
| t00_e13_p0 | 0 | 152 | 152 | 152 | 152 | 152 (wrong_object) | 152 |
| t00_e18_p0 | 0 | 192 | 192 | 192 | 192 | 192 (wrong_object) | 192 |
| t00_e20_p0 | 0 | 80 | 80 | 80 | 80 | 80 (wrong_object) | 80 |
| t00_e28_p0 | 0 | 152 | 152 | 152 | 152 | 152 (missed_grasp) | 152 |
| t00_e29_p0 | 0 | 112 | 112 | 112 | 112 | 112 (missed_grasp) | 112 |
| t00_e32_p0 | 0 | 104 | 104 | 104 | 104 | 104 (missed_grasp) | 104 |
| t00_e41_p0 | 0 | 104 | 104 | 104 | 104 | 104 (missed_grasp) | 104 |
| t00_e42_p0 | 0 | 64 | 64 | 64 | 64 | 64 (wrong_object) | 64 |
| t00_e43_p0 | 336 | 200 | -136 | None | None | None () | None |
| t00_e44_p0 | 256 | 192 | -64 | None | None | None () | None |
| t00_e48_p0 | 0 | 72 | 72 | 72 | 72 | 72 (wrong_object) | 72 |
| t01_e31_p0 | 200 | 360 | 160 | None | None | 360 (stuck) | 160 |
| t01_e33_p0 | 0 | 72 | 72 | 72 | 72 | 72 (missed_grasp) | 72 |
| t01_e34_p0 | 64 | None | None | None | None | None () | None |
| t04_e02_p0 | 0 | 56 | 56 | 56 | 56 | 56 (missed_grasp) | 56 |
| t04_e03_p0 | 96 | None | None | None | None | None () | None |
| t04_e05_p0 | 64 | 232 | 168 | 232 | 168 | 232 (missed_grasp) | 168 |
| t04_e08_p0 | 160 | 128 | -32 | 128 | -32 | 384 (stuck) | 224 |
| t04_e11_p0 | 152 | 112 | -40 | 112 | -40 | 168 (stuck) | 16 |
| t04_e12_p0 | 24 | 48 | 24 | 48 | 24 | 48 (missed_grasp) | 24 |
| t04_e13_p0 | 48 | 88 | 40 | 88 | 40 | 88 (drop) | 40 |
| t04_e15_p0 | 112 | 200 | 88 | 200 | 88 | 200 (missed_grasp) | 88 |
| t04_e16_p0 | 200 | None | None | None | None | None () | None |
| t04_e21_p0 | 0 | 88 | 88 | 88 | 88 | 88 (missed_grasp) | 88 |
| t04_e32_p0 | 0 | 72 | 72 | 72 | 72 | 72 (missed_grasp) | 72 |
| t04_e35_p0 | 0 | 64 | 64 | 64 | 64 | 64 (missed_grasp) | 64 |
| t04_e39_p0 | 0 | 80 | 80 | 80 | 80 | 80 (missed_grasp) | 80 |
| t04_e41_p0 | 0 | None | None | None | None | None () | None |
| t04_e42_p0 | 160 | 64 | -96 | 64 | -96 | 280 (missed_grasp) | 120 |
| t04_e45_p0 | 0 | 72 | 72 | 72 | 72 | 72 (missed_grasp) | 72 |
| t04_e47_p0 | 88 | 488 | 400 | None | None | 488 (stuck) | 400 |
| t04_e48_p0 | 48 | 88 | 40 | 88 | 40 | 88 (missed_grasp) | 40 |
| t04_e49_p0 | 0 | 504 | 504 | None | None | 504 (stuck) | 504 |
| t05_e20_p0 | 0 | 80 | 80 | 80 | 80 | 80 (missed_grasp) | 80 |
| t06_e04_p0 | 408 | 112 | -296 | 112 | -296 | None () | None |
| t06_e11_p0 | 104 | 184 | 80 | None | None | 184 (stuck) | 80 |
| t06_e12_p0 | 152 | 232 | 80 | 232 | 80 | 232 (missed_grasp) | 80 |
| t06_e24_p0 | 48 | 96 | 48 | 96 | 48 | 96 (missed_grasp) | 48 |
| t06_e26_p0 | 144 | 184 | 40 | 232 | 88 | 184 (stuck) | 40 |
| t06_e27_p0 | 328 | 184 | -144 | 352 | 24 | 352 (missed_grasp) | 24 |
| t06_e28_p0 | 0 | 288 | 288 | 288 | 288 | 288 (missed_grasp) | 288 |
| t06_e30_p0 | 200 | 152 | -48 | 152 | -48 | 224 (missed_grasp) | 24 |
| t06_e31_p0 | 56 | 112 | 56 | 112 | 56 | 112 (drop) | 56 |
| t06_e33_p0 | 0 | 112 | 112 | 112 | 112 | 112 (drop) | 112 |
| t06_e35_p0 | 176 | 224 | 48 | 224 | 48 | 224 (missed_grasp) | 48 |
| t06_e43_p0 | 0 | 168 | 168 | 168 | 168 | 168 (missed_grasp) | 168 |
| t06_e45_p0 | 264 | 328 | 64 | 368 | 104 | 328 (stuck) | 64 |
| t06_e46_p0 | 168 | 216 | 48 | 216 | 48 | 216 (missed_grasp) | 48 |
| t07_e03_p0 | 488 | 216 | -272 | 216 | -272 | None () | None |
| t07_e14_p0 | 512 | 88 | -424 | 88 | -424 | None () | None |
| t07_e19_p0 | 0 | 104 | 104 | 104 | 104 | 104 (missed_grasp) | 104 |
| t07_e29_p0 | 0 | 312 | 312 | 344 | 344 | 312 (stuck) | 312 |
| t07_e47_p0 | 48 | 104 | 56 | 176 | 128 | 104 (stuck) | 56 |
| t08_e04_p0 | 272 | 320 | 48 | 320 | 48 | 320 (missed_grasp) | 48 |
| t08_e08_p0 | 488 | 328 | -160 | 328 | -160 | None () | None |
| t08_e10_p0 | 88 | 312 | 224 | None | None | 312 (stuck) | 224 |
| t08_e23_p0 | 72 | 352 | 280 | None | None | 352 (stuck) | 280 |
| t08_e38_p0 | 312 | 144 | -168 | 144 | -168 | 512 (missed_grasp) | 200 |
| t00_e00_p0_s1 | 0 | 72 | 72 | 72 | 72 | 72 (wrong_object) | 72 |
| t00_e01_p0_s1 | 0 | 112 | 112 | 112 | 112 | 112 (missed_grasp) | 112 |
| t00_e01_p0_s2 | 0 | 80 | 80 | 80 | 80 | 80 (missed_grasp) | 80 |
| t00_e04_p0_s1 | 0 | 128 | 128 | 128 | 128 | 128 (wrong_object) | 128 |
| t00_e06_p0_s1 | 344 | 264 | -80 | 280 | -64 | 392 (missed_grasp) | 48 |
| t00_e08_p0_s1 | 0 | 96 | 96 | 96 | 96 | 96 (missed_grasp) | 96 |
| t00_e08_p0_s2 | 24 | 160 | 136 | 160 | 136 | 160 (missed_grasp) | 136 |
| t00_e09_p0_s1 | 32 | 280 | 248 | 280 | 248 | 280 (missed_grasp) | 248 |
| t00_e10_p0_s1 | 184 | 256 | 72 | 480 | 296 | 256 (stuck) | 72 |
| t00_e13_p0_s2 | None | 264 | None | 264 | None | None () | None |
| t00_e14_p0_s2 | 0 | 72 | 72 | 72 | 72 | 72 (wrong_object) | 72 |
| t00_e15_p0_s2 | 0 | 64 | 64 | 64 | 64 | 64 (wrong_object) | 64 |
| t00_e17_p0_s1 | 216 | 280 | 64 | 280 | 64 | 280 (missed_grasp) | 64 |
| t00_e17_p0_s2 | 352 | 192 | -160 | 264 | -88 | 424 (missed_grasp) | 72 |
| t00_e18_p0_s2 | 312 | 136 | -176 | 248 | -64 | None () | None |
| t00_e20_p0_s2 | 0 | 104 | 104 | 104 | 104 | 104 (wrong_object) | 104 |
| t00_e23_p0_s1 | 200 | 224 | 24 | 224 | 24 | 224 (missed_grasp) | 24 |
| t00_e24_p0_s1 | 0 | 64 | 64 | 64 | 64 | 64 (wrong_object) | 64 |
| t00_e26_p0_s1 | 232 | 96 | -136 | 96 | -136 | 328 (stuck) | 96 |
| t00_e27_p0_s2 | 208 | 112 | -96 | None | None | 296 (stuck) | 88 |
| t00_e28_p0_s1 | 208 | 192 | -16 | 272 | 64 | 272 (missed_grasp) | 64 |
| t00_e32_p0_s1 | 144 | 272 | 128 | 272 | 128 | 272 (missed_grasp) | 128 |
| t00_e32_p0_s2 | 0 | 88 | 88 | 88 | 88 | 88 (missed_grasp) | 88 |
| t00_e33_p0_s2 | 264 | 240 | -24 | None | None | None () | None |
| t00_e36_p0_s2 | 144 | 88 | -56 | 88 | -56 | 368 (missed_grasp) | 224 |
| t00_e39_p0_s2 | 144 | 256 | 112 | 256 | 112 | 256 (missed_grasp) | 112 |
| t00_e41_p0_s1 | 0 | 80 | 80 | 80 | 80 | 80 (wrong_object) | 80 |
| t00_e42_p0_s1 | 0 | 72 | 72 | 72 | 72 | 72 (wrong_object) | 72 |
| t00_e46_p0_s1 | 280 | 408 | 128 | 408 | 128 | 408 (missed_grasp) | 128 |
| t00_e48_p0_s1 | 0 | 64 | 64 | 64 | 64 | 64 (wrong_object) | 64 |
| t00_e49_p0_s2 | 0 | 104 | 104 | 104 | 104 | 104 (wrong_object) | 104 |
| t01_e07_p0_s1 | 136 | 112 | -24 | 160 | 24 | 160 (missed_grasp) | 24 |
| t01_e18_p0_s1 | 48 | 120 | 72 | 120 | 72 | 120 (missed_grasp) | 72 |
| t01_e25_p0_s1 | 48 | 88 | 40 | 88 | 40 | 88 (missed_grasp) | 40 |
| t01_e30_p0_s2 | 152 | 272 | 120 | 272 | 120 | 272 (missed_grasp) | 120 |
| t01_e32_p0_s1 | 152 | 248 | 96 | None | None | 248 (stuck) | 96 |
| t01_e35_p0_s2 | 128 | 128 | 0 | 208 | 80 | 128 (stuck) | 0 |
| t01_e41_p0_s2 | 152 | 232 | 80 | 232 | 80 | 232 (missed_grasp) | 80 |
| t01_e43_p0_s1 | 288 | 256 | -32 | 256 | -32 | None () | None |
| t01_e43_p0_s2 | 384 | 336 | -48 | 336 | -48 | 472 (stuck) | 88 |
| t01_e45_p0_s1 | 184 | 384 | 200 | 480 | 296 | 384 (stuck) | 200 |
| t01_e48_p0_s1 | 168 | 128 | -40 | 128 | -40 | 256 (missed_grasp) | 88 |
| t01_e48_p0_s2 | 120 | 104 | -16 | 104 | -16 | 152 (missed_grasp) | 32 |
| t04_e00_p0_s2 | 40 | 64 | 24 | 64 | 24 | 64 (missed_grasp) | 24 |
| t04_e01_p0_s2 | 80 | 432 | 352 | None | None | 432 (stuck) | 352 |
| t04_e04_p0_s2 | 152 | 256 | 104 | 256 | 104 | 256 (missed_grasp) | 104 |
| t04_e21_p0_s1 | 80 | 464 | 384 | None | None | 464 (stuck) | 384 |
| t04_e24_p0_s2 | 0 | 120 | 120 | 120 | 120 | 120 (missed_grasp) | 120 |
| t04_e33_p0_s1 | 120 | 200 | 80 | 200 | 80 | 200 (missed_grasp) | 80 |
| t04_e33_p0_s2 | 0 | 56 | 56 | 56 | 56 | 56 (missed_grasp) | 56 |
| t04_e41_p0_s2 | 72 | 56 | -16 | 56 | -16 | None () | None |
| t04_e42_p0_s1 | 0 | 80 | 80 | 80 | 80 | 80 (missed_grasp) | 80 |
| t04_e45_p0_s2 | 160 | 104 | -56 | 104 | -56 | 192 (missed_grasp) | 32 |
| t04_e48_p0_s1 | 72 | 144 | 72 | 144 | 72 | 144 (missed_grasp) | 72 |
| t07_e08_p0_s1 | 64 | 120 | 56 | 120 | 56 | 120 (missed_grasp) | 56 |
| t07_e09_p0_s2 | 0 | 64 | 64 | 64 | 64 | 64 (missed_grasp) | 64 |
| t07_e10_p0_s1 | 72 | 80 | 8 | 80 | 8 | 80 (missed_grasp) | 8 |
| t07_e28_p0_s1 | 0 | 72 | 72 | 72 | 72 | 72 (missed_grasp) | 72 |
| t07_e29_p0_s1 | 0 | 80 | 80 | 80 | 80 | 80 (missed_grasp) | 80 |
| t07_e33_p0_s1 | 0 | 488 | 488 | None | None | 488 (stuck) | 488 |
| t07_e33_p0_s2 | 0 | 288 | 288 | None | None | 288 (stuck) | 288 |
| t07_e34_p0_s1 | 48 | 88 | 40 | 88 | 40 | 88 (missed_grasp) | 40 |
| t07_e43_p0_s1 | 432 | 112 | -320 | 232 | -200 | None () | None |

Failures with a t_pnr: 136 of 151 scanned (50 doomed from start). With an event at or after t_pnr: 117. Onset before t_pnr (window < 0): onset_any 35, onset_strict 24.
