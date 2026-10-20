# Detection window t_alarm - t_pnr (steps), results/predictor, threshold time-varying 0.05

Negative = before t_pnr (timely). Doomed from start (t_pnr 0) shown, left out of medians and counts.

| episode | t_pnr | mlp | combined | mlp_reg | combined_reg | progress | safe |
|---|---|---|---|---|---|---|---|
| t00_e08_n0 | 0 (doomed) | 384 | 384 | 336 | 320 | missed | 320 |
| t00_e14_n0 | 288 | 32 | -120 | 112 | missed | -184 | 32 |
| t00_e27_n0 | 0 (doomed) | 64 | 64 | 360 | 88 | missed | 328 |
| t00_e42_n0 | 0 (doomed) | 376 | 376 | 336 | 328 | 512 | 320 |
| t01_e41_n0 | 176 | -144 | -136 | -152 | -160 | 240 | 144 |
| t02_e10_n0 | 184 | 80 | 80 | 144 | 136 | 216 | 136 |
| t04_e11_n0 | 184 | 152 | 144 | 144 | 144 | -16 | 136 |
| t06_e23_n0 | 472 | -152 | -136 | -160 | -200 | -136 | -152 |
| t06_e25_n0 | 464 | -208 | -208 | -192 | -192 | -144 | missed |
| t06_e26_n0 | 312 | 96 | 96 | 8 | -56 | -160 | 24 |
| t06_e27_n0 | 464 | -200 | -200 | -200 | -200 | -144 | -144 |
| t08_e04_n0 | 488 | 8 | 16 | missed | missed | missed | missed |
| t08_e38_n0 | 264 | 48 | 48 | missed | missed | missed | missed |
| t09_e25_n0 | 176 | missed | 232 | missed | missed | 8 | 144 |
| median, t_pnr > 0 | | 20 (10 alarmed) | 16 (11 alarmed) | -72 (8 alarmed) | -160 (7 alarmed) | -136 (9 alarmed) | 84 (8 alarmed) |

Compared with safe on the 11 failures with t_pnr > 0 (earlier / same step / later / only one of them alarms / both missed):

- mlp: earlier on 6 (3 both alarm, 3 safe missed), same 2, later on 3 (2 both alarm, 1 mlp missed), both missed 0
- combined: earlier on 7 (4 both alarm, 3 safe missed), same 0, later on 4 (4 both alarm, 0 combined missed), both missed 0
- mlp_reg: earlier on 5 (4 both alarm, 1 safe missed), same 0, later on 4 (3 both alarm, 1 mlp_reg missed), both missed 2
- combined_reg: earlier on 5 (4 both alarm, 1 safe missed), same 1, later on 3 (1 both alarm, 2 combined_reg missed), both missed 2
- progress: earlier on 5 (4 both alarm, 1 safe missed), same 1, later on 3 (3 both alarm, 0 progress missed), both missed 2
