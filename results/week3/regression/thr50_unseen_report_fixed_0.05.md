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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr50/unseen | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| data/week3_reg/thr50/unseen | gru_phys | 12 of 81 (6 to 19) | 32 / 37 | -5 (-14 to +4) | +112 (44) | 15 of 1071 (0.014) | 2 of 31 | 0.000 of 472 / 0.025 of 599 |
| data/week3_reg/thr50/unseen | gru_phys_frac | 15 of 81 (9 to 22) | 37 / 29 | -2 (-10 to +6) | +84 (52) | 63 of 1071 (0.059) | 4 of 31 | 0.110 of 472 / 0.018 of 599 |
| data/week3_reg/thr50/unseen | gru_phys_ttp | 11 of 81 (5 to 17) | 38 / 32 | -6 (-14 to +2) | +120 (49) | 58 of 1071 (0.054) | 2 of 31 | 0.108 of 472 / 0.012 of 599 |
| data/week3_reg/thr50/unseen | gru_robot | 6 of 81 (2 to 11) | 23 / 52 | -11 (-19 to -3) | +208 (29) | 51 of 1071 (0.048) | 0 of 31 | 0.104 of 472 / 0.003 of 599 |
| data/week3_reg/thr50/unseen | gru_robotobj1 | 4 of 81 (1 to 8) | 29 / 48 | -13 (-21 to -6) | +112 (33) | 223 of 1071 (0.208) | 1 of 31 | 0.146 of 472 / 0.257 of 599 |
| data/week3_reg/thr50/unseen | gru_robotobj2 | 4 of 81 (1 to 8) | 27 / 50 | -13 (-21 to -6) | +104 (31) | 219 of 1071 (0.204) | 1 of 31 | 0.144 of 472 / 0.252 of 599 |
