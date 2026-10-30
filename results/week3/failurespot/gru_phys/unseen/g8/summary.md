# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 167; doomed from start (t_pnr 0, left out of timing): 55. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes; perturbed: 139 labelled failures, 599 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 12 of 16 | 0.000 (of 77) | 0.698 | 0.632 | 7 | 0.71 | 2 | 3 | 2 | -160.0 | 164.8 | 1.69 |
| gru_phys | 1 of 16 | 0.000 (of 77) | 0.570 | 0.602 | 7 | 0.00 | 0 | 0 | 7 | nan | nan | nan |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 15.0% | fixed 20.0% | fixed 25.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 15.0% | time-varying 20.0% | time-varying 25.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 2 / 3 / 2, FA 0.000 | 2 / 3 / 2, FA 0.000 | 2 / 4 / 1, FA 0.078 | 2 / 4 / 1, FA 0.117 | 2 / 4 / 1, FA 0.260 | 2 / 4 / 1, FA 0.260 | 0 / 0 / 7, FA 0.000 | 0 / 1 / 6, FA 0.000 | 1 / 4 / 2, FA 0.026 | 1 / 4 / 2, FA 0.026 | 1 / 4 / 2, FA 0.026 | 1 / 4 / 2, FA 0.026 |
| gru_phys | 0 / 0 / 7, FA 0.000 | 0 / 0 / 7, FA 0.000 | 0 / 0 / 7, FA 0.000 | 0 / 0 / 7, FA 0.000 | 0 / 1 / 6, FA 0.000 | 0 / 1 / 6, FA 0.000 | 0 / 0 / 7, FA 0.000 | 0 / 0 / 7, FA 0.000 | 0 / 0 / 7, FA 0.000 | 0 / 1 / 6, FA 0.000 | 0 / 1 / 6, FA 0.013 | 0 / 1 / 6, FA 0.013 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- progress t08_e04_n0: t_pnr 464 -> t_alarm 368 (lead 96, threshold 8.000)
- progress t08_e06_n0: t_pnr None -> t_alarm None (lead None, threshold 8.000)
- progress t08_e08_n0: t_pnr None -> t_alarm 376 (lead None, threshold 8.000)
- progress t08_e11_n0: t_pnr None -> t_alarm None (lead None, threshold 8.000)
- progress t08_e12_n0: t_pnr None -> t_alarm 424 (lead None, threshold 8.000)
- progress t08_e20_n0: t_pnr None -> t_alarm 176 (lead None, threshold 8.000)
- progress t08_e27_n0: t_pnr None -> t_alarm 432 (lead None, threshold 8.000)
- progress t08_e30_n0: t_pnr None -> t_alarm None (lead None, threshold 8.000)
- progress t08_e38_n0: t_pnr 232 -> t_alarm 392 (lead -160, threshold 8.000)
- progress t08_e45_n0: t_pnr None -> t_alarm 432 (lead None, threshold 8.000)
- progress t08_e47_n0: t_pnr None -> t_alarm 384 (lead None, threshold 8.000)
- progress t08_e04_p0: t_pnr 280 -> t_alarm None (lead None, threshold 8.000)
- progress t08_e08_p0: t_pnr 480 -> t_alarm 440 (lead 40, threshold 8.000)
- progress t08_e10_p0: t_pnr 88 -> t_alarm 320 (lead -232, threshold 8.000)
- progress t08_e12_p0: t_pnr None -> t_alarm 344 (lead None, threshold 8.000)
- progress t08_e18_p0: t_pnr None -> t_alarm 360 (lead None, threshold 8.000)
- progress t08_e23_p0: t_pnr 64 -> t_alarm 360 (lead -296, threshold 8.000)
- progress t08_e32_p0: t_pnr None -> t_alarm 360 (lead None, threshold 8.000)
- progress t08_e36_p0: t_pnr None -> t_alarm 320 (lead None, threshold 8.000)
- progress t08_e37_p0: t_pnr None -> t_alarm 376 (lead None, threshold 8.000)
- progress t08_e38_p0: t_pnr 32 -> t_alarm None (lead None, threshold 8.000)
- progress t08_e41_p0: t_pnr None -> t_alarm None (lead None, threshold 8.000)
- progress t08_e44_p0: t_pnr None -> t_alarm 424 (lead None, threshold 8.000)
- gru_phys t08_e04_n0: t_pnr 464 -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e06_n0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e08_n0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e11_n0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e12_n0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e20_n0: t_pnr None -> t_alarm 184 (lead None, threshold 0.990)
- gru_phys t08_e27_n0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e30_n0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e38_n0: t_pnr 232 -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e45_n0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e47_n0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e04_p0: t_pnr 280 -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e08_p0: t_pnr 480 -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e10_p0: t_pnr 88 -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e12_p0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e18_p0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e23_p0: t_pnr 64 -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e32_p0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e36_p0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e37_p0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e38_p0: t_pnr 32 -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e41_p0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
- gru_phys t08_e44_p0: t_pnr None -> t_alarm None (lead None, threshold 0.990)
