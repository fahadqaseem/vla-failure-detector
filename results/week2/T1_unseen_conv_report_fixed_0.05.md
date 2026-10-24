# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/week2/T1_unseen_conv | progress | 0.048 | -128 (36) | 11 of 46 (6 to 17) | 0.023 | -160 (30) | 10 of 46 (5 to 16) |
| results/week2/T1_unseen_conv | conv | 0.117 | -112 (34) | 8 of 46 (3 to 13) | 0.052 | -128 (29) | 5 of 46 (1 to 9) |
| results/week2/T1_unseen_conv | conv_cusum | 0.078 | -88 (35) | 12 of 46 (6 to 18) | 0.043 | -76 (30) | 12 of 46 (6 to 18) |
| results/week2/T1_unseen_conv | conv_phys | 0.000 | +96 (4) | 2 of 46 (0 to 5) | 0.000 | +192 (3) | 2 of 46 (0 to 5) |
| results/week2/T1_unseen_conv | conv_phys_cusum | 0.003 | -40 (1) | 0 of 46 (0 to 0) | 0.003 | -56 (1) | 0 of 46 (0 to 0) |
| results/week2/T1_unseen_conv | conv_physvla | 0.052 | -124 (36) | 9 of 46 (4 to 14) | 0.020 | -128 (32) | 7 of 46 (3 to 12) |
| results/week2/T1_unseen_conv | conv_physvla_cusum | 0.102 | -80 (37) | 10 of 46 (5 to 16) | 0.077 | -112 (31) | 8 of 46 (3 to 13) |
| results/week2/T1_unseen_conv | conv_physall | 0.039 | -88 (41) | 11 of 46 (6 to 17) | 0.022 | -112 (37) | 9 of 46 (4 to 15) |
| results/week2/T1_unseen_conv | conv_physall_cusum | 0.070 | -80 (39) | 10 of 46 (5 to 16) | 0.047 | -88 (37) | 7 of 46 (3 to 12) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/T1_unseen_conv | progress | 11 of 46 (6 to 17) | 25 / 10 |  | +128 (36) | 36 of 743 (0.048) | 23 of 27 | 0.049 of 472 / 0.048 of 271 |
| results/week2/T1_unseen_conv | conv | 8 of 46 (3 to 13) | 26 / 12 | -3 (-9 to +3) | +112 (34) | 87 of 743 (0.117) | 10 of 27 | 0.085 of 472 / 0.173 of 271 |
| results/week2/T1_unseen_conv | conv_cusum | 12 of 46 (6 to 18) | 23 / 11 | +1 (-5 to +7) | +88 (35) | 58 of 743 (0.078) | 16 of 27 | 0.072 of 472 / 0.089 of 271 |
| results/week2/T1_unseen_conv | conv_phys | 2 of 46 (0 to 5) | 2 / 42 | -9 (-14 to -4) | -96 (4) | 0 of 743 (0.000) | 0 of 27 | 0.000 of 472 / 0.000 of 271 |
| results/week2/T1_unseen_conv | conv_phys_cusum | 0 of 46 (0 to 0) | 1 / 45 | -11 (-17 to -6) | +40 (1) | 2 of 743 (0.003) | 0 of 27 | 0.000 of 472 / 0.007 of 271 |
| results/week2/T1_unseen_conv | conv_physvla | 9 of 46 (4 to 15) | 27 / 10 | -2 (-9 to +5) | +124 (36) | 39 of 743 (0.052) | 5 of 27 | 0.025 of 472 / 0.100 of 271 |
| results/week2/T1_unseen_conv | conv_physvla_cusum | 10 of 46 (5 to 16) | 27 / 9 | -1 (-7 to +5) | +80 (37) | 76 of 743 (0.102) | 8 of 27 | 0.083 of 472 / 0.137 of 271 |
| results/week2/T1_unseen_conv | conv_physall | 11 of 46 (6 to 17) | 30 / 5 | +0 (-6 to +6) | +88 (41) | 29 of 743 (0.039) | 8 of 27 | 0.006 of 472 / 0.096 of 271 |
| results/week2/T1_unseen_conv | conv_physall_cusum | 10 of 46 (5 to 16) | 29 / 7 | -1 (-7 to +5) | +80 (39) | 52 of 743 (0.070) | 10 of 27 | 0.049 of 472 / 0.107 of 271 |
