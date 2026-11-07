# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/realistic/pi05/thr80/unseen/merged | progress | 0.050 | +28 (30) | 17 of 33 (11 to 23) | 0.025 | -40 (27) | 12 of 33 (7 to 18) |
| data/realistic/pi05/thr80/unseen/merged | gru_phys_ttp | 0.005 | +192 (9) | 7 of 33 (3 to 12) | 0.002 | +136 (8) | 6 of 33 (2 to 11) |
| data/realistic/pi05/thr80/unseen/merged | gru_robot_ttp | 0.068 | -72 (14) | 4 of 33 (1 to 8) | 0.050 | -80 (12) | 2 of 33 (0 to 5) |
| data/realistic/pi05/thr80/unseen/merged | gru_robotcontact_ttp | 0.018 | -68 (14) | 5 of 33 (1 to 9) | 0.009 | -56 (12) | 5 of 33 (1 to 9) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/realistic/pi05/thr80/unseen/merged | progress | 17 of 33 (11 to 22) | 13 / 3 |  | -28 (30) | 46 of 928 (0.050) | 7 of 8 | 0.040 of 475 / 0.060 of 453 |
| data/realistic/pi05/thr80/unseen/merged | gru_phys_ttp | 7 of 33 (3 to 12) | 2 / 24 | -10 (-16 to -3) | -192 (9) | 5 of 928 (0.005) | 1 of 8 | 0.002 of 475 / 0.009 of 453 |
| data/realistic/pi05/thr80/unseen/merged | gru_robot_ttp | 4 of 33 (1 to 8) | 10 / 19 | -13 (-18 to -8) | +72 (14) | 63 of 928 (0.068) | 0 of 8 | 0.109 of 475 / 0.024 of 453 |
| data/realistic/pi05/thr80/unseen/merged | gru_robotcontact_ttp | 5 of 33 (1 to 9) | 9 / 19 | -12 (-18 to -6) | +68 (14) | 17 of 928 (0.018) | 0 of 8 | 0.011 of 475 / 0.026 of 453 |
