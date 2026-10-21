# Detection window t_alarm - t_pnr (steps), results/predictor_seen_task_gated, threshold fixed 0.05

Negative = before t_pnr (timely). Doomed from start (t_pnr 0) shown, left out of medians and counts.

| episode | t_pnr | mlp | combined | gated_mlp | gated_combined | progress | safe |
|---|---|---|---|---|---|---|---|
| t00_e08_n0 | 0 (doomed) | 0 | 0 | 328 | 328 | 352 | 272 |
| t00_e14_n0 | 288 | -48 | -120 | -184 | -184 | missed | 32 |
| t00_e27_n0 | 0 (doomed) | 56 | 48 | 384 | 384 | 408 | 64 |
| t00_e42_n0 | 0 (doomed) | 280 | 8 | 352 | 352 | 376 | 296 |
| t01_e41_n0 | 176 | 72 | 24 | 88 | 88 | 256 | 72 |
| t02_e10_n0 | 184 | 80 | 80 | 176 | 176 | 216 | 80 |
| t04_e11_n0 | 184 | missed | 160 | 296 | 296 | 0 | 280 |
| t06_e23_n0 | 472 | missed | -240 | -224 | -224 | -200 | -248 |
| t06_e25_n0 | 464 | missed | missed | -200 | -200 | -160 | -232 |
| t06_e26_n0 | 312 | 104 | missed | 136 | 136 | -120 | 64 |
| t06_e27_n0 | 464 | -224 | -200 | -192 | -192 | -168 | -360 |
| t08_e04_n0 | 488 | 8 | missed | -160 | 0 | -112 | -200 |
| t08_e38_n0 | 264 | 48 | 80 | 88 | 88 | 112 | 0 |
| t09_e25_n0 | 176 | missed | missed | missed | 232 | 136 | missed |
| median, t_pnr > 0 | | 48 (7 alarmed) | 24 (7 alarmed) | -36 (10 alarmed) | 88 (11 alarmed) | -56 (10 alarmed) | 16 (10 alarmed) |

Compared with safe on the 11 failures with t_pnr > 0 (earlier / same step / later / only one of them alarms / both missed):

- mlp: earlier on 1 (1 both alarm, 0 safe missed), same 2, later on 7 (4 both alarm, 3 mlp missed), both missed 1
- combined: earlier on 3 (3 both alarm, 0 safe missed), same 1, later on 6 (3 both alarm, 3 combined missed), both missed 1
- gated_mlp: earlier on 1 (1 both alarm, 0 safe missed), same 0, later on 9 (9 both alarm, 0 gated_mlp missed), both missed 1
- gated_combined: earlier on 2 (1 both alarm, 1 safe missed), same 0, later on 9 (9 both alarm, 0 gated_combined missed), both missed 0
- progress: earlier on 3 (2 both alarm, 1 safe missed), same 0, later on 8 (7 both alarm, 1 progress missed), both missed 0
