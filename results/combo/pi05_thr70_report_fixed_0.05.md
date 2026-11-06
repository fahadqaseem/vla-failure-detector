# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/combo/pi05/thr70/merged | progress | 0.050 | -84 (28) | 8 of 31 (3 to 13) | 0.025 | -136 (25) | 6 of 31 (2 to 11) |
| data/combo/pi05/thr70/merged | gru_phys_ttp | 0.014 | +84 (14) | 10 of 31 (5 to 15) | 0.005 | +80 (12) | 9 of 31 (4 to 14) |
| data/combo/pi05/thr70/merged | or_progress_ttp | 0.032 | -64 (29) | 12 of 31 (7 to 18) | 0.017 | -76 (26) | 12 of 31 (7 to 18) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/combo/pi05/thr70/merged | progress | 8 of 31 (4 to 13) | 20 / 3 |  | +84 (28) | 46 of 928 (0.050) | 6 of 7 | 0.040 of 475 / 0.060 of 453 |
| data/combo/pi05/thr70/merged | gru_phys_ttp | 10 of 31 (5 to 15) | 4 / 17 | +2 (-3 to +8) | -84 (14) | 13 of 928 (0.014) | 0 of 7 | 0.008 of 475 / 0.020 of 453 |
| data/combo/pi05/thr70/merged | or_progress_ttp | 12 of 31 (7 to 18) | 17 / 2 | +4 (+1 to +8) | +64 (29) | 30 of 928 (0.032) | 6 of 7 | 0.025 of 475 / 0.040 of 453 |
