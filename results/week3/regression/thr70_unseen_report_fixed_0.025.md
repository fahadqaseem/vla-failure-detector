# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/week3_reg/thr70/unseen | progress | 0.048 | -108 (68) | 22 of 91 (14 to 30) | 0.025 | -156 (50) | 13 of 91 (7 to 20) |
| data/week3_reg/thr70/unseen | gru_phys | 0.052 | -72 (53) | 19 of 91 (12 to 27) | 0.040 | -80 (47) | 17 of 91 (10 to 25) |
| data/week3_reg/thr70/unseen | gru_phys_frac | 0.017 | -68 (62) | 21 of 91 (13 to 29) | 0.009 | -88 (56) | 18 of 91 (11 to 26) |
| data/week3_reg/thr70/unseen | gru_phys_ttp | 0.018 | -80 (61) | 22 of 91 (14 to 30) | 0.007 | -96 (56) | 16 of 91 (9 to 23) |
| data/week3_reg/thr70/unseen | gru_robot | 0.048 | -104 (23) | 8 of 91 (3 to 14) | 0.043 | -120 (15) | 5 of 91 (1 to 10) |
| data/week3_reg/thr70/unseen | gru_robotobj1 | 0.176 | -88 (33) | 7 of 91 (2 to 12) | 0.174 | -88 (33) | 7 of 91 (2 to 12) |
| data/week3_reg/thr70/unseen | gru_robotobj2 | 0.181 | -88 (35) | 7 of 91 (2 to 12) | 0.175 | -88 (33) | 7 of 91 (2 to 12) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr70/unseen | progress | 13 of 91 (7 to 20) | 37 / 41 |  | +156 (50) | 27 of 1071 (0.025) | 25 of 35 | 0.030 of 472 / 0.022 of 599 |
| data/week3_reg/thr70/unseen | gru_phys | 17 of 91 (10 to 24) | 30 / 44 | +4 (-5 to +13) | +80 (47) | 43 of 1071 (0.040) | 7 of 35 | 0.015 of 472 / 0.060 of 599 |
| data/week3_reg/thr70/unseen | gru_phys_frac | 18 of 91 (11 to 26) | 38 / 35 | +5 (-3 to +14) | +88 (56) | 10 of 1071 (0.009) | 4 of 35 | 0.002 of 472 / 0.015 of 599 |
| data/week3_reg/thr70/unseen | gru_phys_ttp | 16 of 91 (9 to 23) | 40 / 35 | +3 (-5 to +12) | +96 (56) | 8 of 1071 (0.007) | 4 of 35 | 0.000 of 472 / 0.013 of 599 |
| data/week3_reg/thr70/unseen | gru_robot | 5 of 91 (1 to 10) | 10 / 76 | -8 (-16 to +0) | +120 (15) | 46 of 1071 (0.043) | 1 of 35 | 0.095 of 472 / 0.002 of 599 |
| data/week3_reg/thr70/unseen | gru_robotobj1 | 7 of 91 (2 to 12) | 26 / 58 | -6 (-14 to +2) | +88 (33) | 186 of 1071 (0.174) | 1 of 35 | 0.121 of 472 / 0.215 of 599 |
| data/week3_reg/thr70/unseen | gru_robotobj2 | 7 of 91 (2 to 12) | 26 / 58 | -6 (-14 to +2) | +88 (33) | 187 of 1071 (0.175) | 1 of 35 | 0.121 of 472 / 0.217 of 599 |
