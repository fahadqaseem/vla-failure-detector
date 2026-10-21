# Detection window t_alarm - t_pnr (steps), results/predictor_with_perturbed, threshold fixed 0.05

Negative = before t_pnr (timely). Doomed from start (t_pnr 0) shown, left out of medians and counts.

| episode | t_pnr | mlp | combined | gated_mlp | gated_combined | progress | safe |
|---|---|---|---|---|---|---|---|
| t00_e07_p0 | 0 (doomed) | missed | 168 | 152 | 152 | 176 | 104 |
| t00_e08_n0 | 0 (doomed) | 288 | 272 | 328 | 328 | 352 | 272 |
| t00_e09_p0 | 24 | missed | missed | 88 | 88 | 112 | 136 |
| t00_e13_p0 | 0 (doomed) | 96 | 96 | 72 | 72 | missed | 96 |
| t00_e14_n0 | 288 | -48 | -8 | -200 | -200 | missed | -48 |
| t00_e18_p0 | 0 (doomed) | 104 | 128 | 440 | 440 | missed | 64 |
| t00_e20_p0 | 0 (doomed) | 256 | 256 | 464 | 464 | 488 | 272 |
| t00_e27_n0 | 0 (doomed) | 336 | 344 | 384 | 384 | 408 | 64 |
| t00_e28_p0 | 0 (doomed) | 152 | 80 | 424 | 424 | 448 | 144 |
| t00_e29_p0 | 0 (doomed) | 392 | 192 | 144 | 136 | 160 | 104 |
| t00_e32_p0 | 0 (doomed) | 152 | 48 | 176 | 176 | 200 | 72 |
| t00_e41_p0 | 0 (doomed) | 256 | 224 | 192 | 192 | 216 | 248 |
| t00_e42_n0 | 0 (doomed) | 304 | 304 | 352 | 352 | 376 | 304 |
| t00_e42_p0 | 0 (doomed) | 304 | 304 | 360 | 360 | 384 | 304 |
| t00_e43_p0 | 336 | missed | 56 | -160 | -168 | -144 | 144 |
| t00_e44_p0 | 256 | -40 | -56 | -96 | -96 | -72 | 248 |
| t00_e48_p0 | 0 (doomed) | 312 | 312 | 408 | 408 | missed | 312 |
| t01_e31_p0 | 200 | -168 | -136 | 128 | 128 | 168 | -128 |
| t01_e33_p0 | 0 (doomed) | missed | 136 | missed | missed | missed | 40 |
| t01_e34_p0 | 64 | 160 | 152 | 216 | 216 | missed | 152 |
| t01_e41_n0 | 176 | -144 | 40 | 88 | 88 | 248 | -104 |
| t02_e10_n0 | 184 | missed | missed | 168 | 168 | 216 | 144 |
| t04_e02_p0 | 0 (doomed) | missed | missed | 208 | 208 | 248 | 344 |
| t04_e03_p0 | 96 | 360 | 200 | missed | missed | missed | 344 |
| t04_e05_p0 | 64 | missed | missed | 280 | 160 | 320 | 312 |
| t04_e08_p0 | 160 | 232 | 232 | 192 | -8 | missed | missed |
| t04_e11_n0 | 184 | missed | missed | 0 | 296 | -8 | 144 |
| t04_e11_p0 | 152 | missed | 280 | -16 | -16 | 24 | missed |
| t04_e12_p0 | 24 | missed | missed | 280 | 280 | 320 | 24 |
| t04_e13_p0 | 48 | missed | missed | 120 | 120 | 112 | missed |
| t04_e15_p0 | 112 | missed | missed | 112 | 104 | 288 | missed |
| t04_e16_p0 | 200 | missed | missed | 232 | 224 | missed | missed |
| t04_e21_p0 | 0 (doomed) | missed | missed | 80 | 80 | 112 | 88 |
| t04_e32_p0 | 0 (doomed) | missed | missed | 168 | 168 | 400 | missed |
| t04_e35_p0 | 0 (doomed) | missed | missed | 192 | 192 | 232 | 248 |
| t04_e39_p0 | 0 (doomed) | 472 | missed | 232 | 232 | 272 | 96 |
| t04_e41_p0 | 0 (doomed) | missed | 448 | 504 | 496 | missed | missed |
| t04_e42_p0 | 160 | 128 | missed | 104 | 104 | 240 | 128 |
| t04_e45_p0 | 0 (doomed) | 368 | missed | 384 | 384 | 424 | 120 |
| t04_e47_p0 | 88 | missed | 416 | 208 | 208 | 408 | 376 |
| t04_e48_p0 | 48 | missed | 240 | 88 | 88 | 128 | 120 |
| t04_e49_p0 | 0 (doomed) | missed | missed | 480 | 432 | missed | missed |
| t05_e20_p0 | 0 (doomed) | missed | 144 | missed | missed | 376 | 88 |
| t06_e04_p0 | 408 | 88 | 56 | -80 | -80 | -56 | 88 |
| t06_e11_p0 | 104 | 296 | 296 | 48 | 48 | 72 | missed |
| t06_e12_p0 | 152 | 56 | 216 | 144 | 144 | 160 | 352 |
| t06_e23_n0 | 472 | missed | missed | -216 | -216 | -200 | -88 |
| t06_e24_p0 | 48 | missed | missed | 104 | 120 | 128 | missed |
| t06_e25_n0 | 464 | missed | missed | -184 | -200 | -176 | missed |
| t06_e26_n0 | 312 | 104 | missed | -8 | 136 | -144 | missed |
| t06_e26_p0 | 144 | missed | 216 | 104 | 104 | 32 | missed |
| t06_e27_n0 | 464 | -160 | -160 | -192 | -192 | -168 | -136 |
| t06_e27_p0 | 328 | missed | missed | -144 | -64 | -152 | missed |
| t06_e28_p0 | 0 (doomed) | missed | missed | 280 | 288 | 304 | missed |
| t06_e30_p0 | 200 | missed | missed | 80 | 80 | 296 | 40 |
| t06_e31_p0 | 56 | 136 | 168 | 112 | 112 | 136 | 160 |
| t06_e33_p0 | 0 (doomed) | missed | missed | 168 | 168 | 192 | missed |
| t06_e35_p0 | 176 | missed | missed | 144 | 144 | 168 | 128 |
| t06_e43_p0 | 0 (doomed) | missed | missed | 168 | 200 | 160 | 448 |
| t06_e45_p0 | 264 | missed | 224 | 32 | 32 | 56 | 208 |
| t06_e46_p0 | 168 | missed | missed | 104 | 104 | 128 | missed |
| t07_e03_p0 | 488 | missed | -392 | 24 | 24 | missed | -368 |
| t07_e14_p0 | 512 | missed | -408 | -424 | -424 | missed | -240 |
| t07_e19_p0 | 0 (doomed) | missed | 104 | 328 | 328 | 368 | 168 |
| t07_e29_p0 | 0 (doomed) | missed | 120 | 280 | 280 | 320 | 72 |
| t07_e47_p0 | 48 | missed | 80 | 48 | missed | missed | 80 |
| t08_e04_n0 | 488 | missed | missed | missed | missed | -120 | missed |
| t08_e04_p0 | 272 | 56 | 72 | 32 | 120 | missed | 96 |
| t08_e08_p0 | 488 | missed | missed | -88 | -88 | -48 | missed |
| t08_e10_p0 | 88 | missed | missed | 192 | 192 | 232 | missed |
| t08_e23_p0 | 72 | missed | missed | 248 | 248 | 288 | missed |
| t08_e38_n0 | 264 | 64 | 72 | 88 | 88 | 128 | 88 |
| t08_e38_p0 | 312 | missed | missed | missed | missed | missed | missed |
| t09_e25_n0 | 176 | missed | missed | missed | missed | 128 | missed |
| median, t_pnr > 0 | | 76 (16 alarmed) | 80 (23 alarmed) | 88 (42 alarmed) | 104 (41 alarmed) | 128 (36 alarmed) | 124 (28 alarmed) |

Compared with safe on the 46 failures with t_pnr > 0 (earlier / same step / later / only one of them alarms / both missed):

- mlp: earlier on 11 (8 both alarm, 3 safe missed), same 3, later on 17 (2 both alarm, 15 mlp missed), both missed 15
- combined: earlier on 15 (11 both alarm, 4 safe missed), same 2, later on 15 (6 both alarm, 9 combined missed), both missed 14
- gated_mlp: earlier on 33 (18 both alarm, 15 safe missed), same 1, later on 9 (8 both alarm, 1 gated_mlp missed), both missed 3
- gated_combined: earlier on 30 (15 both alarm, 15 safe missed), same 1, later on 12 (10 both alarm, 2 gated_combined missed), both missed 3
- progress: earlier on 25 (10 both alarm, 15 safe missed), same 0, later on 18 (11 both alarm, 7 progress missed), both missed 3
