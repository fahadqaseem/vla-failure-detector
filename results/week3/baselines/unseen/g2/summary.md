# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 167; doomed from start (t_pnr 0, left out of timing): 55. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes; perturbed: 139 labelled failures, 599 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 0 of 0 | 0.000 (of 49) | 0.976 | 0.637 | 1 | 1.00 | 0 | 1 | 0 | -208.0 | 208.0 | 2.13 |
| progress | 0 of 0 | 0.000 (of 49) | 0.746 | 0.505 | 1 | 1.00 | 0 | 1 | 0 | -208.0 | 208.0 | 2.13 |
| safe | 0 of 0 | 0.000 (of 49) | 0.997 | 0.980 | 1 | 1.00 | 0 | 1 | 0 | -120.0 | 120.0 | 1.65 |
| hideseek | 0 of 0 | 0.000 (of 49) | 0.874 | 0.773 | 1 | 1.00 | 0 | 1 | 0 | -112.0 | 112.0 | 1.61 |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 15.0% | fixed 20.0% | fixed 25.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 15.0% | time-varying 20.0% | time-varying 25.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.020 | 0 / 1 / 0, FA 0.020 | 0 / 1 / 0, FA 0.061 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 |
| progress | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.265 | 0 / 1 / 0, FA 0.531 | 1 / 0 / 0, FA 0.898 | 1 / 0 / 0, FA 0.898 | 0 / 1 / 0, FA 0.041 | 0 / 1 / 0, FA 0.245 | 1 / 0 / 0, FA 0.898 | 1 / 0 / 0, FA 0.898 | 1 / 0 / 0, FA 0.898 | 1 / 0 / 0, FA 0.898 |
| safe | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 |
| hideseek | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.041 | 0 / 1 / 0, FA 0.122 | 0 / 1 / 0, FA 0.633 | 0 / 1 / 0, FA 0.939 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.041 | 0 / 1 / 0, FA 0.224 | 1 / 0 / 0, FA 1.000 | 1 / 0 / 0, FA 1.000 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- timer t02_e10_n0: t_pnr 184 -> t_alarm 392 (lead -208, threshold 384.000)
- progress t02_e10_n0: t_pnr 184 -> t_alarm 392 (lead -208, threshold 7.000)
- safe t02_e10_n0: t_pnr 184 -> t_alarm 304 (lead -120, threshold 0.999)
- hideseek t02_e10_n0: t_pnr 184 -> t_alarm 296 (lead -112, threshold 0.015)
