# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 167; doomed from start (t_pnr 0, left out of timing): 55. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes; perturbed: 139 labelled failures, 599 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 3 of 3 | 0.000 (of 181) | 0.710 | 0.582 | 15 | 0.73 | 1 | 10 | 4 | -232.0 | 203.6 | 2.79 |
| gru_phys | 0 of 3 | 0.061 (of 181) | 0.820 | 0.845 | 15 | 0.67 | 5 | 5 | 5 | -8.0 | 106.4 | 1.30 |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 15.0% | fixed 20.0% | fixed 25.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 15.0% | time-varying 20.0% | time-varying 25.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 0 / 8 / 7, FA 0.000 | 1 / 10 / 4, FA 0.000 | 2 / 9 / 4, FA 0.000 | 2 / 11 / 2, FA 0.017 | 2 / 11 / 2, FA 0.017 | 3 / 10 / 2, FA 0.028 | 2 / 9 / 4, FA 0.000 | 2 / 10 / 3, FA 0.000 | 2 / 11 / 2, FA 0.000 | 2 / 11 / 2, FA 0.000 | 2 / 11 / 2, FA 0.000 | 2 / 11 / 2, FA 0.000 |
| gru_phys | 5 / 5 / 5, FA 0.061 | 5 / 5 / 5, FA 0.061 | 8 / 4 / 3, FA 0.188 | 9 / 5 / 1, FA 0.326 | 10 / 5 / 0, FA 0.481 | 11 / 4 / 0, FA 0.597 | 1 / 13 / 1, FA 0.000 | 8 / 7 / 0, FA 0.448 | 9 / 6 / 0, FA 0.586 | 12 / 3 / 0, FA 0.641 | 12 / 3 / 0, FA 0.707 | 13 / 2 / 0, FA 0.746 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

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
- gru_phys t01_e41_n0: t_pnr 152 -> t_alarm 376 (lead -224, threshold 0.995)
- gru_phys t01_e19_p0: t_pnr None -> t_alarm None (lead None, threshold 0.995)
- gru_phys t01_e31_p0: t_pnr 200 -> t_alarm None (lead None, threshold 0.995)
- gru_phys t01_e33_p0: t_pnr 0 (doomed from start) -> t_alarm 240 (lead -240, threshold 0.995)
- gru_phys t01_e34_p0: t_pnr 40 -> t_alarm None (lead None, threshold 0.995)
- gru_phys t01_e40_p0: t_pnr None -> t_alarm None (lead None, threshold 0.995)
- gru_phys t01_e07_p0_s1: t_pnr 120 -> t_alarm 96 (lead 24, threshold 0.995)
- gru_phys t01_e18_p0_s1: t_pnr 48 -> t_alarm 184 (lead -136, threshold 0.995)
- gru_phys t01_e19_p0_s2: t_pnr None -> t_alarm None (lead None, threshold 0.995)
- gru_phys t01_e25_p0_s1: t_pnr 32 -> t_alarm 96 (lead -64, threshold 0.995)
- gru_phys t01_e30_p0_s2: t_pnr 112 -> t_alarm 0 (lead 112, threshold 0.995)
- gru_phys t01_e32_p0_s1: t_pnr 144 -> t_alarm None (lead None, threshold 0.995)
- gru_phys t01_e35_p0_s2: t_pnr 128 -> t_alarm 96 (lead 32, threshold 0.995)
- gru_phys t01_e41_p0_s2: t_pnr 160 -> t_alarm 0 (lead 160, threshold 0.995)
- gru_phys t01_e43_p0_s1: t_pnr 272 -> t_alarm None (lead None, threshold 0.995)
- gru_phys t01_e43_p0_s2: t_pnr 144 -> t_alarm None (lead None, threshold 0.995)
- gru_phys t01_e45_p0_s1: t_pnr 176 -> t_alarm 0 (lead 176, threshold 0.995)
- gru_phys t01_e48_p0_s1: t_pnr 48 -> t_alarm 88 (lead -40, threshold 0.995)
- gru_phys t01_e48_p0_s2: t_pnr 120 -> t_alarm 216 (lead -96, threshold 0.995)
