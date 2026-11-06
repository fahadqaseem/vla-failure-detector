# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/combo/oft/thr50/merged | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| data/combo/oft/thr50/merged | gru_phys_ttp | 0.054 | -120 (49) | 11 of 81 (5 to 17) | 0.007 | -120 (45) | 10 of 81 (5 to 16) |
| data/combo/oft/thr50/merged | or_progress_ttp | 0.042 | -128 (64) | 16 of 81 (9 to 23) | 0.018 | -144 (63) | 13 of 81 (7 to 20) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/combo/oft/thr50/merged | progress | 11 of 81 (5 to 17) | 32 / 38 |  | +200 (43) | 27 of 1071 (0.025) | 22 of 31 | 0.030 of 472 / 0.022 of 599 |
| data/combo/oft/thr50/merged | gru_phys_ttp | 10 of 81 (5 to 16) | 35 / 36 | -1 (-7 to +6) | +120 (45) | 8 of 1071 (0.007) | 2 of 31 | 0.004 of 472 / 0.010 of 599 |
| data/combo/oft/thr50/merged | or_progress_ttp | 13 of 81 (7 to 20) | 50 / 18 | +2 (-2 to +6) | +144 (63) | 19 of 1071 (0.018) | 21 of 31 | 0.019 of 472 / 0.017 of 599 |
