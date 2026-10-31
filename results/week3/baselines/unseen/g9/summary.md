# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 167; doomed from start (t_pnr 0, left out of timing): 55. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes; perturbed: 139 labelled failures, 599 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 1 of 1 | 0.021 (of 48) | 0.946 | 0.593 | 1 | 1.00 | 0 | 1 | 0 | -208.0 | 208.0 | 2.13 |
| progress | 1 of 1 | 0.083 (of 48) | 0.889 | 0.642 | 1 | 1.00 | 0 | 1 | 0 | -120.0 | 120.0 | 1.65 |
| safe | 1 of 1 | 0.042 (of 48) | 0.663 | 0.673 | 1 | 0.00 | 0 | 0 | 1 | nan | nan | nan |
| hideseek | 1 of 1 | 0.354 (of 48) | 0.379 | 0.010 | 1 | 0.00 | 0 | 0 | 1 | nan | nan | nan |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 15.0% | fixed 20.0% | fixed 25.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 15.0% | time-varying 20.0% | time-varying 25.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.021 | 0 / 1 / 0, FA 0.042 | 0 / 1 / 0, FA 0.125 | 0 / 1 / 0, FA 0.208 | 0 / 1 / 0, FA 0.312 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.083 | 0 / 1 / 0, FA 0.083 | 0 / 1 / 0, FA 0.083 |
| progress | 0 / 1 / 0, FA 0.042 | 0 / 1 / 0, FA 0.083 | 1 / 0 / 0, FA 0.104 | 1 / 0 / 0, FA 0.104 | 1 / 0 / 0, FA 0.125 | 1 / 0 / 0, FA 0.125 | 0 / 1 / 0, FA 0.000 | 0 / 1 / 0, FA 0.000 | 1 / 0 / 0, FA 0.083 | 1 / 0 / 0, FA 0.083 | 1 / 0 / 0, FA 0.083 | 1 / 0 / 0, FA 0.083 |
| safe | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.042 | 0 / 0 / 1, FA 0.062 | 0 / 0 / 1, FA 0.062 | 0 / 0 / 1, FA 0.104 | 1 / 0 / 0, FA 0.271 | 0 / 0 / 1, FA 0.104 | 0 / 0 / 1, FA 0.188 | 0 / 0 / 1, FA 0.229 | 0 / 0 / 1, FA 0.250 | 1 / 0 / 0, FA 0.333 | 1 / 0 / 0, FA 0.396 |
| hideseek | 0 / 0 / 1, FA 0.167 | 0 / 0 / 1, FA 0.354 | 0 / 0 / 1, FA 0.958 | 0 / 0 / 1, FA 1.000 | 1 / 0 / 0, FA 1.000 | 1 / 0 / 0, FA 1.000 | 0 / 0 / 1, FA 0.000 | 0 / 0 / 1, FA 0.062 | 0 / 0 / 1, FA 0.979 | 1 / 0 / 0, FA 1.000 | 1 / 0 / 0, FA 1.000 | 1 / 0 / 0, FA 1.000 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- timer t09_e25_n0: t_pnr 184 -> t_alarm 392 (lead -208, threshold 384.000)
- timer t09_e34_n0: t_pnr None -> t_alarm 392 (lead None, threshold 384.000)
- progress t09_e25_n0: t_pnr 184 -> t_alarm 304 (lead -120, threshold 7.000)
- progress t09_e34_n0: t_pnr None -> t_alarm 248 (lead None, threshold 7.000)
- safe t09_e25_n0: t_pnr 184 -> t_alarm None (lead None, threshold 0.999)
- safe t09_e34_n0: t_pnr None -> t_alarm 272 (lead None, threshold 0.999)
- hideseek t09_e25_n0: t_pnr 184 -> t_alarm None (lead None, threshold 0.007)
- hideseek t09_e34_n0: t_pnr None -> t_alarm 216 (lead None, threshold 0.007)
