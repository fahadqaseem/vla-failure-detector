# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/combo/oft/thr50/merged | progress | 0.048 | -144 (61) | 17 of 81 (10 to 24) | 0.025 | -200 (43) | 11 of 81 (5 to 17) |
| data/combo/oft/thr50/merged | gru_phys_ttp | 0.054 | -120 (49) | 11 of 81 (5 to 17) | 0.007 | -120 (45) | 10 of 81 (5 to 16) |
| data/combo/oft/thr50/merged | or_progress_ttp | 0.042 | -128 (64) | 16 of 81 (9 to 23) | 0.018 | -144 (63) | 13 of 81 (7 to 20) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/combo/oft/thr50/merged | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| data/combo/oft/thr50/merged | gru_phys_ttp | 11 of 81 (5 to 17) | 38 / 32 | -6 (-14 to +2) | +120 (49) | 58 of 1071 (0.054) | 2 of 31 | 0.108 of 472 / 0.012 of 599 |
| data/combo/oft/thr50/merged | or_progress_ttp | 16 of 81 (9 to 23) | 48 / 17 | -1 (-7 to +5) | +128 (64) | 45 of 1071 (0.042) | 23 of 31 | 0.055 of 472 / 0.032 of 599 |
