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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr80/unseen | progress | 29 of 102 (20 to 38) | 45 / 28 |  | +96 (74) | 51 of 1071 (0.048) | 35 of 39 | 0.049 of 472 / 0.047 of 599 |
| data/week3_reg/thr80/unseen | gru_phys | 19 of 102 (12 to 27) | 23 / 60 | -10 (-20 to +0) | +52 (42) | 48 of 1071 (0.045) | 6 of 39 | 0.017 of 472 / 0.067 of 599 |
| data/week3_reg/thr80/unseen | gru_phys_frac | 27 of 102 (18 to 36) | 53 / 22 | -2 (-12 to +8) | +48 (80) | 33 of 1071 (0.031) | 12 of 39 | 0.015 of 472 / 0.043 of 599 |
| data/week3_reg/thr80/unseen | gru_phys_ttp | 24 of 102 (16 to 33) | 51 / 27 | -5 (-15 to +5) | +56 (75) | 27 of 1071 (0.025) | 8 of 39 | 0.006 of 472 / 0.040 of 599 |
| data/week3_reg/thr80/unseen | gru_robot | 6 of 102 (2 to 11) | 12 / 84 | -23 (-33 to -13) | +72 (18) | 40 of 1071 (0.037) | 4 of 39 | 0.078 of 472 / 0.005 of 599 |
| data/week3_reg/thr80/unseen | gru_robotobj1 | 9 of 102 (4 to 15) | 27 / 66 | -20 (-30 to -9) | +48 (36) | 174 of 1071 (0.162) | 3 of 39 | 0.106 of 472 / 0.207 of 599 |
| data/week3_reg/thr80/unseen | gru_robotobj2 | 9 of 102 (4 to 15) | 27 / 66 | -20 (-30 to -9) | +60 (36) | 173 of 1071 (0.162) | 3 of 39 | 0.104 of 472 / 0.207 of 599 |
