# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/combo/oft/thr70/merged | progress | 0.048 | -108 (68) | 22 of 91 (14 to 30) | 0.025 | -156 (50) | 13 of 91 (7 to 20) |
| data/combo/oft/thr70/merged | gru_phys_ttp | 0.017 | -84 (60) | 21 of 91 (14 to 29) | 0.007 | -96 (57) | 16 of 91 (9 to 24) |
| data/combo/oft/thr70/merged | or_progress_ttp | 0.034 | -92 (80) | 26 of 91 (18 to 35) | 0.019 | -128 (74) | 21 of 91 (14 to 29) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/combo/oft/thr70/merged | progress | 22 of 91 (14 to 30) | 46 / 23 |  | +108 (68) | 51 of 1071 (0.048) | 31 of 35 | 0.049 of 472 / 0.047 of 599 |
| data/combo/oft/thr70/merged | gru_phys_ttp | 21 of 91 (14 to 29) | 39 / 31 | -1 (-9 to +8) | +84 (60) | 18 of 1071 (0.017) | 6 of 35 | 0.006 of 472 / 0.025 of 599 |
| data/combo/oft/thr70/merged | or_progress_ttp | 26 of 91 (18 to 34) | 54 / 11 | +4 (-3 to +11) | +92 (80) | 36 of 1071 (0.034) | 28 of 35 | 0.034 of 472 / 0.033 of 599 |
