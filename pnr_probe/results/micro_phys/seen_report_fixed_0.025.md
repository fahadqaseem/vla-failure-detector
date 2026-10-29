# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 |
|---|---|---|---|---|---|---|---|
| pnr_probe/results/micro_phys/seen | progress | 0.026 | -180 (44) | 11 of 81 (5 to 17) | 0.046 | -144 (61) | 16 of 81 (9 to 23) |
| pnr_probe/results/micro_phys/seen | gru_phys | 0.021 | -72 (70) | 14 of 81 (8 to 21) | 0.045 | -56 (73) | 21 of 81 (14 to 29) |
| pnr_probe/results/micro_phys/seen | gru_phys_cusum | 0.023 | -64 (55) | 13 of 81 (7 to 20) | 0.049 | -56 (67) | 18 of 81 (11 to 25) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/micro_phys/seen | progress | 11 of 81 (5 to 17) | 33 / 37 |  | +180 (44) | 28 of 1071 (0.026) | 22 of 31 | 0.032 of 472 / 0.022 of 599 |
| pnr_probe/results/micro_phys/seen | gru_phys | 14 of 81 (8 to 21) | 56 / 11 | +3 (-5 to +11) | +72 (70) | 23 of 1071 (0.021) | 9 of 31 | 0.008 of 472 / 0.032 of 599 |
| pnr_probe/results/micro_phys/seen | gru_phys_cusum | 13 of 81 (7 to 20) | 42 / 26 | +2 (-6 to +10) | +64 (55) | 25 of 1071 (0.023) | 9 of 31 | 0.017 of 472 / 0.028 of 599 |
