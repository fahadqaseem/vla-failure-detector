# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr80/seen | progress | 0.047 | +44 (30) | 18 of 33 (12 to 23) | 0.020 | -40 (27) | 12 of 33 (7 to 17) |
| data/pi05_reg/thr80/seen | gru_phys | 0.066 | +88 (28) | 18 of 33 (12 to 23) | 0.019 | +32 (23) | 13 of 33 (8 to 19) |
| data/pi05_reg/thr80/seen | gru_phys_frac | 0.057 | +128 (29) | 20 of 33 (14 to 25) | 0.020 | +64 (27) | 17 of 33 (11 to 23) |
| data/pi05_reg/thr80/seen | gru_phys_ttp | 0.055 | +104 (28) | 19 of 33 (13 to 24) | 0.019 | +72 (27) | 17 of 33 (11 to 23) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| data/pi05_reg/thr80/seen | progress | 12 of 33 (7 to 17) | 15 / 6 |  | +40 (27) | 19 of 928 (0.020) | 7 of 8 | 0.017 of 475 / 0.024 of 453 |
| data/pi05_reg/thr80/seen | gru_phys | 13 of 33 (8 to 19) | 10 / 10 | +1 (-5 to +7) | -32 (23) | 18 of 928 (0.019) | 4 of 8 | 0.017 of 475 / 0.022 of 453 |
| data/pi05_reg/thr80/seen | gru_phys_frac | 17 of 33 (11 to 23) | 10 / 6 | +5 (-1 to +11) | -64 (27) | 19 of 928 (0.020) | 3 of 8 | 0.019 of 475 / 0.022 of 453 |
| data/pi05_reg/thr80/seen | gru_phys_ttp | 17 of 33 (11 to 23) | 10 / 6 | +5 (-1 to +11) | -72 (27) | 18 of 928 (0.019) | 3 of 8 | 0.017 of 475 / 0.022 of 453 |
