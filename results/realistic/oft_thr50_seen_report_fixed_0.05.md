# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/realistic/oft/thr50/seen/merged | progress | 0.046 | -144 (61) | 16 of 81 (9 to 23) | 0.026 | -180 (44) | 11 of 81 (5 to 17) |
| data/realistic/oft/thr50/seen/merged | gru_phys_ttp | 0.049 | -56 (76) | 18 of 81 (11 to 26) | 0.025 | -64 (69) | 17 of 81 (10 to 24) |
| data/realistic/oft/thr50/seen/merged | gru_robot_ttp | 0.049 | -92 (72) | 16 of 81 (9 to 23) | 0.022 | -120 (69) | 12 of 81 (6 to 19) |
| data/realistic/oft/thr50/seen/merged | gru_robotcontact_ttp | 0.049 | -80 (76) | 16 of 81 (9 to 23) | 0.022 | -112 (70) | 10 of 81 (5 to 16) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/realistic/oft/thr50/seen/merged | progress | 16 of 81 (9 to 23) | 45 / 20 |  | +144 (61) | 49 of 1071 (0.046) | 26 of 31 | 0.049 of 472 / 0.043 of 599 |
| data/realistic/oft/thr50/seen/merged | gru_phys_ttp | 18 of 81 (11 to 25) | 58 / 5 | +2 (-6 to +10) | +56 (76) | 52 of 1071 (0.049) | 18 of 31 | 0.034 of 472 / 0.060 of 599 |
| data/realistic/oft/thr50/seen/merged | gru_robot_ttp | 16 of 81 (9 to 23) | 56 / 9 | +0 (-7 to +7) | +92 (72) | 53 of 1071 (0.049) | 14 of 31 | 0.038 of 472 / 0.058 of 599 |
| data/realistic/oft/thr50/seen/merged | gru_robotcontact_ttp | 16 of 81 (9 to 23) | 60 / 5 | +0 (-8 to +8) | +80 (76) | 52 of 1071 (0.049) | 21 of 31 | 0.025 of 472 / 0.067 of 599 |
