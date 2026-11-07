# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/realistic/pi05/thr80/seen/merged | progress | 0.047 | +44 (30) | 18 of 33 (12 to 23) | 0.020 | -40 (27) | 12 of 33 (7 to 17) |
| data/realistic/pi05/thr80/seen/merged | gru_phys_ttp | 0.055 | +104 (28) | 19 of 33 (13 to 24) | 0.019 | +72 (27) | 17 of 33 (11 to 23) |
| data/realistic/pi05/thr80/seen/merged | gru_robot_ttp | 0.044 | +32 (27) | 15 of 33 (9 to 21) | 0.026 | -32 (23) | 10 of 33 (5 to 15) |
| data/realistic/pi05/thr80/seen/merged | gru_robotcontact_ttp | 0.051 | +56 (27) | 16 of 33 (10 to 22) | 0.027 | -8 (25) | 12 of 33 (7 to 17) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/realistic/pi05/thr80/seen/merged | progress | 18 of 33 (12 to 23) | 12 / 3 |  | -44 (30) | 44 of 928 (0.047) | 7 of 8 | 0.038 of 475 / 0.057 of 453 |
| data/realistic/pi05/thr80/seen/merged | gru_phys_ttp | 19 of 33 (13 to 24) | 9 / 5 | +1 (-5 to +7) | -104 (28) | 51 of 928 (0.055) | 4 of 8 | 0.027 of 475 / 0.084 of 453 |
| data/realistic/pi05/thr80/seen/merged | gru_robot_ttp | 15 of 33 (9 to 21) | 12 / 6 | -3 (-9 to +3) | -32 (27) | 41 of 928 (0.044) | 5 of 8 | 0.032 of 475 / 0.057 of 453 |
| data/realistic/pi05/thr80/seen/merged | gru_robotcontact_ttp | 16 of 33 (10 to 22) | 11 / 6 | -2 (-7 to +3) | -56 (27) | 47 of 928 (0.051) | 6 of 8 | 0.034 of 475 / 0.068 of 453 |
