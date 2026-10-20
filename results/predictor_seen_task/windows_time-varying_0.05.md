# Detection window t_alarm - t_pnr (steps), results/predictor_seen_task, threshold time-varying 0.05

Negative = before t_pnr (timely). Doomed from start (t_pnr 0) shown, left out of medians and counts.

| episode | t_pnr | mlp | combined | mlp_reg | combined_reg | progress | safe |
|---|---|---|---|---|---|---|---|
| t00_e08_n0 | 0 (doomed) | 0 | 0 | 16 | 24 | 392 | missed |
| t00_e14_n0 | 288 | -288 | -288 | -32 | -120 | -184 | missed |
| t00_e27_n0 | 0 (doomed) | 40 | 24 | 344 | 48 | missed | 40 |
| t00_e42_n0 | 0 (doomed) | 0 | 0 | 320 | 336 | missed | missed |
| t01_e41_n0 | 176 | 72 | 112 | 80 | 104 | missed | missed |
| t02_e10_n0 | 184 | 80 | missed | 152 | 144 | missed | missed |
| t04_e11_n0 | 184 | 216 | 152 | missed | missed | -16 | missed |
| t06_e23_n0 | 472 | missed | -240 | -208 | -232 | -96 | missed |
| t06_e25_n0 | 464 | missed | missed | missed | missed | -40 | missed |
| t06_e26_n0 | 312 | 96 | 136 | 104 | missed | -136 | missed |
| t06_e27_n0 | 464 | -200 | -160 | missed | missed | 8 | missed |
| t08_e04_n0 | 488 | 8 | 16 | 16 | 8 | -104 | -488 |
| t08_e38_n0 | 264 | 48 | 80 | missed | 208 | 152 | missed |
| t09_e25_n0 | 176 | missed | missed | missed | missed | 8 | missed |
| median, t_pnr > 0 | | 60 (8 alarmed) | 48 (8 alarmed) | 48 (6 alarmed) | 56 (6 alarmed) | -40 (9 alarmed) | -488 (1 alarmed) |

Compared with safe on the 11 failures with t_pnr > 0 (earlier / same step / later / only one of them alarms / both missed):

- mlp: earlier on 7 (0 both alarm, 7 safe missed), same 0, later on 1 (1 both alarm, 0 mlp missed), both missed 3
- combined: earlier on 7 (0 both alarm, 7 safe missed), same 0, later on 1 (1 both alarm, 0 combined missed), both missed 3
- mlp_reg: earlier on 5 (0 both alarm, 5 safe missed), same 0, later on 1 (1 both alarm, 0 mlp_reg missed), both missed 5
- combined_reg: earlier on 5 (0 both alarm, 5 safe missed), same 0, later on 1 (1 both alarm, 0 combined_reg missed), both missed 5
- progress: earlier on 8 (0 both alarm, 8 safe missed), same 0, later on 1 (1 both alarm, 0 progress missed), both missed 2
