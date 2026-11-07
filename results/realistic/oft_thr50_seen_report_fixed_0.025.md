# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/realistic/oft/thr50/seen/merged | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| data/realistic/oft/thr50/seen/merged | gru_phys_ttp | 0.049 | -56 (76) | 18 of 81 (11 to 26) | 0.025 | -64 (69) | 17 of 81 (10 to 24) |
| data/realistic/oft/thr50/seen/merged | gru_robot_ttp | 0.049 | -92 (72) | 16 of 81 (9 to 23) | 0.022 | -120 (69) | 12 of 81 (6 to 19) |
| data/realistic/oft/thr50/seen/merged | gru_robotcontact_ttp | 0.049 | -80 (76) | 16 of 81 (9 to 23) | 0.022 | -112 (70) | 10 of 81 (5 to 16) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/realistic/oft/thr50/seen/merged | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| data/realistic/oft/thr50/seen/merged | gru_phys_ttp | 17 of 81 (10 to 24) | 52 / 12 | +6 (-2 to +14) | +64 (69) | 27 of 1071 (0.025) | 10 of 31 | 0.013 of 472 / 0.035 of 599 |
| data/realistic/oft/thr50/seen/merged | gru_robot_ttp | 12 of 81 (6 to 19) | 57 / 12 | +1 (-6 to +8) | +120 (69) | 24 of 1071 (0.022) | 12 of 31 | 0.015 of 472 / 0.028 of 599 |
| data/realistic/oft/thr50/seen/merged | gru_robotcontact_ttp | 10 of 81 (5 to 16) | 60 / 11 | -1 (-9 to +7) | +112 (70) | 24 of 1071 (0.022) | 11 of 31 | 0.011 of 472 / 0.032 of 599 |
