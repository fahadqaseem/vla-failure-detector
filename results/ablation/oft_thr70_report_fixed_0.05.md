# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/ablation/oft/thr70/merged | progress | 0.048 | -108 (68) | 22 of 91 (14 to 30) | 0.025 | -156 (50) | 13 of 91 (7 to 20) |
| data/ablation/oft/thr70/merged | gru_phys_ttp | 0.018 | -80 (61) | 22 of 91 (14 to 30) | 0.007 | -96 (56) | 16 of 91 (9 to 23) |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_goal | 0.159 | -112 (31) | 5 of 91 (1 to 9) | 0.156 | -120 (28) | 4 of 91 (1 to 8) |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_pose | 0.031 | -104 (65) | 18 of 91 (11 to 26) | 0.009 | -120 (59) | 15 of 91 (8 to 22) |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_contact | 0.013 | -80 (56) | 17 of 91 (10 to 25) | 0.007 | -120 (47) | 10 of 91 (5 to 16) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/ablation/oft/thr70/merged | progress | 22 of 91 (14 to 30) | 46 / 23 |  | +108 (68) | 51 of 1071 (0.048) | 31 of 35 | 0.049 of 472 / 0.047 of 599 |
| data/ablation/oft/thr70/merged | gru_phys_ttp | 22 of 91 (14 to 30) | 39 / 30 | +0 (-8 to +8) | +80 (61) | 19 of 1071 (0.018) | 7 of 35 | 0.006 of 472 / 0.027 of 599 |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_goal | 5 of 91 (1 to 10) | 26 / 60 | -17 (-26 to -8) | +112 (31) | 170 of 1071 (0.159) | 0 of 35 | 0.104 of 472 / 0.202 of 599 |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_pose | 18 of 91 (11 to 26) | 47 / 26 | -4 (-13 to +5) | +104 (65) | 33 of 1071 (0.031) | 4 of 35 | 0.051 of 472 / 0.015 of 599 |
| data/ablation/oft/thr70/merged | gru_phys_ttp_no_contact | 17 of 91 (10 to 24) | 39 / 35 | -5 (-14 to +3) | +80 (56) | 14 of 1071 (0.013) | 5 of 35 | 0.002 of 472 / 0.022 of 599 |
