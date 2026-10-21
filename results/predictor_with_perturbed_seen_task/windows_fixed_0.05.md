# Detection window t_alarm - t_pnr (steps), results/predictor_with_perturbed_seen_task, threshold fixed 0.05

Negative = before t_pnr (timely). Doomed from start (t_pnr 0) shown, left out of medians and counts.

| episode | t_pnr | mlp | combined | gated_mlp | gated_combined | progress | safe |
|---|---|---|---|---|---|---|---|
| t00_e07_p0 | 0 (doomed) | 24 | 0 | 152 | 152 | 184 | 80 |
| t00_e08_n0 | 0 (doomed) | 264 | 0 | 328 | 328 | 360 | 272 |
| t00_e09_p0 | 24 | 16 | 16 | 88 | 88 | 128 | 64 |
| t00_e13_p0 | 0 (doomed) | 88 | 0 | 72 | 72 | missed | 80 |
| t00_e14_n0 | 288 | -128 | -128 | -200 | -200 | missed | -120 |
| t00_e18_p0 | 0 (doomed) | 72 | 64 | 440 | 440 | missed | 64 |
| t00_e20_p0 | 0 (doomed) | 248 | 144 | 464 | 464 | 504 | 248 |
| t00_e27_n0 | 0 (doomed) | 40 | 48 | 384 | 384 | 416 | 48 |
| t00_e28_p0 | 0 (doomed) | 64 | 56 | 424 | 424 | 456 | 72 |
| t00_e29_p0 | 0 (doomed) | 48 | 16 | 136 | 136 | 176 | 48 |
| t00_e32_p0 | 0 (doomed) | 24 | 0 | 176 | 176 | 208 | 40 |
| t00_e41_p0 | 0 (doomed) | 24 | 24 | 192 | 192 | 344 | 104 |
| t00_e42_n0 | 0 (doomed) | 296 | 144 | 352 | 352 | 384 | 296 |
| t00_e42_p0 | 0 (doomed) | 256 | 136 | 360 | 360 | 392 | 288 |
| t00_e43_p0 | 336 | missed | -16 | -112 | -112 | -136 | missed |
| t00_e44_p0 | 256 | 240 | 240 | -96 | -96 | -56 | 240 |
| t00_e48_p0 | 0 (doomed) | 16 | 0 | 408 | 408 | missed | 304 |
| t01_e31_p0 | 200 | -80 | -144 | 128 | 128 | 168 | 24 |
| t01_e33_p0 | 0 (doomed) | missed | 40 | missed | 408 | missed | 40 |
| t01_e34_p0 | 64 | 176 | 160 | 216 | 216 | missed | 144 |
| t01_e41_n0 | 176 | 112 | 40 | 88 | 88 | 248 | 56 |
| t02_e10_n0 | 184 | 160 | 80 | 176 | 176 | 216 | 72 |
| t04_e02_p0 | 0 (doomed) | 64 | 8 | 208 | 208 | 240 | 16 |
| t04_e03_p0 | 96 | 160 | -96 | missed | missed | missed | 168 |
| t04_e05_p0 | 64 | 112 | 112 | 160 | 160 | 320 | 144 |
| t04_e08_p0 | 160 | 184 | -160 | 8 | -8 | 224 | -120 |
| t04_e11_n0 | 184 | 136 | 32 | 0 | -48 | -8 | 136 |
| t04_e11_p0 | 152 | 96 | -136 | 8 | -16 | 24 | 160 |
| t04_e12_p0 | 24 | 56 | 16 | 280 | 280 | 312 | 24 |
| t04_e13_p0 | 48 | 296 | 120 | 72 | 72 | 104 | 296 |
| t04_e15_p0 | 112 | 88 | 96 | 104 | 104 | 288 | 176 |
| t04_e16_p0 | 200 | 40 | -24 | 224 | 224 | missed | 40 |
| t04_e21_p0 | 0 (doomed) | 136 | 80 | 72 | 72 | 112 | 8 |
| t04_e32_p0 | 0 (doomed) | 56 | 56 | 168 | 168 | 392 | 16 |
| t04_e35_p0 | 0 (doomed) | 56 | 72 | 192 | 192 | 232 | 72 |
| t04_e39_p0 | 0 (doomed) | 40 | 40 | 232 | 232 | 272 | 48 |
| t04_e41_p0 | 0 (doomed) | 136 | 176 | 496 | 496 | missed | 144 |
| t04_e42_p0 | 160 | 32 | -104 | 104 | 104 | 232 | -136 |
| t04_e45_p0 | 0 (doomed) | 8 | 80 | 384 | 384 | 424 | 80 |
| t04_e47_p0 | 88 | 168 | -24 | 208 | 208 | 400 | 168 |
| t04_e48_p0 | 48 | 40 | 16 | 88 | 88 | 120 | 48 |
| t04_e49_p0 | 0 (doomed) | 248 | 248 | 432 | 432 | missed | 256 |
| t05_e20_p0 | 0 (doomed) | 136 | 88 | 344 | 344 | 384 | 88 |
| t06_e04_p0 | 408 | -168 | -176 | -80 | -80 | -40 | -184 |
| t06_e11_p0 | 104 | 280 | -32 | 48 | 48 | 88 | 32 |
| t06_e12_p0 | 152 | 56 | -8 | 136 | 136 | 168 | 56 |
| t06_e23_n0 | 472 | 24 | -240 | -224 | -224 | -128 | -248 |
| t06_e24_p0 | 48 | 40 | 40 | 104 | 104 | 360 | 48 |
| t06_e25_n0 | 464 | missed | missed | missed | -200 | -160 | -232 |
| t06_e26_n0 | 312 | 96 | 56 | -32 | -128 | -128 | 72 |
| t06_e26_p0 | 144 | 144 | 152 | 104 | 48 | 48 | 144 |
| t06_e27_n0 | 464 | -160 | -328 | -192 | -192 | -160 | -368 |
| t06_e27_p0 | 328 | 24 | -184 | -176 | -176 | -144 | 16 |
| t06_e28_p0 | 0 (doomed) | 240 | 144 | 280 | 280 | 312 | 104 |
| t06_e30_p0 | 200 | 48 | 48 | 80 | 80 | 312 | 40 |
| t06_e31_p0 | 56 | 80 | 16 | 112 | 112 | 152 | 72 |
| t06_e33_p0 | 0 (doomed) | missed | 64 | 168 | 168 | 200 | 136 |
| t06_e35_p0 | 176 | 72 | 72 | 144 | 144 | 184 | 56 |
| t06_e43_p0 | 0 (doomed) | missed | 192 | 152 | 152 | 168 | 400 |
| t06_e45_p0 | 264 | 184 | 32 | 32 | 32 | 72 | 96 |
| t06_e46_p0 | 168 | 16 | 16 | 104 | 104 | 144 | 16 |
| t07_e03_p0 | 488 | missed | -480 | 24 | 24 | missed | -432 |
| t07_e14_p0 | 512 | missed | -432 | -424 | -424 | missed | -456 |
| t07_e19_p0 | 0 (doomed) | 144 | 144 | 328 | 328 | 368 | 104 |
| t07_e29_p0 | 0 (doomed) | 88 | 24 | 280 | 280 | 320 | 72 |
| t07_e47_p0 | 48 | 80 | -40 | 40 | 40 | 56 | 64 |
| t08_e04_n0 | 488 | missed | missed | missed | missed | -120 | -200 |
| t08_e04_p0 | 272 | 64 | 48 | 32 | 32 | missed | 0 |
| t08_e08_p0 | 488 | missed | missed | -88 | -88 | -56 | -224 |
| t08_e10_p0 | 88 | 152 | 136 | 192 | 192 | 232 | 152 |
| t08_e23_p0 | 72 | 224 | 152 | 248 | 248 | 280 | 184 |
| t08_e38_n0 | 264 | 144 | 64 | 88 | 88 | 120 | 16 |
| t08_e38_p0 | 312 | missed | -160 | missed | missed | missed | -168 |
| t09_e25_n0 | 176 | missed | missed | missed | missed | 136 | missed |
| median, t_pnr > 0 | | 84 (38 alarmed) | 16 (42 alarmed) | 88 (41 alarmed) | 76 (42 alarmed) | 124 (38 alarmed) | 48 (44 alarmed) |

Compared with safe on the 46 failures with t_pnr > 0 (earlier / same step / later / only one of them alarms / both missed):

- mlp: earlier on 9 (9 both alarm, 0 safe missed), same 9, later on 26 (20 both alarm, 6 mlp missed), both missed 2
- combined: earlier on 27 (26 both alarm, 1 safe missed), same 2, later on 16 (13 both alarm, 3 combined missed), both missed 1
- gated_mlp: earlier on 12 (11 both alarm, 1 safe missed), same 0, later on 33 (29 both alarm, 4 gated_mlp missed), both missed 1
- gated_combined: earlier on 12 (11 both alarm, 1 safe missed), same 0, later on 33 (30 both alarm, 3 gated_combined missed), both missed 1
- progress: earlier on 11 (9 both alarm, 2 safe missed), same 0, later on 35 (27 both alarm, 8 progress missed), both missed 0
