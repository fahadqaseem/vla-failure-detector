# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 167; doomed from start (t_pnr 0, left out of timing): 55. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes; perturbed: 139 labelled failures, 599 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 1 of 1 | 0.083 (of 48) | 0.889 | 0.642 | 1 | 1.00 | 0 | 1 | 0 | -120.0 | 120.0 | 1.65 |
| gru_phys | 0 of 1 | 0.000 (of 48) | 0.846 | 0.179 | 1 | 0.00 | 0 | 0 | 1 | nan | nan | nan |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 15.0% | fixed 20.0% | fixed 25.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 15.0% | time-varying 20.0% | time-varying 25.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 0 / 1 / 0, FA 0.042 | 0 / 1 / 0, FA 0.083 | 1 / 0 / 0, FA 0.104 | 1 / 0 / 0, FA 0.104 | 1 / 0 / 0, FA 0.125 | 1 / 0 / 0, FA 0.125 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 1 / 0 / 0, FA 0.083 | 1 / 0 / 0, FA 0.083 | 1 / 0 / 0, FA 0.083 | 1 / 0 / 0, FA 0.083 |
| gru_phys | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.021 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- progress t09_e25_n0: t_pnr 184 -> t_alarm 304 (lead -120, threshold 7.000)
- progress t09_e34_n0: t_pnr None -> t_alarm 248 (lead None, threshold 7.000)
- gru_phys t09_e25_n0: t_pnr 184 -> t_alarm None (lead None, threshold 0.991)
- gru_phys t09_e34_n0: t_pnr None -> t_alarm None (lead None, threshold 0.991)
