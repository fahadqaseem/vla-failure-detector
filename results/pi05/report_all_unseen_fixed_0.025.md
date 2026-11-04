# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/pi05/all_unseen_mlp | progress | 0.050 | -104 (24) | 5 of 27 (2 to 9) | 0.025 | -144 (21) | 2 of 27 (0 to 5) |
| results/pi05/all_unseen_mlp | mlp | 0.077 | -192 (10) | 1 of 27 (0 to 3) | 0.050 | -280 (9) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_mlp | combined | 0.046 | -104 (10) | 2 of 27 (0 to 5) | 0.029 | -112 (9) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_mlp | mlp_cusum | 0.074 | -192 (10) | 1 of 27 (0 to 3) | 0.050 | -280 (9) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_mlp | combined_cusum | 0.045 | -104 (10) | 2 of 27 (0 to 5) | 0.029 | -112 (9) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_mlp | mlp_phys | 0.106 | -88 (5) | 1 of 27 (0 to 3) | 0.071 | -96 (5) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_mlp | mlp_phys_cusum | 0.141 | -152 (3) | 0 of 27 (0 to 0) | 0.121 | -120 (2) | 0 of 27 (0 to 0) |
| results/pi05/all_unseen_mlp | mlp_physvla | 0.051 | -64 (9) | 2 of 27 (0 to 5) | 0.015 | -168 (7) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_mlp | mlp_physvla_cusum | 0.053 | -64 (9) | 2 of 27 (0 to 5) | 0.014 | -184 (7) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_mlp | mlp_physall | 0.045 | -96 (12) | 3 of 27 (0 to 7) | 0.024 | -116 (10) | 2 of 27 (0 to 5) |
| results/pi05/all_unseen_mlp | mlp_physall_cusum | 0.045 | -96 (12) | 3 of 27 (0 to 7) | 0.026 | -152 (9) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_gru | progress | 0.050 | -104 (24) | 5 of 27 (2 to 9) | 0.025 | -144 (21) | 2 of 27 (0 to 5) |
| results/pi05/all_unseen_gru | gru | 0.047 | -112 (17) | 5 of 27 (1 to 9) | 0.022 | -184 (15) | 3 of 27 (0 to 6) |
| results/pi05/all_unseen_gru | gru_cusum | 0.050 | -112 (17) | 5 of 27 (1 to 9) | 0.022 | -184 (15) | 3 of 27 (0 to 6) |
| results/pi05/all_unseen_gru | gru_phys | 0.018 | -48 (8) | 4 of 27 (1 to 8) | 0.011 | -108 (8) | 3 of 27 (0 to 6) |
| results/pi05/all_unseen_gru | gru_phys_cusum | 0.153 | +48 (20) | 12 of 27 (7 to 17) | 0.126 | +40 (19) | 12 of 27 (7 to 17) |
| results/pi05/all_unseen_gru | gru_physvla | 0.014 | -48 (12) | 5 of 27 (1 to 9) | 0.003 | -104 (8) | 2 of 27 (0 to 5) |
| results/pi05/all_unseen_gru | gru_physvla_cusum | 0.039 | -80 (7) | 2 of 27 (0 to 5) | 0.018 | -104 (7) | 2 of 27 (0 to 5) |
| results/pi05/all_unseen_gru | gru_physall | 0.087 | +20 (20) | 11 of 27 (6 to 16) | 0.048 | -40 (17) | 7 of 27 (3 to 12) |
| results/pi05/all_unseen_gru | gru_physall_cusum | 0.112 | -80 (19) | 8 of 27 (4 to 13) | 0.080 | -72 (16) | 6 of 27 (2 to 10) |
| results/pi05/all_unseen_conv | progress | 0.050 | -104 (24) | 5 of 27 (2 to 9) | 0.025 | -144 (21) | 2 of 27 (0 to 5) |
| results/pi05/all_unseen_conv | conv | 0.048 | -140 (12) | 3 of 27 (0 to 6) | 0.029 | -176 (9) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_conv | conv_cusum | 0.047 | -112 (13) | 3 of 27 (0 to 6) | 0.025 | -148 (10) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_conv | conv_phys | 0.015 | -36 (6) | 3 of 27 (0 to 6) | 0.010 | -112 (5) | 1 of 27 (0 to 3) |
| results/pi05/all_unseen_conv | conv_phys_cusum | 0.218 | +88 (15) | 8 of 27 (4 to 13) | 0.139 | -36 (14) | 6 of 27 (2 to 10) |
| results/pi05/all_unseen_conv | conv_physvla | 0.039 | -56 (13) | 5 of 27 (1 to 9) | 0.018 | -72 (9) | 2 of 27 (0 to 5) |
| results/pi05/all_unseen_conv | conv_physvla_cusum | 0.086 | -48 (13) | 5 of 27 (1 to 9) | 0.048 | -72 (11) | 3 of 27 (0 to 7) |
| results/pi05/all_unseen_conv | conv_physall | 0.024 | -120 (16) | 6 of 27 (2 to 10) | 0.010 | -136 (15) | 4 of 27 (1 to 8) |
| results/pi05/all_unseen_conv | conv_physall_cusum | 0.056 | +0 (17) | 9 of 27 (4 to 14) | 0.034 | -40 (17) | 7 of 27 (3 to 12) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/pi05/all_unseen_mlp | progress | 2 of 27 (0 to 5) | 19 / 6 |  | +144 (21) | 23 of 928 (0.025) | 6 of 7 | 0.021 of 475 / 0.029 of 453 |
| results/pi05/all_unseen_mlp | mlp | 1 of 27 (0 to 3) | 8 / 18 | -1 (-4 to +2) | +280 (9) | 46 of 928 (0.050) | 2 of 7 | 0.084 of 475 / 0.013 of 453 |
| results/pi05/all_unseen_mlp | combined | 1 of 27 (0 to 3) | 8 / 18 | -1 (-4 to +2) | +112 (9) | 27 of 928 (0.029) | 4 of 7 | 0.023 of 475 / 0.035 of 453 |
| results/pi05/all_unseen_mlp | mlp_cusum | 1 of 27 (0 to 3) | 8 / 18 | -1 (-4 to +2) | +280 (9) | 46 of 928 (0.050) | 2 of 7 | 0.084 of 475 / 0.013 of 453 |
| results/pi05/all_unseen_mlp | combined_cusum | 1 of 27 (0 to 3) | 8 / 18 | -1 (-4 to +2) | +112 (9) | 27 of 928 (0.029) | 4 of 7 | 0.023 of 475 / 0.035 of 453 |
| results/pi05/all_unseen_mlp | mlp_phys | 1 of 27 (0 to 3) | 4 / 22 | -1 (-4 to +2) | +96 (5) | 66 of 928 (0.071) | 1 of 7 | 0.046 of 475 / 0.097 of 453 |
| results/pi05/all_unseen_mlp | mlp_phys_cusum | 0 of 27 (0 to 0) | 2 / 25 | -2 (-5 to +0) | +120 (2) | 112 of 928 (0.121) | 1 of 7 | 0.093 of 475 / 0.150 of 453 |
| results/pi05/all_unseen_mlp | mlp_physvla | 1 of 27 (0 to 3) | 6 / 20 | -1 (-4 to +2) | +168 (7) | 14 of 928 (0.015) | 2 of 7 | 0.017 of 475 / 0.013 of 453 |
| results/pi05/all_unseen_mlp | mlp_physvla_cusum | 1 of 27 (0 to 3) | 6 / 20 | -1 (-4 to +2) | +184 (7) | 13 of 928 (0.014) | 2 of 7 | 0.017 of 475 / 0.011 of 453 |
| results/pi05/all_unseen_mlp | mlp_physall | 2 of 27 (0 to 5) | 8 / 17 | +0 (-3 to +3) | +116 (10) | 22 of 928 (0.024) | 1 of 7 | 0.017 of 475 / 0.031 of 453 |
| results/pi05/all_unseen_mlp | mlp_physall_cusum | 1 of 27 (0 to 3) | 8 / 18 | -1 (-3 to +0) | +152 (9) | 24 of 928 (0.026) | 1 of 7 | 0.019 of 475 / 0.033 of 453 |
| results/pi05/all_unseen_gru | progress | 2 of 27 (0 to 5) | 19 / 6 |  | +144 (21) | 23 of 928 (0.025) | 6 of 7 | 0.021 of 475 / 0.029 of 453 |
| results/pi05/all_unseen_gru | gru | 3 of 27 (0 to 6) | 12 / 12 | +1 (-3 to +5) | +184 (15) | 20 of 928 (0.022) | 4 of 7 | 0.021 of 475 / 0.022 of 453 |
| results/pi05/all_unseen_gru | gru_cusum | 3 of 27 (0 to 6) | 12 / 12 | +1 (-3 to +5) | +184 (15) | 20 of 928 (0.022) | 4 of 7 | 0.023 of 475 / 0.020 of 453 |
| results/pi05/all_unseen_gru | gru_phys | 3 of 27 (0 to 6) | 5 / 19 | +1 (-3 to +5) | +108 (8) | 10 of 928 (0.011) | 1 of 7 | 0.004 of 475 / 0.018 of 453 |
| results/pi05/all_unseen_gru | gru_phys_cusum | 12 of 27 (7 to 17) | 7 / 8 | +10 (+5 to +15) | -40 (19) | 117 of 928 (0.126) | 1 of 7 | 0.097 of 475 / 0.157 of 453 |
| results/pi05/all_unseen_gru | gru_physvla | 2 of 27 (0 to 5) | 6 / 19 | +0 (-4 to +4) | +104 (8) | 3 of 928 (0.003) | 1 of 7 | 0.002 of 475 / 0.004 of 453 |
| results/pi05/all_unseen_gru | gru_physvla_cusum | 2 of 27 (0 to 5) | 5 / 20 | +0 (-4 to +4) | +104 (7) | 17 of 928 (0.018) | 1 of 7 | 0.008 of 475 / 0.029 of 453 |
| results/pi05/all_unseen_gru | gru_physall | 7 of 27 (3 to 12) | 10 / 10 | +5 (+0 to +10) | +40 (17) | 45 of 928 (0.048) | 4 of 7 | 0.021 of 475 / 0.077 of 453 |
| results/pi05/all_unseen_gru | gru_physall_cusum | 6 of 27 (2 to 10) | 10 / 11 | +4 (+0 to +9) | +72 (16) | 74 of 928 (0.080) | 5 of 7 | 0.046 of 475 / 0.115 of 453 |
| results/pi05/all_unseen_conv | progress | 2 of 27 (0 to 5) | 19 / 6 |  | +144 (21) | 23 of 928 (0.025) | 6 of 7 | 0.021 of 475 / 0.029 of 453 |
| results/pi05/all_unseen_conv | conv | 1 of 27 (0 to 3) | 8 / 18 | -1 (-4 to +2) | +176 (9) | 27 of 928 (0.029) | 4 of 7 | 0.032 of 475 / 0.026 of 453 |
| results/pi05/all_unseen_conv | conv_cusum | 1 of 27 (0 to 3) | 9 / 17 | -1 (-4 to +2) | +148 (10) | 23 of 928 (0.025) | 4 of 7 | 0.019 of 475 / 0.031 of 453 |
| results/pi05/all_unseen_conv | conv_phys | 1 of 27 (0 to 3) | 4 / 22 | -1 (-4 to +2) | +112 (5) | 9 of 928 (0.010) | 1 of 7 | 0.002 of 475 / 0.018 of 453 |
| results/pi05/all_unseen_conv | conv_phys_cusum | 6 of 27 (2 to 10) | 8 / 13 | +4 (+0 to +9) | +36 (14) | 129 of 928 (0.139) | 1 of 7 | 0.088 of 475 / 0.192 of 453 |
| results/pi05/all_unseen_conv | conv_physvla | 2 of 27 (0 to 5) | 7 / 18 | +0 (-4 to +4) | +72 (9) | 17 of 928 (0.018) | 1 of 7 | 0.008 of 475 / 0.029 of 453 |
| results/pi05/all_unseen_conv | conv_physvla_cusum | 3 of 27 (0 to 7) | 8 / 16 | +1 (-2 to +4) | +72 (11) | 45 of 928 (0.048) | 1 of 7 | 0.029 of 475 / 0.068 of 453 |
| results/pi05/all_unseen_conv | conv_physall | 4 of 27 (1 to 8) | 11 / 12 | +2 (-2 to +6) | +136 (15) | 9 of 928 (0.010) | 5 of 7 | 0.006 of 475 / 0.013 of 453 |
| results/pi05/all_unseen_conv | conv_physall_cusum | 7 of 27 (3 to 12) | 10 / 10 | +5 (+0 to +10) | +40 (17) | 32 of 928 (0.034) | 5 of 7 | 0.023 of 475 / 0.046 of 453 |
