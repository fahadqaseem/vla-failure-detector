# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/pi05/all_seen_mlp | progress | 0.047 | -96 (24) | 6 of 27 (2 to 10) | 0.020 | -160 (21) | 1 of 27 (0 to 3) |
| results/pi05/all_seen_mlp | mlp | 0.054 | -48 (25) | 8 of 27 (4 to 13) | 0.024 | -44 (22) | 5 of 27 (1 to 9) |
| results/pi05/all_seen_mlp | combined | 0.096 | -16 (25) | 9 of 27 (4 to 14) | 0.044 | -80 (24) | 8 of 27 (4 to 13) |
| results/pi05/all_seen_mlp | mlp_cusum | 0.051 | -64 (25) | 7 of 27 (3 to 12) | 0.024 | -56 (22) | 4 of 27 (1 to 8) |
| results/pi05/all_seen_mlp | combined_cusum | 0.089 | -32 (25) | 8 of 27 (4 to 13) | 0.038 | -92 (24) | 7 of 27 (3 to 11) |
| results/pi05/all_seen_mlp | mlp_phys | 0.053 | +12 (20) | 10 of 27 (5 to 15) | 0.027 | -68 (18) | 8 of 27 (4 to 13) |
| results/pi05/all_seen_mlp | mlp_phys_cusum | 0.041 | -64 (15) | 5 of 27 (1 to 9) | 0.020 | -116 (10) | 1 of 27 (0 to 3) |
| results/pi05/all_seen_mlp | mlp_physvla | 0.053 | -40 (23) | 9 of 27 (4 to 14) | 0.022 | -32 (21) | 8 of 27 (4 to 13) |
| results/pi05/all_seen_mlp | mlp_physvla_cusum | 0.052 | -56 (25) | 10 of 27 (5 to 15) | 0.022 | -48 (21) | 7 of 27 (3 to 12) |
| results/pi05/all_seen_mlp | mlp_physall | 0.053 | -24 (26) | 10 of 27 (5 to 15) | 0.020 | -112 (23) | 7 of 27 (3 to 12) |
| results/pi05/all_seen_mlp | mlp_physall_cusum | 0.052 | -24 (26) | 9 of 27 (4 to 14) | 0.019 | -124 (22) | 6 of 27 (2 to 10) |
| results/pi05/all_seen_gru | progress | 0.047 | -96 (24) | 6 of 27 (2 to 10) | 0.020 | -160 (21) | 1 of 27 (0 to 3) |
| results/pi05/all_seen_gru | gru | 0.054 | -60 (24) | 6 of 27 (2 to 10) | 0.025 | -128 (22) | 3 of 27 (0 to 6) |
| results/pi05/all_seen_gru | gru_cusum | 0.053 | -40 (24) | 6 of 27 (2 to 10) | 0.028 | -128 (22) | 3 of 27 (0 to 6) |
| results/pi05/all_seen_gru | gru_phys | 0.053 | -56 (23) | 10 of 27 (5 to 15) | 0.023 | -60 (20) | 8 of 27 (4 to 13) |
| results/pi05/all_seen_gru | gru_phys_cusum | 0.051 | -12 (24) | 12 of 27 (7 to 17) | 0.018 | -76 (20) | 8 of 27 (4 to 13) |
| results/pi05/all_seen_gru | gru_physvla | 0.031 | -72 (23) | 10 of 27 (5 to 15) | 0.014 | -100 (22) | 9 of 27 (4 to 14) |
| results/pi05/all_seen_gru | gru_physvla_cusum | 0.032 | -72 (23) | 10 of 27 (5 to 15) | 0.015 | -96 (22) | 9 of 27 (4 to 14) |
| results/pi05/all_seen_gru | gru_physall | 0.052 | -64 (25) | 9 of 27 (4 to 14) | 0.027 | -128 (23) | 7 of 27 (3 to 12) |
| results/pi05/all_seen_gru | gru_physall_cusum | 0.052 | -68 (24) | 9 of 27 (4 to 14) | 0.030 | -112 (24) | 7 of 27 (3 to 12) |
| results/pi05/all_seen_conv | progress | 0.047 | -96 (24) | 6 of 27 (2 to 10) | 0.020 | -160 (21) | 1 of 27 (0 to 3) |
| results/pi05/all_seen_conv | conv | 0.044 | -36 (24) | 8 of 27 (4 to 13) | 0.022 | -140 (24) | 5 of 27 (1 to 9) |
| results/pi05/all_seen_conv | conv_cusum | 0.045 | -32 (24) | 8 of 27 (4 to 13) | 0.022 | -116 (24) | 5 of 27 (1 to 9) |
| results/pi05/all_seen_conv | conv_phys | 0.052 | -64 (21) | 9 of 27 (4 to 14) | 0.026 | -96 (20) | 7 of 27 (3 to 11) |
| results/pi05/all_seen_conv | conv_phys_cusum | 0.052 | -44 (22) | 10 of 27 (5 to 15) | 0.024 | -88 (21) | 9 of 27 (4 to 14) |
| results/pi05/all_seen_conv | conv_physvla | 0.046 | -24 (25) | 11 of 27 (6 to 16) | 0.023 | -104 (23) | 9 of 27 (4 to 14) |
| results/pi05/all_seen_conv | conv_physvla_cusum | 0.046 | -24 (25) | 11 of 27 (6 to 16) | 0.025 | -96 (23) | 9 of 27 (4 to 14) |
| results/pi05/all_seen_conv | conv_physall | 0.048 | -56 (25) | 10 of 27 (5 to 15) | 0.022 | -56 (23) | 8 of 27 (4 to 13) |
| results/pi05/all_seen_conv | conv_physall_cusum | 0.045 | -32 (25) | 10 of 27 (5 to 15) | 0.022 | -56 (23) | 8 of 27 (4 to 13) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/pi05/all_seen_mlp | progress | 1 of 27 (0 to 3) | 20 / 6 |  | +160 (21) | 19 of 928 (0.020) | 6 of 7 | 0.017 of 475 / 0.024 of 453 |
| results/pi05/all_seen_mlp | mlp | 5 of 27 (1 to 9) | 17 / 5 | +4 (+1 to +8) | +44 (22) | 22 of 928 (0.024) | 3 of 7 | 0.013 of 475 / 0.035 of 453 |
| results/pi05/all_seen_mlp | combined | 8 of 27 (4 to 13) | 16 / 3 | +7 (+3 to +12) | +80 (24) | 41 of 928 (0.044) | 5 of 7 | 0.023 of 475 / 0.066 of 453 |
| results/pi05/all_seen_mlp | mlp_cusum | 4 of 27 (1 to 8) | 18 / 5 | +3 (+0 to +7) | +56 (22) | 22 of 928 (0.024) | 3 of 7 | 0.013 of 475 / 0.035 of 453 |
| results/pi05/all_seen_mlp | combined_cusum | 7 of 27 (3 to 12) | 17 / 3 | +6 (+2 to +11) | +92 (24) | 35 of 928 (0.038) | 5 of 7 | 0.023 of 475 / 0.053 of 453 |
| results/pi05/all_seen_mlp | mlp_phys | 8 of 27 (4 to 13) | 10 / 9 | +7 (+3 to +12) | +68 (18) | 25 of 928 (0.027) | 1 of 7 | 0.023 of 475 / 0.031 of 453 |
| results/pi05/all_seen_mlp | mlp_phys_cusum | 1 of 27 (0 to 3) | 9 / 17 | +0 (-3 to +3) | +116 (10) | 19 of 928 (0.020) | 0 of 7 | 0.017 of 475 / 0.024 of 453 |
| results/pi05/all_seen_mlp | mlp_physvla | 8 of 27 (4 to 13) | 13 / 6 | +7 (+3 to +12) | +32 (21) | 20 of 928 (0.022) | 3 of 7 | 0.013 of 475 / 0.031 of 453 |
| results/pi05/all_seen_mlp | mlp_physvla_cusum | 7 of 27 (3 to 12) | 14 / 6 | +6 (+2 to +11) | +48 (21) | 20 of 928 (0.022) | 3 of 7 | 0.013 of 475 / 0.031 of 453 |
| results/pi05/all_seen_mlp | mlp_physall | 7 of 27 (3 to 12) | 16 / 4 | +6 (+2 to +10) | +112 (23) | 19 of 928 (0.020) | 3 of 7 | 0.013 of 475 / 0.029 of 453 |
| results/pi05/all_seen_mlp | mlp_physall_cusum | 6 of 27 (2 to 11) | 16 / 5 | +5 (+1 to +9) | +124 (22) | 18 of 928 (0.019) | 3 of 7 | 0.013 of 475 / 0.026 of 453 |
| results/pi05/all_seen_gru | progress | 1 of 27 (0 to 3) | 20 / 6 |  | +160 (21) | 19 of 928 (0.020) | 6 of 7 | 0.017 of 475 / 0.024 of 453 |
| results/pi05/all_seen_gru | gru | 3 of 27 (0 to 6) | 19 / 5 | +2 (-2 to +6) | +128 (22) | 23 of 928 (0.025) | 4 of 7 | 0.011 of 475 / 0.040 of 453 |
| results/pi05/all_seen_gru | gru_cusum | 3 of 27 (0 to 6) | 19 / 5 | +2 (-2 to +6) | +128 (22) | 26 of 928 (0.028) | 4 of 7 | 0.011 of 475 / 0.046 of 453 |
| results/pi05/all_seen_gru | gru_phys | 8 of 27 (4 to 13) | 12 / 7 | +7 (+3 to +12) | +60 (20) | 21 of 928 (0.023) | 2 of 7 | 0.011 of 475 / 0.035 of 453 |
| results/pi05/all_seen_gru | gru_phys_cusum | 8 of 27 (4 to 13) | 12 / 7 | +7 (+3 to +12) | +76 (20) | 17 of 928 (0.018) | 2 of 7 | 0.008 of 475 / 0.029 of 453 |
| results/pi05/all_seen_gru | gru_physvla | 9 of 27 (4 to 14) | 13 / 5 | +8 (+4 to +13) | +100 (22) | 13 of 928 (0.014) | 2 of 7 | 0.008 of 475 / 0.020 of 453 |
| results/pi05/all_seen_gru | gru_physvla_cusum | 9 of 27 (4 to 14) | 13 / 5 | +8 (+4 to +13) | +96 (22) | 14 of 928 (0.015) | 2 of 7 | 0.008 of 475 / 0.022 of 453 |
| results/pi05/all_seen_gru | gru_physall | 7 of 27 (3 to 12) | 16 / 4 | +6 (+2 to +10) | +128 (23) | 25 of 928 (0.027) | 4 of 7 | 0.013 of 475 / 0.042 of 453 |
| results/pi05/all_seen_gru | gru_physall_cusum | 7 of 27 (3 to 12) | 17 / 3 | +6 (+2 to +10) | +112 (24) | 28 of 928 (0.030) | 4 of 7 | 0.021 of 475 / 0.040 of 453 |
| results/pi05/all_seen_conv | progress | 1 of 27 (0 to 3) | 20 / 6 |  | +160 (21) | 19 of 928 (0.020) | 6 of 7 | 0.017 of 475 / 0.024 of 453 |
| results/pi05/all_seen_conv | conv | 5 of 27 (1 to 9) | 19 / 3 | +4 (+1 to +8) | +140 (24) | 20 of 928 (0.022) | 3 of 7 | 0.011 of 475 / 0.033 of 453 |
| results/pi05/all_seen_conv | conv_cusum | 5 of 27 (1 to 9) | 19 / 3 | +4 (+1 to +8) | +116 (24) | 20 of 928 (0.022) | 3 of 7 | 0.011 of 475 / 0.033 of 453 |
| results/pi05/all_seen_conv | conv_phys | 7 of 27 (3 to 12) | 13 / 7 | +6 (+2 to +10) | +96 (20) | 24 of 928 (0.026) | 2 of 7 | 0.011 of 475 / 0.042 of 453 |
| results/pi05/all_seen_conv | conv_phys_cusum | 9 of 27 (4 to 14) | 12 / 6 | +8 (+4 to +13) | +88 (21) | 22 of 928 (0.024) | 1 of 7 | 0.015 of 475 / 0.033 of 453 |
| results/pi05/all_seen_conv | conv_physvla | 9 of 27 (4 to 14) | 14 / 4 | +8 (+4 to +13) | +104 (23) | 21 of 928 (0.023) | 2 of 7 | 0.019 of 475 / 0.026 of 453 |
| results/pi05/all_seen_conv | conv_physvla_cusum | 9 of 27 (4 to 14) | 14 / 4 | +8 (+4 to +13) | +96 (23) | 23 of 928 (0.025) | 3 of 7 | 0.017 of 475 / 0.033 of 453 |
| results/pi05/all_seen_conv | conv_physall | 8 of 27 (4 to 13) | 15 / 4 | +7 (+3 to +12) | +56 (23) | 20 of 928 (0.022) | 3 of 7 | 0.019 of 475 / 0.024 of 453 |
| results/pi05/all_seen_conv | conv_physall_cusum | 8 of 27 (4 to 13) | 15 / 4 | +7 (+3 to +12) | +56 (23) | 20 of 928 (0.022) | 3 of 7 | 0.017 of 475 / 0.026 of 453 |
