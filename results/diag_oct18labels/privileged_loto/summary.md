# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 28; doomed from start (t_pnr 0, left out of timing): 3. Training and test use all natural successes. Threshold: conformal, alpha 0.05, from cross-fitted scores of all training-task successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| privileged | 0 of 14 | 0.032 (of 472) | 0.684 | 0.504 | 11 | 0.00 | 0 | 0 | 11 | nan | nan | nan |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- privileged t00_e08_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.999)
- privileged t00_e14_n0: t_pnr 368 -> t_alarm None (lead None, threshold 0.999)
- privileged t00_e27_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.999)
- privileged t00_e42_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.999)
- privileged t01_e41_n0: t_pnr 152 -> t_alarm None (lead None, threshold 0.997)
- privileged t02_e10_n0: t_pnr 184 -> t_alarm None (lead None, threshold 0.962)
- privileged t03_e37_n0: t_pnr None -> t_alarm None (lead None, threshold 0.979)
- privileged t03_e43_n0: t_pnr None -> t_alarm None (lead None, threshold 0.979)
- privileged t04_e11_n0: t_pnr 176 -> t_alarm None (lead None, threshold 0.971)
- privileged t06_e20_n0: t_pnr None -> t_alarm None (lead None, threshold 0.999)
- privileged t06_e23_n0: t_pnr 432 -> t_alarm None (lead None, threshold 0.999)
- privileged t06_e25_n0: t_pnr 392 -> t_alarm None (lead None, threshold 0.999)
- privileged t06_e26_n0: t_pnr 376 -> t_alarm None (lead None, threshold 0.999)
- privileged t06_e27_n0: t_pnr 472 -> t_alarm None (lead None, threshold 0.999)
- privileged t06_e28_n0: t_pnr None -> t_alarm None (lead None, threshold 0.999)
- privileged t08_e04_n0: t_pnr 488 -> t_alarm None (lead None, threshold 0.983)
- privileged t08_e06_n0: t_pnr None -> t_alarm None (lead None, threshold 0.983)
- privileged t08_e08_n0: t_pnr None -> t_alarm None (lead None, threshold 0.983)
- privileged t08_e11_n0: t_pnr None -> t_alarm None (lead None, threshold 0.983)
- privileged t08_e12_n0: t_pnr None -> t_alarm None (lead None, threshold 0.983)
- privileged t08_e20_n0: t_pnr None -> t_alarm None (lead None, threshold 0.983)
- privileged t08_e27_n0: t_pnr None -> t_alarm None (lead None, threshold 0.983)
- privileged t08_e30_n0: t_pnr None -> t_alarm None (lead None, threshold 0.983)
- privileged t08_e38_n0: t_pnr 232 -> t_alarm None (lead None, threshold 0.983)
- privileged t08_e45_n0: t_pnr None -> t_alarm None (lead None, threshold 0.983)
- privileged t08_e47_n0: t_pnr None -> t_alarm None (lead None, threshold 0.983)
- privileged t09_e25_n0: t_pnr 192 -> t_alarm None (lead None, threshold 0.972)
- privileged t09_e34_n0: t_pnr None -> t_alarm None (lead None, threshold 0.972)
