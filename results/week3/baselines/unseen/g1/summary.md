# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 167; doomed from start (t_pnr 0, left out of timing): 55. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes; perturbed: 139 labelled failures, 599 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 3 of 3 | 0.000 (of 181) | 0.882 | 0.563 | 15 | 1.00 | 0 | 15 | 0 | -264.0 | 265.6 | 3.06 |
| progress | 3 of 3 | 0.000 (of 181) | 0.710 | 0.582 | 15 | 0.73 | 1 | 10 | 4 | -232.0 | 203.6 | 2.79 |
| safe | 3 of 3 | 0.801 (of 181) | 0.872 | 0.841 | 15 | 1.00 | 12 | 3 | 0 | 80.0 | 83.2 | 0.36 |
| hideseek | 3 of 3 | 0.011 (of 181) | 0.902 | 0.798 | 15 | 1.00 | 2 | 13 | 0 | -72.0 | 86.9 | 1.59 |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 15.0% | fixed 20.0% | fixed 25.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 15.0% | time-varying 20.0% | time-varying 25.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 0 / 15 / 0, FA 0.000 | 0 / 15 / 0, FA 0.000 | 0 / 15 / 0, FA 0.006 | 0 / 15 / 0, FA 0.017 | 0 / 15 / 0, FA 0.028 | 1 / 14 / 0, FA 0.039 | 0 / 15 / 0, FA 0.000 | 0 / 15 / 0, FA 0.000 | 0 / 15 / 0, FA 0.000 | 0 / 15 / 0, FA 0.000 | 0 / 15 / 0, FA 0.000 | 0 / 15 / 0, FA 0.000 |
| progress | 0 / 8 / 7, FA 0.000 | 1 / 10 / 4, FA 0.000 | 2 / 9 / 4, FA 0.000 | 2 / 11 / 2, FA 0.017 | 2 / 11 / 2, FA 0.017 | 3 / 10 / 2, FA 0.028 | 2 / 9 / 4, FA 0.000 | 2 / 10 / 3, FA 0.000 | 2 / 11 / 2, FA 0.000 | 2 / 11 / 2, FA 0.000 | 2 / 11 / 2, FA 0.000 | 2 / 11 / 2, FA 0.000 |
| safe | 8 / 7 / 0, FA 0.420 | 12 / 3 / 0, FA 0.801 | 15 / 0 / 0, FA 0.967 | 15 / 0 / 0, FA 0.983 | 15 / 0 / 0, FA 1.000 | 15 / 0 / 0, FA 1.000 | 13 / 0 / 2, FA 0.652 | 14 / 0 / 1, FA 0.768 | 14 / 0 / 1, FA 0.928 | 14 / 0 / 1, FA 0.972 | 14 / 0 / 1, FA 0.978 | 14 / 1 / 0, FA 0.989 |
| hideseek | 1 / 14 / 0, FA 0.011 | 2 / 13 / 0, FA 0.011 | 2 / 13 / 0, FA 0.017 | 2 / 13 / 0, FA 0.033 | 3 / 12 / 0, FA 0.039 | 3 / 12 / 0, FA 0.050 | 0 / 9 / 6, FA 0.022 | 1 / 13 / 1, FA 0.110 | 4 / 10 / 1, FA 0.420 | 4 / 10 / 1, FA 0.530 | 6 / 9 / 0, FA 0.641 | 12 / 3 / 0, FA 0.785 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- timer t01_e41_n0: t_pnr 152 -> t_alarm 392 (lead -240, threshold 384.000)
- timer t01_e19_p0: t_pnr None -> t_alarm 392 (lead None, threshold 384.000)
- timer t01_e31_p0: t_pnr 200 -> t_alarm 392 (lead -192, threshold 384.000)
- timer t01_e33_p0: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t01_e34_p0: t_pnr 40 -> t_alarm 392 (lead -352, threshold 384.000)
- timer t01_e40_p0: t_pnr None -> t_alarm 392 (lead None, threshold 384.000)
- timer t01_e07_p0_s1: t_pnr 120 -> t_alarm 392 (lead -272, threshold 384.000)
- timer t01_e18_p0_s1: t_pnr 48 -> t_alarm 392 (lead -344, threshold 384.000)
- timer t01_e19_p0_s2: t_pnr None -> t_alarm 392 (lead None, threshold 384.000)
- timer t01_e25_p0_s1: t_pnr 32 -> t_alarm 392 (lead -360, threshold 384.000)
- timer t01_e30_p0_s2: t_pnr 112 -> t_alarm 392 (lead -280, threshold 384.000)
- timer t01_e32_p0_s1: t_pnr 144 -> t_alarm 392 (lead -248, threshold 384.000)
- timer t01_e35_p0_s2: t_pnr 128 -> t_alarm 392 (lead -264, threshold 384.000)
- timer t01_e41_p0_s2: t_pnr 160 -> t_alarm 392 (lead -232, threshold 384.000)
- timer t01_e43_p0_s1: t_pnr 272 -> t_alarm 392 (lead -120, threshold 384.000)
- timer t01_e43_p0_s2: t_pnr 144 -> t_alarm 392 (lead -248, threshold 384.000)
- timer t01_e45_p0_s1: t_pnr 176 -> t_alarm 392 (lead -216, threshold 384.000)
- timer t01_e48_p0_s1: t_pnr 48 -> t_alarm 392 (lead -344, threshold 384.000)
- timer t01_e48_p0_s2: t_pnr 120 -> t_alarm 392 (lead -272, threshold 384.000)
- progress t01_e41_n0: t_pnr 152 -> t_alarm 424 (lead -272, threshold 8.000)
- progress t01_e19_p0: t_pnr None -> t_alarm 336 (lead None, threshold 8.000)
- progress t01_e31_p0: t_pnr 200 -> t_alarm 368 (lead -168, threshold 8.000)
- progress t01_e33_p0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 8.000)
- progress t01_e34_p0: t_pnr 40 -> t_alarm None (lead None, threshold 8.000)
- progress t01_e40_p0: t_pnr None -> t_alarm 328 (lead None, threshold 8.000)
- progress t01_e07_p0_s1: t_pnr 120 -> t_alarm 120 (lead 0, threshold 8.000)
- progress t01_e18_p0_s1: t_pnr 48 -> t_alarm 280 (lead -232, threshold 8.000)
- progress t01_e19_p0_s2: t_pnr None -> t_alarm 400 (lead None, threshold 8.000)
- progress t01_e25_p0_s1: t_pnr 32 -> t_alarm None (lead None, threshold 8.000)
- progress t01_e30_p0_s2: t_pnr 112 -> t_alarm 360 (lead -248, threshold 8.000)
- progress t01_e32_p0_s1: t_pnr 144 -> t_alarm 256 (lead -112, threshold 8.000)
- progress t01_e35_p0_s2: t_pnr 128 -> t_alarm 136 (lead -8, threshold 8.000)
- progress t01_e41_p0_s2: t_pnr 160 -> t_alarm 472 (lead -312, threshold 8.000)
- progress t01_e43_p0_s1: t_pnr 272 -> t_alarm None (lead None, threshold 8.000)
- progress t01_e43_p0_s2: t_pnr 144 -> t_alarm 480 (lead -336, threshold 8.000)
- progress t01_e45_p0_s1: t_pnr 176 -> t_alarm 392 (lead -216, threshold 8.000)
- progress t01_e48_p0_s1: t_pnr 48 -> t_alarm 384 (lead -336, threshold 8.000)
- progress t01_e48_p0_s2: t_pnr 120 -> t_alarm None (lead None, threshold 8.000)
- safe t01_e41_n0: t_pnr 152 -> t_alarm 72 (lead 80, threshold 0.995)
- safe t01_e19_p0: t_pnr None -> t_alarm 32 (lead None, threshold 0.995)
- safe t01_e31_p0: t_pnr 200 -> t_alarm 72 (lead 128, threshold 0.995)
- safe t01_e33_p0: t_pnr 0 (doomed from start) -> t_alarm 40 (lead -40, threshold 0.995)
- safe t01_e34_p0: t_pnr 40 -> t_alarm 24 (lead 16, threshold 0.995)
- safe t01_e40_p0: t_pnr None -> t_alarm 24 (lead None, threshold 0.995)
- safe t01_e07_p0_s1: t_pnr 120 -> t_alarm 40 (lead 80, threshold 0.995)
- safe t01_e18_p0_s1: t_pnr 48 -> t_alarm 64 (lead -16, threshold 0.995)
- safe t01_e19_p0_s2: t_pnr None -> t_alarm 152 (lead None, threshold 0.995)
- safe t01_e25_p0_s1: t_pnr 32 -> t_alarm 24 (lead 8, threshold 0.995)
- safe t01_e30_p0_s2: t_pnr 112 -> t_alarm 160 (lead -48, threshold 0.995)
- safe t01_e32_p0_s1: t_pnr 144 -> t_alarm 160 (lead -16, threshold 0.995)
- safe t01_e35_p0_s2: t_pnr 128 -> t_alarm 32 (lead 96, threshold 0.995)
- safe t01_e41_p0_s2: t_pnr 160 -> t_alarm 32 (lead 128, threshold 0.995)
- safe t01_e43_p0_s1: t_pnr 272 -> t_alarm 24 (lead 248, threshold 0.995)
- safe t01_e43_p0_s2: t_pnr 144 -> t_alarm 24 (lead 120, threshold 0.995)
- safe t01_e45_p0_s1: t_pnr 176 -> t_alarm 16 (lead 160, threshold 0.995)
- safe t01_e48_p0_s1: t_pnr 48 -> t_alarm 32 (lead 16, threshold 0.995)
- safe t01_e48_p0_s2: t_pnr 120 -> t_alarm 32 (lead 88, threshold 0.995)
- hideseek t01_e41_n0: t_pnr 152 -> t_alarm 248 (lead -96, threshold 0.013)
- hideseek t01_e19_p0: t_pnr None -> t_alarm 248 (lead None, threshold 0.013)
- hideseek t01_e31_p0: t_pnr 200 -> t_alarm 240 (lead -40, threshold 0.013)
- hideseek t01_e33_p0: t_pnr 0 (doomed from start) -> t_alarm 128 (lead -128, threshold 0.013)
- hideseek t01_e34_p0: t_pnr 40 -> t_alarm 224 (lead -184, threshold 0.013)
- hideseek t01_e40_p0: t_pnr None -> t_alarm 240 (lead None, threshold 0.013)
- hideseek t01_e07_p0_s1: t_pnr 120 -> t_alarm 176 (lead -56, threshold 0.013)
- hideseek t01_e18_p0_s1: t_pnr 48 -> t_alarm 104 (lead -56, threshold 0.013)
- hideseek t01_e19_p0_s2: t_pnr None -> t_alarm 264 (lead None, threshold 0.013)
- hideseek t01_e25_p0_s1: t_pnr 32 -> t_alarm 112 (lead -80, threshold 0.013)
- hideseek t01_e30_p0_s2: t_pnr 112 -> t_alarm 272 (lead -160, threshold 0.013)
- hideseek t01_e32_p0_s1: t_pnr 144 -> t_alarm 424 (lead -280, threshold 0.013)
- hideseek t01_e35_p0_s2: t_pnr 128 -> t_alarm 144 (lead -16, threshold 0.013)
- hideseek t01_e41_p0_s2: t_pnr 160 -> t_alarm 248 (lead -88, threshold 0.013)
- hideseek t01_e43_p0_s1: t_pnr 272 -> t_alarm 256 (lead 16, threshold 0.013)
- hideseek t01_e43_p0_s2: t_pnr 144 -> t_alarm 216 (lead -72, threshold 0.013)
- hideseek t01_e45_p0_s1: t_pnr 176 -> t_alarm 280 (lead -104, threshold 0.013)
- hideseek t01_e48_p0_s1: t_pnr 48 -> t_alarm 104 (lead -56, threshold 0.013)
- hideseek t01_e48_p0_s2: t_pnr 120 -> t_alarm 120 (lead 0, threshold 0.013)
