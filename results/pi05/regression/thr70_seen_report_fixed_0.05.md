# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr70/seen | progress | 0.047 | -76 (28) | 9 of 31 (4 to 14) | 0.020 | -152 (25) | 6 of 31 (2 to 11) |
| data/pi05_reg/thr70/seen | gru_phys | 0.055 | +16 (26) | 14 of 31 (9 to 19) | 0.026 | -36 (22) | 9 of 31 (4 to 14) |
| data/pi05_reg/thr70/seen | gru_phys_frac | 0.058 | +32 (28) | 17 of 31 (11 to 22) | 0.024 | -32 (25) | 11 of 31 (6 to 16) |
| data/pi05_reg/thr70/seen | gru_phys_ttp | 0.058 | +36 (28) | 17 of 31 (11 to 22) | 0.025 | +8 (25) | 13 of 31 (8 to 18) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr70/seen | progress | 9 of 31 (4 to 14) | 19 / 3 |  | +76 (28) | 44 of 928 (0.047) | 6 of 7 | 0.038 of 475 / 0.057 of 453 |
| data/pi05_reg/thr70/seen | gru_phys | 14 of 31 (9 to 20) | 12 / 5 | +5 (-2 to +12) | -16 (26) | 51 of 928 (0.055) | 3 of 7 | 0.027 of 475 / 0.084 of 453 |
| data/pi05_reg/thr70/seen | gru_phys_frac | 17 of 31 (12 to 22) | 11 / 3 | +8 (+2 to +14) | -32 (28) | 54 of 928 (0.058) | 5 of 7 | 0.029 of 475 / 0.088 of 453 |
| data/pi05_reg/thr70/seen | gru_phys_ttp | 17 of 31 (12 to 22) | 11 / 3 | +8 (+2 to +14) | -36 (28) | 54 of 928 (0.058) | 2 of 7 | 0.029 of 475 / 0.088 of 453 |
