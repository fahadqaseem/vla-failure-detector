# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 167; doomed from start (t_pnr 0, left out of timing): 55. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes; perturbed: 139 labelled failures, 599 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 0 of 0 | 0.000 (of 99) | 0.822 | 0.532 | 0 | nan | 0 | 0 | 0 | nan | nan | nan |
| progress | 0 of 0 | 0.091 (of 99) | 0.615 | 0.501 | 0 | nan | 0 | 0 | 0 | nan | nan | nan |
| safe | 0 of 0 | 0.000 (of 99) | 0.930 | 0.798 | 0 | nan | 0 | 0 | 0 | nan | nan | nan |
| hideseek | 0 of 0 | 0.010 (of 99) | 0.867 | 0.663 | 0 | nan | 0 | 0 | 0 | nan | nan | nan |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 15.0% | fixed 20.0% | fixed 25.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 15.0% | time-varying 20.0% | time-varying 25.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.010 | 0 / 0 / 0, FA 0.010 | 0 / 0 / 0, FA 0.010 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 |
| progress | 0 / 0 / 0, FA 0.020 | 0 / 0 / 0, FA 0.091 | 0 / 0 / 0, FA 0.111 | 0 / 0 / 0, FA 0.131 | 0 / 0 / 0, FA 0.141 | 0 / 0 / 0, FA 0.141 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.010 | 0 / 0 / 0, FA 0.061 | 0 / 0 / 0, FA 0.061 | 0 / 0 / 0, FA 0.061 | 0 / 0 / 0, FA 0.061 |
| safe | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.010 | 0 / 0 / 0, FA 0.010 | 0 / 0 / 0, FA 0.020 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.000 |
| hideseek | 0 / 0 / 0, FA 0.000 | 0 / 0 / 0, FA 0.010 | 0 / 0 / 0, FA 0.020 | 0 / 0 / 0, FA 0.101 | 0 / 0 / 0, FA 0.283 | 0 / 0 / 0, FA 0.465 | 0 / 0 / 0, FA 0.020 | 0 / 0 / 0, FA 0.040 | 0 / 0 / 0, FA 0.131 | 0 / 0 / 0, FA 0.202 | 0 / 0 / 0, FA 0.293 | 0 / 0 / 0, FA 0.404 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- timer t05_e20_p0: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- progress t05_e20_p0: t_pnr 0 (doomed from start) -> t_alarm 376 (lead -376, threshold 7.000)
- safe t05_e20_p0: t_pnr 0 (doomed from start) -> t_alarm 88 (lead -88, threshold 0.999)
- hideseek t05_e20_p0: t_pnr 0 (doomed from start) -> t_alarm 96 (lead -96, threshold 0.001)
