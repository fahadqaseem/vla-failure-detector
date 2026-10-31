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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr70/unseen | progress | 22 of 91 (14 to 30) | 46 / 23 |  | +108 (68) | 51 of 1071 (0.048) | 31 of 35 | 0.049 of 472 / 0.047 of 599 |
| data/week3_reg/thr70/unseen | gru_phys | 19 of 91 (12 to 27) | 34 / 38 | -3 (-13 to +7) | +72 (53) | 56 of 1071 (0.052) | 8 of 35 | 0.019 of 472 / 0.078 of 599 |
| data/week3_reg/thr70/unseen | gru_phys_frac | 21 of 91 (13 to 29) | 41 / 29 | -1 (-9 to +7) | +68 (62) | 18 of 1071 (0.017) | 8 of 35 | 0.011 of 472 / 0.022 of 599 |
| data/week3_reg/thr70/unseen | gru_phys_ttp | 22 of 91 (14 to 30) | 39 / 30 | +0 (-8 to +8) | +80 (61) | 19 of 1071 (0.018) | 7 of 35 | 0.006 of 472 / 0.027 of 599 |
| data/week3_reg/thr70/unseen | gru_robot | 8 of 91 (3 to 14) | 15 / 68 | -14 (-23 to -5) | +104 (23) | 51 of 1071 (0.048) | 2 of 35 | 0.104 of 472 / 0.003 of 599 |
| data/week3_reg/thr70/unseen | gru_robotobj1 | 7 of 91 (2 to 12) | 26 / 58 | -15 (-24 to -6) | +88 (33) | 189 of 1071 (0.176) | 1 of 35 | 0.123 of 472 / 0.219 of 599 |
| data/week3_reg/thr70/unseen | gru_robotobj2 | 7 of 91 (2 to 12) | 28 / 56 | -15 (-24 to -6) | +88 (35) | 194 of 1071 (0.181) | 1 of 35 | 0.125 of 472 / 0.225 of 599 |
