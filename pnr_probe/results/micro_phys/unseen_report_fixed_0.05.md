# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 |
|---|---|---|---|---|---|---|---|
| pnr_probe/results/micro_phys/unseen | progress | 0.025 | -200 (43) | 11 of 81 (5 to 17) | 0.048 | -144 (61) | 17 of 81 (10 to 24) |
| pnr_probe/results/micro_phys/unseen | gru_phys | 0.011 | -112 (53) | 8 of 81 (3 to 14) | 0.021 | -96 (55) | 13 of 81 (7 to 20) |
| pnr_probe/results/micro_phys/unseen | gru_phys_cusum | 0.126 | -128 (27) | 4 of 81 (1 to 8) | 0.149 | -112 (28) | 4 of 81 (1 to 8) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| pnr_probe/results/micro_phys/unseen | progress | 17 of 81 (10 to 24) | 44 / 20 |  | +144 (61) | 51 of 1071 (0.048) | 27 of 31 | 0.049 of 472 / 0.047 of 599 |
| pnr_probe/results/micro_phys/unseen | gru_phys | 13 of 81 (7 to 20) | 42 / 26 | -4 (-13 to +5) | +96 (55) | 23 of 1071 (0.021) | 3 of 31 | 0.008 of 472 / 0.032 of 599 |
| pnr_probe/results/micro_phys/unseen | gru_phys_cusum | 4 of 81 (1 to 8) | 24 / 53 | -13 (-21 to -5) | +112 (28) | 160 of 1071 (0.149) | 3 of 31 | 0.102 of 472 / 0.187 of 599 |
