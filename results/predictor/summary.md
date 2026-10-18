# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 3; doomed from start (t_pnr 0, left out of timing): 1. Successes in test sets: all natural successes. alpha 0.05, epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0.

Timely = alarm at or before t_pnr; late = after; |err| = mean |t_alarm - t_pnr| over alarmed failures.

| model | per-step AUROC | false alarms on successes | failures with t_pnr > 0 | recall | timely | late | missed | mean abs err (steps) | median eta | alarms on recoverable failures |
|---|---|---|---|---|---|---|---|---|---|---|
| timer | 0.857 | 0.087 (of 472) | 2 | 1.00 | 0 | 2 | 0 | 232.0 | 2.40 | 0 of 0 |
| safe | 0.803 | 0.210 (of 472) | 2 | 1.00 | 1 | 1 | 0 | 80.0 | 0.95 | 0 of 0 |
| logreg | 0.836 | 0.309 (of 472) | 2 | 1.00 | 1 | 1 | 0 | 116.0 | 0.86 | 0 of 0 |
| mlp | 0.863 | 0.201 (of 472) | 2 | 1.00 | 1 | 1 | 0 | 140.0 | 0.94 | 0 of 0 |

Labelled failures, per model: t_pnr -> t_alarm

- timer t00_e08_n0: t_pnr 0 (doomed from start) -> t_alarm 400 (threshold 0.754)
- safe t00_e08_n0: t_pnr 0 (doomed from start) -> t_alarm 296 (threshold 0.993)
- logreg t00_e08_n0: t_pnr 0 (doomed from start) -> t_alarm 288 (threshold 0.900)
- mlp t00_e08_n0: t_pnr 0 (doomed from start) -> t_alarm 264 (threshold 0.117)
- timer t01_e41_n0: t_pnr 152 -> t_alarm 400 (threshold 0.754)
- safe t01_e41_n0: t_pnr 152 -> t_alarm 72 (threshold 0.991)
- logreg t01_e41_n0: t_pnr 152 -> t_alarm 24 (threshold 0.897)
- mlp t01_e41_n0: t_pnr 152 -> t_alarm 16 (threshold 0.117)
- timer t02_e10_n0: t_pnr 184 -> t_alarm 400 (threshold 0.754)
- safe t02_e10_n0: t_pnr 184 -> t_alarm 264 (threshold 0.989)
- logreg t02_e10_n0: t_pnr 184 -> t_alarm 288 (threshold 0.940)
- mlp t02_e10_n0: t_pnr 184 -> t_alarm 328 (threshold 0.323)
