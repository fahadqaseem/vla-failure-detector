# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/week3_reg/thr50/unseen | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| data/week3_reg/thr50/unseen | gru_phys | 0.014 | -112 (44) | 12 of 81 (6 to 18) | 0.014 | -136 (43) | 10 of 81 (5 to 16) |
| data/week3_reg/thr50/unseen | gru_phys_frac | 0.059 | -84 (52) | 15 of 81 (9 to 22) | 0.011 | -100 (52) | 13 of 81 (7 to 20) |
| data/week3_reg/thr50/unseen | gru_phys_ttp | 0.054 | -120 (49) | 11 of 81 (5 to 17) | 0.007 | -120 (45) | 10 of 81 (5 to 16) |
| data/week3_reg/thr50/unseen | gru_robot | 0.048 | -208 (29) | 6 of 81 (2 to 11) | 0.046 | -232 (15) | 4 of 81 (1 to 8) |
| data/week3_reg/thr50/unseen | gru_robotobj1 | 0.208 | -112 (33) | 4 of 81 (1 to 8) | 0.182 | -112 (32) | 4 of 81 (1 to 8) |
| data/week3_reg/thr50/unseen | gru_robotobj2 | 0.204 | -104 (31) | 4 of 81 (1 to 8) | 0.191 | -112 (31) | 4 of 81 (1 to 8) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr50/unseen | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| data/week3_reg/thr50/unseen | gru_phys | 10 of 81 (5 to 16) | 33 / 38 | -1 (-9 to +7) | +136 (43) | 15 of 1071 (0.014) | 2 of 31 | 0.000 of 472 / 0.025 of 599 |
| data/week3_reg/thr50/unseen | gru_phys_frac | 13 of 81 (7 to 20) | 39 / 29 | +2 (-5 to +9) | +100 (52) | 12 of 1071 (0.011) | 1 of 31 | 0.004 of 472 / 0.017 of 599 |
| data/week3_reg/thr50/unseen | gru_phys_ttp | 10 of 81 (5 to 16) | 35 / 36 | -1 (-7 to +6) | +120 (45) | 8 of 1071 (0.007) | 2 of 31 | 0.004 of 472 / 0.010 of 599 |
| data/week3_reg/thr50/unseen | gru_robot | 4 of 81 (1 to 8) | 11 / 66 | -7 (-14 to -1) | +232 (15) | 49 of 1071 (0.046) | 0 of 31 | 0.102 of 472 / 0.002 of 599 |
| data/week3_reg/thr50/unseen | gru_robotobj1 | 4 of 81 (1 to 8) | 28 / 49 | -7 (-14 to +0) | +112 (32) | 195 of 1071 (0.182) | 1 of 31 | 0.133 of 472 / 0.220 of 599 |
| data/week3_reg/thr50/unseen | gru_robotobj2 | 4 of 81 (1 to 8) | 27 / 50 | -7 (-14 to +0) | +112 (31) | 205 of 1071 (0.191) | 1 of 31 | 0.131 of 472 / 0.239 of 599 |
