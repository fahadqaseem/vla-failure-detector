# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/realistic/oft/thr80/seen/merged | progress | 0.046 | -104 (76) | 28 of 102 (19 to 37) | 0.026 | -128 (58) | 18 of 102 (11 to 26) |
| data/realistic/oft/thr80/seen/merged | gru_phys_ttp | 0.054 | +0 (97) | 51 of 102 (41 to 61) | 0.023 | -32 (87) | 37 of 102 (28 to 47) |
| data/realistic/oft/thr80/seen/merged | gru_robot_ttp | 0.047 | -40 (92) | 33 of 102 (24 to 42) | 0.022 | -56 (87) | 27 of 102 (19 to 36) |
| data/realistic/oft/thr80/seen/merged | gru_robotcontact_ttp | 0.047 | -24 (96) | 41 of 102 (31 to 51) | 0.021 | -36 (90) | 30 of 102 (21 to 39) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/realistic/oft/thr80/seen/merged | progress | 18 of 102 (11 to 26) | 40 / 44 |  | +128 (58) | 28 of 1071 (0.026) | 28 of 39 | 0.032 of 472 / 0.022 of 599 |
| data/realistic/oft/thr80/seen/merged | gru_phys_ttp | 37 of 102 (28 to 47) | 50 / 15 | +19 (+8 to +30) | +32 (87) | 25 of 1071 (0.023) | 14 of 39 | 0.011 of 472 / 0.033 of 599 |
| data/realistic/oft/thr80/seen/merged | gru_robot_ttp | 27 of 102 (19 to 36) | 60 / 15 | +9 (-2 to +19) | +56 (87) | 24 of 1071 (0.022) | 13 of 39 | 0.021 of 472 / 0.023 of 599 |
| data/realistic/oft/thr80/seen/merged | gru_robotcontact_ttp | 30 of 102 (21 to 39) | 60 / 12 | +12 (+1 to +23) | +36 (90) | 23 of 1071 (0.021) | 14 of 39 | 0.008 of 472 / 0.032 of 599 |
