# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 3; doomed from start (t_pnr 0, left out of timing): 1. Training and test use all natural successes. Threshold: conformal, alpha 0.05, from cross-fitted scores of all training-task successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0.

| model | per-step AUROC | false alarms on successes | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta | alarms on recoverable failures |
|---|---|---|---|---|---|---|---|---|---|---|---|
| timer | 0.857 | 0.091 (of 472) | 2 | 1.00 | 0 | 2 | 0 | -224.0 | 224.0 | 2.35 | 0 of 0 |
| progress | 0.711 | 0.049 (of 472) | 2 | 1.00 | 0 | 2 | 0 | -244.0 | 244.0 | 2.48 | 0 of 0 |
| safe | 0.792 | 0.051 (of 472) | 2 | 1.00 | 0 | 2 | 0 | -116.0 | 116.0 | 1.71 | 0 of 0 |
| logreg | 0.807 | 0.104 (of 472) | 2 | 0.50 | 1 | 0 | 1 | 120.0 | 120.0 | 0.21 | 0 of 0 |
| mlp | 0.826 | 0.104 (of 472) | 2 | 0.50 | 1 | 0 | 1 | 120.0 | 120.0 | 0.21 | 0 of 0 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- timer t00_e08_n0: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 384.000)
- progress t00_e08_n0: t_pnr 0 (doomed from start) -> t_alarm 360 (lead -360, threshold 7.000)
- safe t00_e08_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.996)
- logreg t00_e08_n0: t_pnr 0 (doomed from start) -> t_alarm 328 (lead -328, threshold 0.909)
- mlp t00_e08_n0: t_pnr 0 (doomed from start) -> t_alarm 400 (lead -400, threshold 0.431)
- timer t01_e41_n0: t_pnr 152 -> t_alarm 392 (lead -240, threshold 384.000)
- progress t01_e41_n0: t_pnr 152 -> t_alarm 424 (lead -272, threshold 8.000)
- safe t01_e41_n0: t_pnr 152 -> t_alarm 288 (lead -136, threshold 0.998)
- logreg t01_e41_n0: t_pnr 152 -> t_alarm 32 (lead 120, threshold 0.951)
- mlp t01_e41_n0: t_pnr 152 -> t_alarm 32 (lead 120, threshold 0.799)
- timer t02_e10_n0: t_pnr 184 -> t_alarm 392 (lead -208, threshold 384.000)
- progress t02_e10_n0: t_pnr 184 -> t_alarm 400 (lead -216, threshold 8.000)
- safe t02_e10_n0: t_pnr 184 -> t_alarm 280 (lead -96, threshold 0.999)
- logreg t02_e10_n0: t_pnr 184 -> t_alarm None (lead None, threshold 0.992)
- mlp t02_e10_n0: t_pnr 184 -> t_alarm None (lead None, threshold 0.994)
