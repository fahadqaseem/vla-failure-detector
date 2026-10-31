# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/week3_reg/thr80/unseen | progress | 0.048 | -96 (74) | 29 of 102 (20 to 38) | 0.025 | -144 (57) | 17 of 102 (10 to 25) |
| data/week3_reg/thr80/unseen | gru_phys | 0.045 | -52 (42) | 19 of 102 (12 to 27) | 0.041 | -56 (36) | 16 of 102 (9 to 23) |
| data/week3_reg/thr80/unseen | gru_phys_frac | 0.031 | -48 (80) | 27 of 102 (19 to 36) | 0.015 | -60 (70) | 23 of 102 (15 to 32) |
| data/week3_reg/thr80/unseen | gru_phys_ttp | 0.025 | -56 (75) | 24 of 102 (16 to 32) | 0.012 | -80 (63) | 20 of 102 (12 to 28) |
| data/week3_reg/thr80/unseen | gru_robot | 0.037 | -72 (18) | 6 of 102 (2 to 11) | 0.017 | -116 (16) | 3 of 102 (0 to 7) |
| data/week3_reg/thr80/unseen | gru_robotobj1 | 0.162 | -48 (36) | 9 of 102 (4 to 15) | 0.162 | -56 (35) | 8 of 102 (3 to 14) |
| data/week3_reg/thr80/unseen | gru_robotobj2 | 0.162 | -60 (36) | 9 of 102 (4 to 15) | 0.160 | -68 (36) | 8 of 102 (3 to 14) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr80/unseen | progress | 17 of 102 (10 to 24) | 40 / 45 |  | +144 (57) | 27 of 1071 (0.025) | 28 of 39 | 0.030 of 472 / 0.022 of 599 |
| data/week3_reg/thr80/unseen | gru_phys | 16 of 102 (9 to 23) | 20 / 66 | -1 (-10 to +8) | +56 (36) | 44 of 1071 (0.041) | 6 of 39 | 0.015 of 472 / 0.062 of 599 |
| data/week3_reg/thr80/unseen | gru_phys_frac | 23 of 102 (15 to 32) | 47 / 32 | +6 (-3 to +16) | +60 (70) | 16 of 1071 (0.015) | 8 of 39 | 0.002 of 472 / 0.025 of 599 |
| data/week3_reg/thr80/unseen | gru_phys_ttp | 20 of 102 (12 to 28) | 43 / 39 | +3 (-7 to +13) | +80 (63) | 13 of 1071 (0.012) | 7 of 39 | 0.002 of 472 / 0.020 of 599 |
| data/week3_reg/thr80/unseen | gru_robot | 3 of 102 (0 to 7) | 13 / 86 | -14 (-22 to -6) | +116 (16) | 18 of 1071 (0.017) | 3 of 39 | 0.032 of 472 / 0.005 of 599 |
| data/week3_reg/thr80/unseen | gru_robotobj1 | 8 of 102 (3 to 14) | 27 / 67 | -9 (-18 to +0) | +56 (35) | 173 of 1071 (0.162) | 3 of 39 | 0.104 of 472 / 0.207 of 599 |
| data/week3_reg/thr80/unseen | gru_robotobj2 | 8 of 102 (3 to 14) | 28 / 66 | -9 (-18 to +0) | +68 (36) | 171 of 1071 (0.160) | 3 of 39 | 0.104 of 472 / 0.204 of 599 |
