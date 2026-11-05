# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr50/seen | progress | 0.047 | -96 (24) | 6 of 27 (2 to 10) | 0.020 | -160 (21) | 1 of 27 (0 to 3) |
| data/pi05_reg/thr50/seen | gru_phys | 0.053 | -56 (23) | 10 of 27 (5 to 15) | 0.025 | -72 (19) | 7 of 27 (3 to 11) |
| data/pi05_reg/thr50/seen | gru_phys_frac | 0.056 | -32 (23) | 11 of 27 (6 to 16) | 0.022 | -56 (19) | 9 of 27 (4 to 14) |
| data/pi05_reg/thr50/seen | gru_phys_ttp | 0.051 | -28 (22) | 11 of 27 (6 to 16) | 0.023 | +32 (19) | 10 of 27 (5 to 15) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr50/seen | progress | 1 of 27 (0 to 3) | 20 / 6 |  | +160 (21) | 19 of 928 (0.020) | 6 of 7 | 0.017 of 475 / 0.024 of 453 |
| data/pi05_reg/thr50/seen | gru_phys | 7 of 27 (3 to 12) | 12 / 8 | +6 (+2 to +10) | +72 (19) | 23 of 928 (0.025) | 2 of 7 | 0.011 of 475 / 0.040 of 453 |
| data/pi05_reg/thr50/seen | gru_phys_frac | 9 of 27 (4 to 14) | 10 / 8 | +8 (+4 to +13) | +56 (19) | 20 of 928 (0.022) | 2 of 7 | 0.013 of 475 / 0.031 of 453 |
| data/pi05_reg/thr50/seen | gru_phys_ttp | 10 of 27 (5 to 15) | 9 / 8 | +9 (+4 to +14) | -32 (19) | 21 of 928 (0.023) | 1 of 7 | 0.013 of 475 / 0.033 of 453 |
