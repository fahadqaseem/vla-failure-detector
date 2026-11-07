# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/realistic/pi05/thr50/unseen/merged | progress | 0.050 | -104 (24) | 5 of 27 (2 to 9) | 0.025 | -144 (21) | 2 of 27 (0 to 5) |
| data/realistic/pi05/thr50/unseen/merged | gru_phys_ttp | 0.009 | +96 (15) | 9 of 27 (4 to 14) | 0.005 | +64 (15) | 8 of 27 (4 to 13) |
| data/realistic/pi05/thr50/unseen/merged | gru_robot_ttp | 0.050 | -160 (10) | 1 of 27 (0 to 3) | 0.019 | -168 (8) | 1 of 27 (0 to 3) |
| data/realistic/pi05/thr50/unseen/merged | gru_robotcontact_ttp | 0.054 | -104 (11) | 2 of 27 (0 to 5) | 0.044 | -160 (9) | 1 of 27 (0 to 3) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/realistic/pi05/thr50/unseen/merged | progress | 5 of 27 (1 to 9) | 19 / 3 |  | +104 (24) | 46 of 928 (0.050) | 6 of 7 | 0.040 of 475 / 0.060 of 453 |
| data/realistic/pi05/thr50/unseen/merged | gru_phys_ttp | 9 of 27 (4 to 14) | 6 / 12 | +4 (+1 to +8) | -96 (15) | 8 of 928 (0.009) | 1 of 7 | 0.006 of 475 / 0.011 of 453 |
| data/realistic/pi05/thr50/unseen/merged | gru_robot_ttp | 1 of 27 (0 to 3) | 9 / 17 | -4 (-8 to -1) | +160 (10) | 46 of 928 (0.050) | 1 of 7 | 0.091 of 475 / 0.007 of 453 |
| data/realistic/pi05/thr50/unseen/merged | gru_robotcontact_ttp | 2 of 27 (0 to 5) | 9 / 16 | -3 (-7 to +0) | +104 (11) | 50 of 928 (0.054) | 1 of 7 | 0.101 of 475 / 0.004 of 453 |
