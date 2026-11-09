# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/ablation/oft/thr50/merged | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| data/ablation/oft/thr50/merged | gru_phys_ttp | 0.054 | -120 (49) | 11 of 81 (5 to 17) | 0.007 | -120 (45) | 10 of 81 (5 to 16) |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_goal | 0.097 | -140 (22) | 1 of 81 (0 to 3) | 0.053 | -176 (21) | 0 of 81 (0 to 0) |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_pose | 0.048 | -160 (30) | 4 of 81 (1 to 8) | 0.048 | -160 (28) | 4 of 81 (1 to 8) |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_contact | 0.038 | -64 (43) | 12 of 81 (6 to 18) | 0.008 | -72 (40) | 11 of 81 (5 to 17) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/ablation/oft/thr50/merged | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| data/ablation/oft/thr50/merged | gru_phys_ttp | 10 of 81 (5 to 16) | 35 / 36 | -1 (-7 to +6) | +120 (45) | 8 of 1071 (0.007) | 2 of 31 | 0.004 of 472 / 0.010 of 599 |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_goal | 0 of 81 (0 to 0) | 21 / 60 | -11 (-17 to -5) | +176 (21) | 57 of 1071 (0.053) | 0 of 31 | 0.032 of 472 / 0.070 of 599 |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_pose | 4 of 81 (1 to 8) | 24 / 53 | -7 (-14 to -1) | +160 (28) | 51 of 1071 (0.048) | 0 of 31 | 0.104 of 472 / 0.003 of 599 |
| data/ablation/oft/thr50/merged | gru_phys_ttp_no_contact | 11 of 81 (5 to 17) | 29 / 41 | +0 (-7 to +7) | +72 (40) | 9 of 1071 (0.008) | 1 of 31 | 0.002 of 472 / 0.013 of 599 |
