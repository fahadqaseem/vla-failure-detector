# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/realistic/oft/thr80/unseen/merged | progress | 0.048 | -96 (74) | 29 of 102 (20 to 38) | 0.025 | -144 (57) | 17 of 102 (10 to 25) |
| data/realistic/oft/thr80/unseen/merged | gru_phys_ttp | 0.025 | -56 (75) | 24 of 102 (16 to 32) | 0.012 | -80 (63) | 20 of 102 (12 to 28) |
| data/realistic/oft/thr80/unseen/merged | gru_robot_ttp | 0.004 | -100 (40) | 10 of 102 (5 to 16) | 0.003 | -128 (32) | 6 of 102 (2 to 11) |
| data/realistic/oft/thr80/unseen/merged | gru_robotcontact_ttp | 0.010 | -72 (79) | 21 of 102 (13 to 29) | 0.006 | -72 (69) | 18 of 102 (11 to 26) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/realistic/oft/thr80/unseen/merged | progress | 29 of 102 (20 to 38) | 45 / 28 |  | +96 (74) | 51 of 1071 (0.048) | 35 of 39 | 0.049 of 472 / 0.047 of 599 |
| data/realistic/oft/thr80/unseen/merged | gru_phys_ttp | 24 of 102 (16 to 33) | 51 / 27 | -5 (-15 to +5) | +56 (75) | 27 of 1071 (0.025) | 8 of 39 | 0.006 of 472 / 0.040 of 599 |
| data/realistic/oft/thr80/unseen/merged | gru_robot_ttp | 10 of 102 (4 to 16) | 30 / 62 | -19 (-29 to -9) | +100 (40) | 4 of 1071 (0.004) | 4 of 39 | 0.002 of 472 / 0.005 of 599 |
| data/realistic/oft/thr80/unseen/merged | gru_robotcontact_ttp | 21 of 102 (13 to 29) | 58 / 23 | -8 (-19 to +3) | +72 (79) | 11 of 1071 (0.010) | 9 of 39 | 0.000 of 472 / 0.018 of 599 |
