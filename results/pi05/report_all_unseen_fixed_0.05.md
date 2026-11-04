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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/pi05/all_unseen_mlp | progress | 5 of 27 (1 to 9) | 19 / 3 |  | +104 (24) | 46 of 928 (0.050) | 6 of 7 | 0.040 of 475 / 0.060 of 453 |
| results/pi05/all_unseen_mlp | mlp | 1 of 27 (0 to 3) | 9 / 17 | -4 (-9 to +0) | +192 (10) | 71 of 928 (0.077) | 3 of 7 | 0.116 of 475 / 0.035 of 453 |
| results/pi05/all_unseen_mlp | combined | 2 of 27 (0 to 5) | 8 / 17 | -3 (-8 to +2) | +104 (10) | 43 of 928 (0.046) | 5 of 7 | 0.048 of 475 / 0.044 of 453 |
| results/pi05/all_unseen_mlp | mlp_cusum | 1 of 27 (0 to 3) | 9 / 17 | -4 (-9 to +0) | +192 (10) | 69 of 928 (0.074) | 3 of 7 | 0.114 of 475 / 0.033 of 453 |
| results/pi05/all_unseen_mlp | combined_cusum | 2 of 27 (0 to 5) | 8 / 17 | -3 (-8 to +2) | +104 (10) | 42 of 928 (0.045) | 5 of 7 | 0.048 of 475 / 0.042 of 453 |
| results/pi05/all_unseen_mlp | mlp_phys | 1 of 27 (0 to 3) | 4 / 22 | -4 (-9 to +0) | +88 (5) | 98 of 928 (0.106) | 1 of 7 | 0.074 of 475 / 0.139 of 453 |
| results/pi05/all_unseen_mlp | mlp_phys_cusum | 0 of 27 (0 to 0) | 3 / 24 | -5 (-9 to -1) | +152 (3) | 131 of 928 (0.141) | 1 of 7 | 0.103 of 475 / 0.181 of 453 |
| results/pi05/all_unseen_mlp | mlp_physvla | 2 of 27 (0 to 5) | 7 / 18 | -3 (-8 to +2) | +64 (9) | 47 of 928 (0.051) | 2 of 7 | 0.053 of 475 / 0.049 of 453 |
| results/pi05/all_unseen_mlp | mlp_physvla_cusum | 2 of 27 (0 to 5) | 7 / 18 | -3 (-8 to +2) | +64 (9) | 49 of 928 (0.053) | 2 of 7 | 0.053 of 475 / 0.053 of 453 |
| results/pi05/all_unseen_mlp | mlp_physall | 3 of 27 (0 to 7) | 9 / 15 | -2 (-7 to +3) | +96 (12) | 42 of 928 (0.045) | 1 of 7 | 0.038 of 475 / 0.053 of 453 |
| results/pi05/all_unseen_mlp | mlp_physall_cusum | 3 of 27 (0 to 7) | 9 / 15 | -2 (-7 to +3) | +96 (12) | 42 of 928 (0.045) | 1 of 7 | 0.038 of 475 / 0.053 of 453 |
| results/pi05/all_unseen_gru | progress | 5 of 27 (1 to 9) | 19 / 3 |  | +104 (24) | 46 of 928 (0.050) | 6 of 7 | 0.040 of 475 / 0.060 of 453 |
| results/pi05/all_unseen_gru | gru | 5 of 27 (1 to 9) | 12 / 10 | +0 (-5 to +5) | +112 (17) | 44 of 928 (0.047) | 4 of 7 | 0.038 of 475 / 0.057 of 453 |
| results/pi05/all_unseen_gru | gru_cusum | 5 of 27 (1 to 9) | 12 / 10 | +0 (-5 to +5) | +112 (17) | 46 of 928 (0.050) | 4 of 7 | 0.042 of 475 / 0.057 of 453 |
| results/pi05/all_unseen_gru | gru_phys | 4 of 27 (1 to 8) | 4 / 19 | -1 (-6 to +4) | +48 (8) | 17 of 928 (0.018) | 1 of 7 | 0.006 of 475 / 0.031 of 453 |
| results/pi05/all_unseen_gru | gru_phys_cusum | 12 of 27 (7 to 17) | 8 / 7 | +7 (+3 to +12) | -48 (20) | 142 of 928 (0.153) | 1 of 7 | 0.103 of 475 / 0.205 of 453 |
| results/pi05/all_unseen_gru | gru_physvla | 5 of 27 (1 to 9) | 7 / 15 | +0 (-6 to +6) | +48 (12) | 13 of 928 (0.014) | 1 of 7 | 0.006 of 475 / 0.022 of 453 |
| results/pi05/all_unseen_gru | gru_physvla_cusum | 2 of 27 (0 to 5) | 5 / 20 | -3 (-8 to +2) | +80 (7) | 36 of 928 (0.039) | 1 of 7 | 0.017 of 475 / 0.062 of 453 |
| results/pi05/all_unseen_gru | gru_physall | 11 of 27 (6 to 16) | 9 / 7 | +6 (+2 to +10) | -20 (20) | 81 of 928 (0.087) | 5 of 7 | 0.061 of 475 / 0.115 of 453 |
| results/pi05/all_unseen_gru | gru_physall_cusum | 8 of 27 (4 to 13) | 11 / 8 | +3 (-2 to +8) | +80 (19) | 104 of 928 (0.112) | 5 of 7 | 0.072 of 475 / 0.155 of 453 |
| results/pi05/all_unseen_conv | progress | 5 of 27 (1 to 9) | 19 / 3 |  | +104 (24) | 46 of 928 (0.050) | 6 of 7 | 0.040 of 475 / 0.060 of 453 |
| results/pi05/all_unseen_conv | conv | 3 of 27 (0 to 7) | 9 / 15 | -2 (-7 to +3) | +140 (12) | 45 of 928 (0.048) | 6 of 7 | 0.055 of 475 / 0.042 of 453 |
| results/pi05/all_unseen_conv | conv_cusum | 3 of 27 (0 to 7) | 10 / 14 | -2 (-7 to +3) | +112 (13) | 44 of 928 (0.047) | 6 of 7 | 0.046 of 475 / 0.049 of 453 |
| results/pi05/all_unseen_conv | conv_phys | 3 of 27 (0 to 7) | 3 / 21 | -2 (-7 to +3) | +36 (6) | 14 of 928 (0.015) | 1 of 7 | 0.002 of 475 / 0.029 of 453 |
| results/pi05/all_unseen_conv | conv_phys_cusum | 8 of 27 (4 to 13) | 7 / 12 | +3 (-1 to +7) | -88 (15) | 202 of 928 (0.218) | 1 of 7 | 0.143 of 475 / 0.296 of 453 |
| results/pi05/all_unseen_conv | conv_physvla | 5 of 27 (1 to 9) | 8 / 14 | +0 (-4 to +4) | +56 (13) | 36 of 928 (0.039) | 1 of 7 | 0.021 of 475 / 0.057 of 453 |
| results/pi05/all_unseen_conv | conv_physvla_cusum | 5 of 27 (1 to 9) | 8 / 14 | +0 (-5 to +5) | +48 (13) | 80 of 928 (0.086) | 1 of 7 | 0.067 of 475 / 0.106 of 453 |
| results/pi05/all_unseen_conv | conv_physall | 6 of 27 (2 to 10) | 10 / 11 | +1 (-3 to +5) | +120 (16) | 22 of 928 (0.024) | 5 of 7 | 0.021 of 475 / 0.026 of 453 |
| results/pi05/all_unseen_conv | conv_physall_cusum | 9 of 27 (4 to 14) | 8 / 10 | +4 (+0 to +9) | +0 (17) | 52 of 928 (0.056) | 6 of 7 | 0.046 of 475 / 0.066 of 453 |
