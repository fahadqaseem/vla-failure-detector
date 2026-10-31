# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/week3_reg/thr70/seen | progress | 0.046 | -112 (69) | 22 of 91 (14 to 30) | 0.026 | -136 (51) | 15 of 91 (8 to 22) |
| data/week3_reg/thr70/seen | gru_phys | 0.046 | -16 (85) | 36 of 91 (27 to 45) | 0.017 | -32 (84) | 27 of 91 (19 to 36) |
| data/week3_reg/thr70/seen | gru_phys_frac | 0.049 | -24 (88) | 35 of 91 (26 to 44) | 0.025 | -48 (78) | 28 of 91 (20 to 37) |
| data/week3_reg/thr70/seen | gru_phys_ttp | 0.047 | -24 (86) | 34 of 91 (25 to 43) | 0.025 | -48 (79) | 28 of 91 (20 to 37) |
| data/week3_reg/thr70/seen | gru_robot | 0.044 | -56 (87) | 29 of 91 (20 to 38) | 0.021 | -80 (74) | 19 of 91 (12 to 27) |
| data/week3_reg/thr70/seen | gru_robotobj1 | 0.049 | -40 (83) | 31 of 91 (22 to 40) | 0.022 | -72 (80) | 22 of 91 (14 to 30) |
| data/week3_reg/thr70/seen | gru_robotobj2 | 0.052 | -24 (83) | 31 of 91 (22 to 40) | 0.022 | -72 (81) | 21 of 91 (13 to 29) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/week3_reg/thr70/seen | progress | 15 of 91 (8 to 22) | 36 / 40 |  | +136 (51) | 28 of 1071 (0.026) | 25 of 35 | 0.032 of 472 / 0.022 of 599 |
| data/week3_reg/thr70/seen | gru_phys | 27 of 91 (19 to 36) | 57 / 7 | +12 (+2 to +22) | +32 (84) | 18 of 1071 (0.017) | 14 of 35 | 0.006 of 472 / 0.025 of 599 |
| data/week3_reg/thr70/seen | gru_phys_frac | 28 of 91 (20 to 37) | 50 / 13 | +13 (+4 to +22) | +48 (78) | 27 of 1071 (0.025) | 18 of 35 | 0.013 of 472 / 0.035 of 599 |
| data/week3_reg/thr70/seen | gru_phys_ttp | 28 of 91 (19 to 37) | 51 / 12 | +13 (+3 to +23) | +48 (79) | 27 of 1071 (0.025) | 14 of 35 | 0.015 of 472 / 0.033 of 599 |
| data/week3_reg/thr70/seen | gru_robot | 19 of 91 (12 to 27) | 55 / 17 | +4 (-5 to +13) | +80 (74) | 22 of 1071 (0.021) | 13 of 35 | 0.013 of 472 / 0.027 of 599 |
| data/week3_reg/thr70/seen | gru_robotobj1 | 22 of 91 (14 to 30) | 58 / 11 | +7 (-1 to +16) | +72 (80) | 24 of 1071 (0.022) | 13 of 35 | 0.004 of 472 / 0.037 of 599 |
| data/week3_reg/thr70/seen | gru_robotobj2 | 21 of 91 (14 to 29) | 60 / 10 | +6 (-3 to +15) | +72 (81) | 24 of 1071 (0.022) | 15 of 35 | 0.004 of 472 / 0.037 of 599 |
