# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 167; doomed from start (t_pnr 0, left out of timing): 55. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes; perturbed: 139 labelled failures, 599 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 6 of 6 | 0.027 (of 73) | 0.819 | 0.549 | 14 | 1.00 | 3 | 11 | 0 | -168.0 | 173.1 | 1.79 |
| progress | 6 of 6 | 0.137 (of 73) | 0.747 | 0.627 | 14 | 1.00 | 5 | 9 | 0 | -56.0 | 146.3 | 1.31 |
| safe | 1 of 6 | 0.027 (of 73) | 0.878 | 0.819 | 14 | 0.36 | 0 | 5 | 9 | -176.0 | 203.2 | 3.17 |
| hideseek | 4 of 6 | 0.014 (of 73) | 0.770 | 0.585 | 14 | 0.93 | 4 | 9 | 1 | -120.0 | 149.5 | 1.79 |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 15.0% | fixed 20.0% | fixed 25.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 15.0% | time-varying 20.0% | time-varying 25.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 3 / 11 / 0, FA 0.014 | 3 / 11 / 0, FA 0.027 | 3 / 11 / 0, FA 0.068 | 6 / 8 / 0, FA 0.137 | 6 / 8 / 0, FA 0.192 | 6 / 8 / 0, FA 0.192 | 1 / 13 / 0, FA 0.014 | 1 / 13 / 0, FA 0.014 | 1 / 13 / 0, FA 0.014 | 1 / 13 / 0, FA 0.014 | 1 / 13 / 0, FA 0.014 | 1 / 13 / 0, FA 0.014 |
| progress | 5 / 8 / 1, FA 0.096 | 5 / 9 / 0, FA 0.137 | 5 / 9 / 0, FA 0.178 | 6 / 8 / 0, FA 0.219 | 7 / 7 / 0, FA 0.315 | 7 / 7 / 0, FA 0.315 | 4 / 10 / 0, FA 0.082 | 6 / 8 / 0, FA 0.164 | 6 / 8 / 0, FA 0.205 | 6 / 8 / 0, FA 0.205 | 6 / 8 / 0, FA 0.205 | 6 / 8 / 0, FA 0.205 |
| safe | 0 / 3 / 11, FA 0.014 | 0 / 5 / 9, FA 0.027 | 0 / 7 / 7, FA 0.027 | 0 / 8 / 6, FA 0.041 | 2 / 9 / 3, FA 0.041 | 2 / 11 / 1, FA 0.068 | 3 / 9 / 2, FA 0.000 | 3 / 9 / 2, FA 0.000 | 3 / 9 / 2, FA 0.000 | 3 / 9 / 2, FA 0.000 | 3 / 9 / 2, FA 0.000 | 3 / 9 / 2, FA 0.014 |
| hideseek | 3 / 10 / 1, FA 0.014 | 4 / 9 / 1, FA 0.014 | 4 / 9 / 1, FA 0.014 | 4 / 9 / 1, FA 0.027 | 4 / 10 / 0, FA 0.027 | 4 / 10 / 0, FA 0.027 | 0 / 1 / 13, FA 0.000 | 2 / 5 / 7, FA 0.000 | 3 / 5 / 6, FA 0.014 | 3 / 6 / 5, FA 0.014 | 3 / 6 / 5, FA 0.027 | 3 / 7 / 4, FA 0.027 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- timer t06_e20_n0: t_pnr None -> t_alarm 392 (lead None, threshold 384.000)
- timer t06_e23_n0: t_pnr 432 -> t_alarm 392 (lead 40, threshold 384.000)
- timer t06_e25_n0: t_pnr 432 -> t_alarm 392 (lead 40, threshold 384.000)
- timer t06_e26_n0: t_pnr 320 -> t_alarm 392 (lead -72, threshold 384.000)
- timer t06_e27_n0: t_pnr 440 -> t_alarm 392 (lead 48, threshold 384.000)
- timer t06_e28_n0: t_pnr None -> t_alarm 392 (lead None, threshold 384.000)
- timer t06_e04_p0: t_pnr 328 -> t_alarm 392 (lead -64, threshold 384.000)
- timer t06_e09_p0: t_pnr None -> t_alarm 392 (lead None, threshold 384.000)
- timer t06_e11_p0: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t06_e12_p0: t_pnr 128 -> t_alarm 392 (lead -264, threshold 384.000)
- timer t06_e13_p0: t_pnr None -> t_alarm 392 (lead None, threshold 384.000)
- timer t06_e23_p0: t_pnr None -> t_alarm 392 (lead None, threshold 384.000)
- timer t06_e24_p0: t_pnr 32 -> t_alarm 392 (lead -360, threshold 384.000)
- timer t06_e26_p0: t_pnr 128 -> t_alarm 392 (lead -264, threshold 384.000)
- timer t06_e27_p0: t_pnr 328 -> t_alarm 392 (lead -64, threshold 384.000)
- timer t06_e28_p0: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t06_e30_p0: t_pnr 192 -> t_alarm 392 (lead -200, threshold 384.000)
- timer t06_e31_p0: t_pnr 56 -> t_alarm 392 (lead -336, threshold 384.000)
- timer t06_e33_p0: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t06_e35_p0: t_pnr 96 -> t_alarm 392 (lead -296, threshold 384.000)
- timer t06_e43_p0: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t06_e44_p0: t_pnr None -> t_alarm 392 (lead None, threshold 384.000)
- timer t06_e45_p0: t_pnr 256 -> t_alarm 392 (lead -136, threshold 384.000)
- timer t06_e46_p0: t_pnr 152 -> t_alarm 392 (lead -240, threshold 384.000)
- progress t06_e20_n0: t_pnr None -> t_alarm 296 (lead None, threshold 6.000)
- progress t06_e23_n0: t_pnr 432 -> t_alarm 272 (lead 160, threshold 6.000)
- progress t06_e25_n0: t_pnr 432 -> t_alarm 288 (lead 144, threshold 6.000)
- progress t06_e26_n0: t_pnr 320 -> t_alarm 168 (lead 152, threshold 6.000)
- progress t06_e27_n0: t_pnr 440 -> t_alarm 296 (lead 144, threshold 6.000)
- progress t06_e28_n0: t_pnr None -> t_alarm 288 (lead None, threshold 6.000)
- progress t06_e04_p0: t_pnr 328 -> t_alarm 352 (lead -24, threshold 6.000)
- progress t06_e09_p0: t_pnr None -> t_alarm 288 (lead None, threshold 6.000)
- progress t06_e11_p0: t_pnr 0 (doomed from start) -> t_alarm 176 (lead -176, threshold 6.000)
- progress t06_e12_p0: t_pnr 128 -> t_alarm 312 (lead -184, threshold 6.000)
- progress t06_e13_p0: t_pnr None -> t_alarm 280 (lead None, threshold 6.000)
- progress t06_e23_p0: t_pnr None -> t_alarm 280 (lead None, threshold 6.000)
- progress t06_e24_p0: t_pnr 32 -> t_alarm 176 (lead -144, threshold 6.000)
- progress t06_e26_p0: t_pnr 128 -> t_alarm 176 (lead -48, threshold 6.000)
- progress t06_e27_p0: t_pnr 328 -> t_alarm 176 (lead 152, threshold 6.000)
- progress t06_e28_p0: t_pnr 0 (doomed from start) -> t_alarm 304 (lead -304, threshold 6.000)
- progress t06_e30_p0: t_pnr 192 -> t_alarm 496 (lead -304, threshold 6.000)
- progress t06_e31_p0: t_pnr 56 -> t_alarm 192 (lead -136, threshold 6.000)
- progress t06_e33_p0: t_pnr 0 (doomed from start) -> t_alarm 192 (lead -192, threshold 6.000)
- progress t06_e35_p0: t_pnr 96 -> t_alarm 344 (lead -248, threshold 6.000)
- progress t06_e43_p0: t_pnr 0 (doomed from start) -> t_alarm 160 (lead -160, threshold 6.000)
- progress t06_e44_p0: t_pnr None -> t_alarm 256 (lead None, threshold 6.000)
- progress t06_e45_p0: t_pnr 256 -> t_alarm 320 (lead -64, threshold 6.000)
- progress t06_e46_p0: t_pnr 152 -> t_alarm 296 (lead -144, threshold 6.000)
- safe t06_e20_n0: t_pnr None -> t_alarm None (lead None, threshold 0.999)
- safe t06_e23_n0: t_pnr 432 -> t_alarm None (lead None, threshold 0.999)
- safe t06_e25_n0: t_pnr 432 -> t_alarm None (lead None, threshold 0.999)
- safe t06_e26_n0: t_pnr 320 -> t_alarm None (lead None, threshold 0.999)
- safe t06_e27_n0: t_pnr 440 -> t_alarm None (lead None, threshold 0.999)
- safe t06_e28_n0: t_pnr None -> t_alarm None (lead None, threshold 0.999)
- safe t06_e04_p0: t_pnr 328 -> t_alarm 504 (lead -176, threshold 0.999)
- safe t06_e09_p0: t_pnr None -> t_alarm None (lead None, threshold 0.999)
- safe t06_e11_p0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.999)
- safe t06_e12_p0: t_pnr 128 -> t_alarm 512 (lead -384, threshold 0.999)
- safe t06_e13_p0: t_pnr None -> t_alarm None (lead None, threshold 0.999)
- safe t06_e23_p0: t_pnr None -> t_alarm None (lead None, threshold 0.999)
- safe t06_e24_p0: t_pnr 32 -> t_alarm None (lead None, threshold 0.999)
- safe t06_e26_p0: t_pnr 128 -> t_alarm None (lead None, threshold 0.999)
- safe t06_e27_p0: t_pnr 328 -> t_alarm None (lead None, threshold 0.999)
- safe t06_e28_p0: t_pnr 0 (doomed from start) -> t_alarm 512 (lead -512, threshold 0.999)
- safe t06_e30_p0: t_pnr 192 -> t_alarm 264 (lead -72, threshold 0.999)
- safe t06_e31_p0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.999)
- safe t06_e33_p0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.999)
- safe t06_e35_p0: t_pnr 96 -> t_alarm 304 (lead -208, threshold 0.999)
- safe t06_e43_p0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.999)
- safe t06_e44_p0: t_pnr None -> t_alarm 384 (lead None, threshold 0.999)
- safe t06_e45_p0: t_pnr 256 -> t_alarm None (lead None, threshold 0.999)
- safe t06_e46_p0: t_pnr 152 -> t_alarm None (lead None, threshold 0.999)
- hideseek t06_e20_n0: t_pnr None -> t_alarm None (lead None, threshold 0.000)
- hideseek t06_e23_n0: t_pnr 432 -> t_alarm 432 (lead 0, threshold 0.000)
- hideseek t06_e25_n0: t_pnr 432 -> t_alarm 288 (lead 144, threshold 0.000)
- hideseek t06_e26_n0: t_pnr 320 -> t_alarm 480 (lead -160, threshold 0.000)
- hideseek t06_e27_n0: t_pnr 440 -> t_alarm 320 (lead 120, threshold 0.000)
- hideseek t06_e28_n0: t_pnr None -> t_alarm None (lead None, threshold 0.000)
- hideseek t06_e04_p0: t_pnr 328 -> t_alarm 288 (lead 40, threshold 0.000)
- hideseek t06_e09_p0: t_pnr None -> t_alarm 360 (lead None, threshold 0.000)
- hideseek t06_e11_p0: t_pnr 0 (doomed from start) -> t_alarm 440 (lead -440, threshold 0.000)
- hideseek t06_e12_p0: t_pnr 128 -> t_alarm 408 (lead -280, threshold 0.000)
- hideseek t06_e13_p0: t_pnr None -> t_alarm 448 (lead None, threshold 0.000)
- hideseek t06_e23_p0: t_pnr None -> t_alarm 296 (lead None, threshold 0.000)
- hideseek t06_e24_p0: t_pnr 32 -> t_alarm 120 (lead -88, threshold 0.000)
- hideseek t06_e26_p0: t_pnr 128 -> t_alarm 464 (lead -336, threshold 0.000)
- hideseek t06_e27_p0: t_pnr 328 -> t_alarm 448 (lead -120, threshold 0.000)
- hideseek t06_e28_p0: t_pnr 0 (doomed from start) -> t_alarm 360 (lead -360, threshold 0.000)
- hideseek t06_e30_p0: t_pnr 192 -> t_alarm 360 (lead -168, threshold 0.000)
- hideseek t06_e31_p0: t_pnr 56 -> t_alarm 200 (lead -144, threshold 0.000)
- hideseek t06_e33_p0: t_pnr 0 (doomed from start) -> t_alarm 240 (lead -240, threshold 0.000)
- hideseek t06_e35_p0: t_pnr 96 -> t_alarm 320 (lead -224, threshold 0.000)
- hideseek t06_e43_p0: t_pnr 0 (doomed from start) -> t_alarm 456 (lead -456, threshold 0.000)
- hideseek t06_e44_p0: t_pnr None -> t_alarm 312 (lead None, threshold 0.000)
- hideseek t06_e45_p0: t_pnr 256 -> t_alarm None (lead None, threshold 0.000)
- hideseek t06_e46_p0: t_pnr 152 -> t_alarm 272 (lead -120, threshold 0.000)
