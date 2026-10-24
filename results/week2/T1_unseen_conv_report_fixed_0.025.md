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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/week2/T1_unseen_conv | progress | 10 of 46 (5 to 16) | 20 / 16 |  | +160 (30) | 17 of 743 (0.023) | 20 of 27 | 0.025 of 472 / 0.018 of 271 |
| results/week2/T1_unseen_conv | conv | 5 of 46 (1 to 10) | 24 / 17 | -5 (-10 to +0) | +128 (29) | 39 of 743 (0.052) | 8 of 27 | 0.019 of 472 / 0.111 of 271 |
| results/week2/T1_unseen_conv | conv_cusum | 12 of 46 (6 to 18) | 18 / 16 | +2 (-4 to +8) | +76 (30) | 32 of 743 (0.043) | 12 of 27 | 0.036 of 472 / 0.055 of 271 |
| results/week2/T1_unseen_conv | conv_phys | 2 of 46 (0 to 5) | 1 / 43 | -8 (-13 to -3) | -192 (3) | 0 of 743 (0.000) | 0 of 27 | 0.000 of 472 / 0.000 of 271 |
| results/week2/T1_unseen_conv | conv_phys_cusum | 0 of 46 (0 to 0) | 1 / 45 | -10 (-16 to -5) | +56 (1) | 2 of 743 (0.003) | 0 of 27 | 0.000 of 472 / 0.007 of 271 |
| results/week2/T1_unseen_conv | conv_physvla | 7 of 46 (3 to 12) | 25 / 14 | -3 (-9 to +3) | +128 (32) | 15 of 743 (0.020) | 5 of 27 | 0.004 of 472 / 0.048 of 271 |
| results/week2/T1_unseen_conv | conv_physvla_cusum | 8 of 46 (3 to 13) | 23 / 15 | -2 (-7 to +3) | +112 (31) | 57 of 743 (0.077) | 7 of 27 | 0.066 of 472 / 0.096 of 271 |
| results/week2/T1_unseen_conv | conv_physall | 9 of 46 (4 to 15) | 28 / 9 | -1 (-6 to +4) | +112 (37) | 16 of 743 (0.022) | 6 of 27 | 0.002 of 472 / 0.055 of 271 |
| results/week2/T1_unseen_conv | conv_physall_cusum | 7 of 46 (3 to 12) | 30 / 9 | -3 (-8 to +1) | +88 (37) | 35 of 743 (0.047) | 8 of 27 | 0.032 of 472 / 0.074 of 271 |
