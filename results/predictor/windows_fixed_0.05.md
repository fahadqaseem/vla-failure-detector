# Detection window t_alarm - t_pnr (steps), results/predictor, threshold fixed 0.05

Negative = before t_pnr (timely). Doomed from start (t_pnr 0) shown, left out of medians and counts.

| episode | t_pnr | mlp | combined | mlp_reg | combined_reg | progress | safe |
|---|---|---|---|---|---|---|---|
| t00_e08_n0 | 0 (doomed) | 264 | 264 | 336 | 312 | 360 | missed |
| t00_e14_n0 | 288 | 32 | -120 | 112 | missed | missed | missed |
| t00_e27_n0 | 0 (doomed) | 64 | 88 | 88 | 88 | 416 | 352 |
| t00_e42_n0 | 0 (doomed) | 376 | 336 | 336 | 328 | 384 | 432 |
| t01_e41_n0 | 176 | -104 | -136 | -24 | -24 | 248 | 112 |
| t02_e10_n0 | 184 | missed | missed | 184 | 184 | 216 | 96 |
| t04_e11_n0 | 184 | missed | missed | missed | missed | -8 | missed |
| t06_e23_n0 | 472 | missed | missed | missed | missed | -200 | missed |
| t06_e25_n0 | 464 | missed | missed | missed | missed | -176 | missed |
| t06_e26_n0 | 312 | missed | missed | missed | missed | -144 | missed |
| t06_e27_n0 | 464 | missed | missed | missed | missed | -168 | missed |
| t08_e04_n0 | 488 | missed | missed | missed | missed | -120 | missed |
| t08_e38_n0 | 264 | missed | missed | missed | missed | 128 | missed |
| t09_e25_n0 | 176 | missed | missed | missed | missed | 128 | missed |
| median, t_pnr > 0 | | -36 (2 alarmed) | -128 (2 alarmed) | 112 (3 alarmed) | 80 (2 alarmed) | -64 (10 alarmed) | 104 (2 alarmed) |

Compared with safe on the 11 failures with t_pnr > 0 (earlier / same step / later / only one of them alarms / both missed):

- mlp: earlier on 2 (1 both alarm, 1 safe missed), same 0, later on 1 (0 both alarm, 1 mlp missed), both missed 8
- combined: earlier on 2 (1 both alarm, 1 safe missed), same 0, later on 1 (0 both alarm, 1 combined missed), both missed 8
- mlp_reg: earlier on 2 (1 both alarm, 1 safe missed), same 0, later on 1 (1 both alarm, 0 mlp_reg missed), both missed 8
- combined_reg: earlier on 1 (1 both alarm, 0 safe missed), same 0, later on 1 (1 both alarm, 0 combined_reg missed), both missed 9
- progress: earlier on 8 (0 both alarm, 8 safe missed), same 0, later on 2 (2 both alarm, 0 progress missed), both missed 1
