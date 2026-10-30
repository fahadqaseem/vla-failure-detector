# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 167; doomed from start (t_pnr 0, left out of timing): 55. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 28 labelled failures, 472 successes; perturbed: 139 labelled failures, 599 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 0 of 0 | 0.006 (of 169) | 0.687 | 0.605 | 20 | 0.65 | 1 | 12 | 7 | -192.0 | 228.3 | 5.64 |
| gru_phys | 0 of 0 | 0.000 (of 169) | 0.847 | 0.640 | 20 | 0.90 | 0 | 18 | 2 | -164.0 | 162.2 | 3.25 |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 15.0% | fixed 20.0% | fixed 25.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 15.0% | time-varying 20.0% | time-varying 25.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 0 / 7 / 13, FA 0.000 | 1 / 12 / 7, FA 0.006 | 2 / 17 / 1, FA 0.024 | 3 / 16 / 1, FA 0.041 | 3 / 16 / 1, FA 0.041 | 3 / 17 / 0, FA 0.065 | 0 / 17 / 3, FA 0.000 | 1 / 18 / 1, FA 0.024 | 2 / 17 / 1, FA 0.030 | 2 / 17 / 1, FA 0.030 | 2 / 17 / 1, FA 0.030 | 2 / 17 / 1, FA 0.030 |
| gru_phys | 0 / 17 / 3, FA 0.000 | 0 / 18 / 2, FA 0.000 | 0 / 19 / 1, FA 0.024 | 0 / 20 / 0, FA 0.260 | 0 / 20 / 0, FA 0.521 | 1 / 19 / 0, FA 0.805 | 0 / 20 / 0, FA 0.065 | 0 / 20 / 0, FA 0.444 | 1 / 19 / 0, FA 0.888 | 1 / 19 / 0, FA 1.000 | 1 / 19 / 0, FA 1.000 | 1 / 19 / 0, FA 1.000 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- progress t04_e11_n0: t_pnr 184 -> t_alarm 176 (lead 8, threshold 8.000)
- progress t04_e02_p0: t_pnr 0 (doomed from start) -> t_alarm 248 (lead -248, threshold 8.000)
- progress t04_e03_p0: t_pnr 96 -> t_alarm None (lead None, threshold 8.000)
- progress t04_e05_p0: t_pnr 16 -> t_alarm 384 (lead -368, threshold 8.000)
- progress t04_e08_p0: t_pnr 160 -> t_alarm None (lead None, threshold 8.000)
- progress t04_e11_p0: t_pnr 160 -> t_alarm 176 (lead -16, threshold 8.000)
- progress t04_e12_p0: t_pnr 8 -> t_alarm 344 (lead -336, threshold 8.000)
- progress t04_e13_p0: t_pnr 48 -> t_alarm 160 (lead -112, threshold 8.000)
- progress t04_e15_p0: t_pnr 64 -> t_alarm 400 (lead -336, threshold 8.000)
- progress t04_e16_p0: t_pnr 200 -> t_alarm None (lead None, threshold 8.000)
- progress t04_e21_p0: t_pnr 0 (doomed from start) -> t_alarm 112 (lead -112, threshold 8.000)
- progress t04_e32_p0: t_pnr 0 (doomed from start) -> t_alarm 400 (lead -400, threshold 8.000)
- progress t04_e35_p0: t_pnr 0 (doomed from start) -> t_alarm 232 (lead -232, threshold 8.000)
- progress t04_e39_p0: t_pnr 0 (doomed from start) -> t_alarm 272 (lead -272, threshold 8.000)
- progress t04_e41_p0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 8.000)
- progress t04_e42_p0: t_pnr 64 -> t_alarm 400 (lead -336, threshold 8.000)
- progress t04_e45_p0: t_pnr 0 (doomed from start) -> t_alarm 424 (lead -424, threshold 8.000)
- progress t04_e47_p0: t_pnr 88 -> t_alarm 496 (lead -408, threshold 8.000)
- progress t04_e48_p0: t_pnr 40 -> t_alarm 176 (lead -136, threshold 8.000)
- progress t04_e49_p0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 8.000)
- progress t04_e00_p0_s2: t_pnr 40 -> t_alarm 232 (lead -192, threshold 8.000)
- progress t04_e01_p0_s2: t_pnr 16 -> t_alarm 440 (lead -424, threshold 8.000)
- progress t04_e04_p0_s2: t_pnr 120 -> t_alarm None (lead None, threshold 8.000)
- progress t04_e21_p0_s1: t_pnr 24 -> t_alarm None (lead None, threshold 8.000)
- progress t04_e24_p0_s2: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 8.000)
- progress t04_e33_p0_s1: t_pnr 120 -> t_alarm 312 (lead -192, threshold 8.000)
- progress t04_e33_p0_s2: t_pnr 0 (doomed from start) -> t_alarm 208 (lead -208, threshold 8.000)
- progress t04_e41_p0_s2: t_pnr 56 -> t_alarm None (lead None, threshold 8.000)
- progress t04_e42_p0_s1: t_pnr 0 (doomed from start) -> t_alarm 248 (lead -248, threshold 8.000)
- progress t04_e45_p0_s2: t_pnr 144 -> t_alarm 248 (lead -104, threshold 8.000)
- progress t04_e48_p0_s1: t_pnr 56 -> t_alarm None (lead None, threshold 8.000)
- gru_phys t04_e11_n0: t_pnr 184 -> t_alarm 296 (lead -112, threshold 0.982)
- gru_phys t04_e02_p0: t_pnr 0 (doomed from start) -> t_alarm 176 (lead -176, threshold 0.982)
- gru_phys t04_e03_p0: t_pnr 96 -> t_alarm 224 (lead -128, threshold 0.982)
- gru_phys t04_e05_p0: t_pnr 16 -> t_alarm 232 (lead -216, threshold 0.982)
- gru_phys t04_e08_p0: t_pnr 160 -> t_alarm 280 (lead -120, threshold 0.982)
- gru_phys t04_e11_p0: t_pnr 160 -> t_alarm 296 (lead -136, threshold 0.982)
- gru_phys t04_e12_p0: t_pnr 8 -> t_alarm 192 (lead -184, threshold 0.982)
- gru_phys t04_e13_p0: t_pnr 48 -> t_alarm 280 (lead -232, threshold 0.982)
- gru_phys t04_e15_p0: t_pnr 64 -> t_alarm 272 (lead -208, threshold 0.982)
- gru_phys t04_e16_p0: t_pnr 200 -> t_alarm 256 (lead -56, threshold 0.982)
- gru_phys t04_e21_p0: t_pnr 0 (doomed from start) -> t_alarm 392 (lead -392, threshold 0.982)
- gru_phys t04_e32_p0: t_pnr 0 (doomed from start) -> t_alarm 152 (lead -152, threshold 0.982)
- gru_phys t04_e35_p0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.982)
- gru_phys t04_e39_p0: t_pnr 0 (doomed from start) -> t_alarm 200 (lead -200, threshold 0.982)
- gru_phys t04_e41_p0: t_pnr 0 (doomed from start) -> t_alarm 248 (lead -248, threshold 0.982)
- gru_phys t04_e42_p0: t_pnr 64 -> t_alarm 280 (lead -216, threshold 0.982)
- gru_phys t04_e45_p0: t_pnr 0 (doomed from start) -> t_alarm 208 (lead -208, threshold 0.982)
- gru_phys t04_e47_p0: t_pnr 88 -> t_alarm 232 (lead -144, threshold 0.982)
- gru_phys t04_e48_p0: t_pnr 40 -> t_alarm None (lead None, threshold 0.982)
- gru_phys t04_e49_p0: t_pnr 0 (doomed from start) -> t_alarm 232 (lead -232, threshold 0.982)
- gru_phys t04_e00_p0_s2: t_pnr 40 -> t_alarm None (lead None, threshold 0.982)
- gru_phys t04_e01_p0_s2: t_pnr 16 -> t_alarm 200 (lead -184, threshold 0.982)
- gru_phys t04_e04_p0_s2: t_pnr 120 -> t_alarm 288 (lead -168, threshold 0.982)
- gru_phys t04_e21_p0_s1: t_pnr 24 -> t_alarm 224 (lead -200, threshold 0.982)
- gru_phys t04_e24_p0_s2: t_pnr 0 (doomed from start) -> t_alarm 96 (lead -96, threshold 0.982)
- gru_phys t04_e33_p0_s1: t_pnr 120 -> t_alarm 208 (lead -88, threshold 0.982)
- gru_phys t04_e33_p0_s2: t_pnr 0 (doomed from start) -> t_alarm 208 (lead -208, threshold 0.982)
- gru_phys t04_e41_p0_s2: t_pnr 56 -> t_alarm 216 (lead -160, threshold 0.982)
- gru_phys t04_e42_p0_s1: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.982)
- gru_phys t04_e45_p0_s2: t_pnr 144 -> t_alarm 296 (lead -152, threshold 0.982)
- gru_phys t04_e48_p0_s1: t_pnr 56 -> t_alarm 272 (lead -216, threshold 0.982)
