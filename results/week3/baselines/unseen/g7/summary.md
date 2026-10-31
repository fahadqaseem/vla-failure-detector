# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 167; doomed from start (t_pnr 0, left out of timing): 55. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes; perturbed: 139 labelled failures, 599 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 0 of 0 | 0.022 (of 186) | 0.784 | 0.529 | 7 | 1.00 | 2 | 5 | 0 | -320.0 | 233.1 | 5.44 |
| progress | 0 of 0 | 0.038 (of 186) | 0.616 | 0.552 | 7 | 0.57 | 2 | 2 | 3 | 28.0 | 216.0 | 1.33 |
| safe | 0 of 0 | 0.011 (of 186) | 0.925 | 0.915 | 7 | 1.00 | 2 | 5 | 0 | -88.0 | 172.6 | 2.17 |
| hideseek | 0 of 0 | 0.032 (of 186) | 0.949 | 0.935 | 7 | 0.86 | 3 | 3 | 1 | 32.0 | 232.0 | 1.45 |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 15.0% | fixed 20.0% | fixed 25.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 15.0% | time-varying 20.0% | time-varying 25.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 2 / 5 / 0, FA 0.016 | 2 / 5 / 0, FA 0.022 | 2 / 5 / 0, FA 0.027 | 2 / 5 / 0, FA 0.070 | 2 / 5 / 0, FA 0.129 | 2 / 5 / 0, FA 0.204 | 1 / 6 / 0, FA 0.016 | 1 / 6 / 0, FA 0.016 | 1 / 6 / 0, FA 0.016 | 1 / 6 / 0, FA 0.016 | 1 / 6 / 0, FA 0.016 | 1 / 6 / 0, FA 0.016 |
| progress | 1 / 1 / 5, FA 0.032 | 2 / 2 / 3, FA 0.038 | 2 / 3 / 2, FA 0.102 | 2 / 4 / 1, FA 0.129 | 2 / 4 / 1, FA 0.247 | 2 / 4 / 1, FA 0.247 | 2 / 2 / 3, FA 0.048 | 2 / 2 / 3, FA 0.054 | 2 / 2 / 3, FA 0.091 | 2 / 2 / 3, FA 0.102 | 2 / 2 / 3, FA 0.102 | 2 / 2 / 3, FA 0.102 |
| safe | 2 / 3 / 2, FA 0.005 | 2 / 5 / 0, FA 0.011 | 2 / 5 / 0, FA 0.016 | 2 / 5 / 0, FA 0.027 | 3 / 4 / 0, FA 0.032 | 5 / 2 / 0, FA 0.097 | 2 / 5 / 0, FA 0.016 | 2 / 5 / 0, FA 0.032 | 2 / 5 / 0, FA 0.075 | 2 / 5 / 0, FA 0.075 | 4 / 3 / 0, FA 0.081 | 4 / 3 / 0, FA 0.102 |
| hideseek | 3 / 3 / 1, FA 0.022 | 3 / 3 / 1, FA 0.032 | 3 / 4 / 0, FA 0.054 | 3 / 4 / 0, FA 0.054 | 3 / 4 / 0, FA 0.054 | 3 / 4 / 0, FA 0.054 | 3 / 2 / 2, FA 0.016 | 3 / 4 / 0, FA 0.032 | 3 / 4 / 0, FA 0.038 | 3 / 4 / 0, FA 0.043 | 4 / 3 / 0, FA 0.043 | 4 / 3 / 0, FA 0.054 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- timer t07_e03_p0: t_pnr 416 -> t_alarm 392 (lead 24, threshold 384.000)
- timer t07_e14_p0: t_pnr 504 -> t_alarm 392 (lead 112, threshold 384.000)
- timer t07_e19_p0: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t07_e29_p0: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t07_e47_p0: t_pnr 48 -> t_alarm 392 (lead -344, threshold 384.000)
- timer t07_e08_p0_s1: t_pnr 72 -> t_alarm 392 (lead -320, threshold 384.000)
- timer t07_e09_p0_s2: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t07_e10_p0_s1: t_pnr 72 -> t_alarm 392 (lead -320, threshold 384.000)
- timer t07_e28_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t07_e29_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t07_e33_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t07_e33_p0_s2: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- timer t07_e34_p0_s1: t_pnr 48 -> t_alarm 392 (lead -344, threshold 384.000)
- timer t07_e43_p0_s1: t_pnr 224 -> t_alarm 392 (lead -168, threshold 384.000)
- progress t07_e03_p0: t_pnr 416 -> t_alarm None (lead None, threshold 7.000)
- progress t07_e14_p0: t_pnr 504 -> t_alarm 120 (lead 384, threshold 7.000)
- progress t07_e19_p0: t_pnr 0 (doomed from start) -> t_alarm 360 (lead -360, threshold 7.000)
- progress t07_e29_p0: t_pnr 0 (doomed from start) -> t_alarm 312 (lead -312, threshold 7.000)
- progress t07_e47_p0: t_pnr 48 -> t_alarm 104 (lead -56, threshold 7.000)
- progress t07_e08_p0_s1: t_pnr 72 -> t_alarm None (lead None, threshold 7.000)
- progress t07_e09_p0_s2: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 7.000)
- progress t07_e10_p0_s1: t_pnr 72 -> t_alarm None (lead None, threshold 7.000)
- progress t07_e28_p0_s1: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 7.000)
- progress t07_e29_p0_s1: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 7.000)
- progress t07_e33_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 488 (lead -488, threshold 7.000)
- progress t07_e33_p0_s2: t_pnr 0 (doomed from start) -> t_alarm 288 (lead -288, threshold 7.000)
- progress t07_e34_p0_s1: t_pnr 48 -> t_alarm 360 (lead -312, threshold 7.000)
- progress t07_e43_p0_s1: t_pnr 224 -> t_alarm 112 (lead 112, threshold 7.000)
- safe t07_e03_p0: t_pnr 416 -> t_alarm 168 (lead 248, threshold 1.000)
- safe t07_e14_p0: t_pnr 504 -> t_alarm 272 (lead 232, threshold 1.000)
- safe t07_e19_p0: t_pnr 0 (doomed from start) -> t_alarm 152 (lead -152, threshold 1.000)
- safe t07_e29_p0: t_pnr 0 (doomed from start) -> t_alarm 216 (lead -216, threshold 1.000)
- safe t07_e47_p0: t_pnr 48 -> t_alarm 136 (lead -88, threshold 1.000)
- safe t07_e08_p0_s1: t_pnr 72 -> t_alarm 168 (lead -96, threshold 1.000)
- safe t07_e09_p0_s2: t_pnr 0 (doomed from start) -> t_alarm 88 (lead -88, threshold 1.000)
- safe t07_e10_p0_s1: t_pnr 72 -> t_alarm 304 (lead -232, threshold 1.000)
- safe t07_e28_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 128 (lead -128, threshold 1.000)
- safe t07_e29_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 304 (lead -304, threshold 1.000)
- safe t07_e33_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 160 (lead -160, threshold 1.000)
- safe t07_e33_p0_s2: t_pnr 0 (doomed from start) -> t_alarm 152 (lead -152, threshold 1.000)
- safe t07_e34_p0_s1: t_pnr 48 -> t_alarm 104 (lead -56, threshold 1.000)
- safe t07_e43_p0_s1: t_pnr 224 -> t_alarm 480 (lead -256, threshold 1.000)
- hideseek t07_e03_p0: t_pnr 416 -> t_alarm 88 (lead 328, threshold 0.018)
- hideseek t07_e14_p0: t_pnr 504 -> t_alarm 88 (lead 416, threshold 0.018)
- hideseek t07_e19_p0: t_pnr 0 (doomed from start) -> t_alarm 136 (lead -136, threshold 0.018)
- hideseek t07_e29_p0: t_pnr 0 (doomed from start) -> t_alarm 72 (lead -72, threshold 0.018)
- hideseek t07_e47_p0: t_pnr 48 -> t_alarm 136 (lead -88, threshold 0.018)
- hideseek t07_e08_p0_s1: t_pnr 72 -> t_alarm None (lead None, threshold 0.018)
- hideseek t07_e09_p0_s2: t_pnr 0 (doomed from start) -> t_alarm 104 (lead -104, threshold 0.018)
- hideseek t07_e10_p0_s1: t_pnr 72 -> t_alarm 424 (lead -352, threshold 0.018)
- hideseek t07_e28_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 256 (lead -256, threshold 0.018)
- hideseek t07_e29_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 376 (lead -376, threshold 0.018)
- hideseek t07_e33_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 152 (lead -152, threshold 0.018)
- hideseek t07_e33_p0_s2: t_pnr 0 (doomed from start) -> t_alarm 136 (lead -136, threshold 0.018)
- hideseek t07_e34_p0_s1: t_pnr 48 -> t_alarm 120 (lead -72, threshold 0.018)
- hideseek t07_e43_p0_s1: t_pnr 224 -> t_alarm 88 (lead 136, threshold 0.018)
