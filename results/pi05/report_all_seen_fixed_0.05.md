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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/pi05/all_seen_mlp | progress | 6 of 27 (2 to 11) | 18 / 3 |  | +96 (24) | 44 of 928 (0.047) | 6 of 7 | 0.038 of 475 / 0.057 of 453 |
| results/pi05/all_seen_mlp | mlp | 8 of 27 (4 to 13) | 17 / 2 | +2 (-3 to +8) | +48 (25) | 50 of 928 (0.054) | 6 of 7 | 0.023 of 475 / 0.086 of 453 |
| results/pi05/all_seen_mlp | combined | 9 of 27 (4 to 14) | 16 / 2 | +3 (-1 to +7) | +16 (25) | 89 of 928 (0.096) | 6 of 7 | 0.067 of 475 / 0.126 of 453 |
| results/pi05/all_seen_mlp | mlp_cusum | 7 of 27 (3 to 12) | 18 / 2 | +1 (-4 to +6) | +64 (25) | 47 of 928 (0.051) | 6 of 7 | 0.025 of 475 / 0.077 of 453 |
| results/pi05/all_seen_mlp | combined_cusum | 8 of 27 (4 to 13) | 17 / 2 | +2 (-2 to +6) | +32 (25) | 83 of 928 (0.089) | 6 of 7 | 0.065 of 475 / 0.115 of 453 |
| results/pi05/all_seen_mlp | mlp_phys | 10 of 27 (5 to 15) | 10 / 7 | +4 (+0 to +9) | -12 (20) | 49 of 928 (0.053) | 2 of 7 | 0.036 of 475 / 0.071 of 453 |
| results/pi05/all_seen_mlp | mlp_phys_cusum | 5 of 27 (1 to 9) | 10 / 12 | -1 (-5 to +3) | +64 (15) | 38 of 928 (0.041) | 2 of 7 | 0.034 of 475 / 0.049 of 453 |
| results/pi05/all_seen_mlp | mlp_physvla | 9 of 27 (4 to 14) | 14 / 4 | +3 (-3 to +9) | +40 (23) | 49 of 928 (0.053) | 5 of 7 | 0.029 of 475 / 0.077 of 453 |
| results/pi05/all_seen_mlp | mlp_physvla_cusum | 10 of 27 (5 to 15) | 15 / 2 | +4 (-1 to +9) | +56 (25) | 48 of 928 (0.052) | 5 of 7 | 0.032 of 475 / 0.073 of 453 |
| results/pi05/all_seen_mlp | mlp_physall | 10 of 27 (5 to 15) | 16 / 1 | +4 (-1 to +9) | +24 (26) | 49 of 928 (0.053) | 3 of 7 | 0.034 of 475 / 0.073 of 453 |
| results/pi05/all_seen_mlp | mlp_physall_cusum | 9 of 27 (4 to 14) | 17 / 1 | +3 (-2 to +8) | +24 (26) | 48 of 928 (0.052) | 5 of 7 | 0.034 of 475 / 0.071 of 453 |
| results/pi05/all_seen_gru | progress | 6 of 27 (2 to 11) | 18 / 3 |  | +96 (24) | 44 of 928 (0.047) | 6 of 7 | 0.038 of 475 / 0.057 of 453 |
| results/pi05/all_seen_gru | gru | 6 of 27 (2 to 10) | 18 / 3 | +0 (-6 to +5) | +60 (24) | 50 of 928 (0.054) | 4 of 7 | 0.027 of 475 / 0.082 of 453 |
| results/pi05/all_seen_gru | gru_cusum | 6 of 27 (2 to 10) | 18 / 3 | +0 (-6 to +5) | +40 (24) | 49 of 928 (0.053) | 4 of 7 | 0.023 of 475 / 0.084 of 453 |
| results/pi05/all_seen_gru | gru_phys | 10 of 27 (5 to 15) | 13 / 4 | +4 (-1 to +9) | +56 (23) | 49 of 928 (0.053) | 3 of 7 | 0.023 of 475 / 0.084 of 453 |
| results/pi05/all_seen_gru | gru_phys_cusum | 12 of 27 (7 to 17) | 12 / 3 | +6 (+1 to +11) | +12 (24) | 47 of 928 (0.051) | 2 of 7 | 0.027 of 475 / 0.075 of 453 |
| results/pi05/all_seen_gru | gru_physvla | 10 of 27 (5 to 15) | 13 / 4 | +4 (-1 to +9) | +72 (23) | 29 of 928 (0.031) | 2 of 7 | 0.017 of 475 / 0.046 of 453 |
| results/pi05/all_seen_gru | gru_physvla_cusum | 10 of 27 (5 to 15) | 13 / 4 | +4 (-1 to +9) | +72 (23) | 30 of 928 (0.032) | 2 of 7 | 0.017 of 475 / 0.049 of 453 |
| results/pi05/all_seen_gru | gru_physall | 9 of 27 (4 to 14) | 16 / 2 | +3 (-3 to +9) | +64 (25) | 48 of 928 (0.052) | 4 of 7 | 0.029 of 475 / 0.075 of 453 |
| results/pi05/all_seen_gru | gru_physall_cusum | 9 of 27 (4 to 14) | 15 / 3 | +3 (-2 to +8) | +68 (24) | 48 of 928 (0.052) | 4 of 7 | 0.032 of 475 / 0.073 of 453 |
| results/pi05/all_seen_conv | progress | 6 of 27 (2 to 11) | 18 / 3 |  | +96 (24) | 44 of 928 (0.047) | 6 of 7 | 0.038 of 475 / 0.057 of 453 |
| results/pi05/all_seen_conv | conv | 8 of 27 (4 to 13) | 16 / 3 | +2 (-3 to +7) | +36 (24) | 41 of 928 (0.044) | 4 of 7 | 0.027 of 475 / 0.062 of 453 |
| results/pi05/all_seen_conv | conv_cusum | 8 of 27 (4 to 13) | 16 / 3 | +2 (-3 to +7) | +32 (24) | 42 of 928 (0.045) | 6 of 7 | 0.027 of 475 / 0.064 of 453 |
| results/pi05/all_seen_conv | conv_phys | 9 of 27 (4 to 14) | 12 / 6 | +3 (-2 to +8) | +64 (21) | 48 of 928 (0.052) | 2 of 7 | 0.025 of 475 / 0.079 of 453 |
| results/pi05/all_seen_conv | conv_phys_cusum | 10 of 27 (5 to 15) | 12 / 5 | +4 (+0 to +9) | +44 (22) | 48 of 928 (0.052) | 3 of 7 | 0.032 of 475 / 0.073 of 453 |
| results/pi05/all_seen_conv | conv_physvla | 11 of 27 (6 to 16) | 14 / 2 | +5 (+0 to +11) | +24 (25) | 43 of 928 (0.046) | 4 of 7 | 0.027 of 475 / 0.066 of 453 |
| results/pi05/all_seen_conv | conv_physvla_cusum | 11 of 27 (6 to 16) | 14 / 2 | +5 (+0 to +10) | +24 (25) | 43 of 928 (0.046) | 5 of 7 | 0.029 of 475 / 0.064 of 453 |
| results/pi05/all_seen_conv | conv_physall | 10 of 27 (5 to 15) | 15 / 2 | +4 (-1 to +9) | +56 (25) | 45 of 928 (0.048) | 5 of 7 | 0.034 of 475 / 0.064 of 453 |
| results/pi05/all_seen_conv | conv_physall_cusum | 10 of 27 (5 to 15) | 15 / 2 | +4 (-1 to +9) | +32 (25) | 42 of 928 (0.045) | 5 of 7 | 0.032 of 475 / 0.060 of 453 |
