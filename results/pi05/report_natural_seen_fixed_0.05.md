# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/pi05/natural_seen_mlp | progress | 0.046 | -40 (5) | 1 of 5 (0 to 3) | 0.019 | -104 (5) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_mlp | mlp | 0.051 | -72 (4) | 1 of 5 (0 to 3) | 0.025 | -184 (3) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_mlp | combined | 0.051 | -56 (4) | 1 of 5 (0 to 3) | 0.025 | -68 (4) | 1 of 5 (0 to 3) |
| results/pi05/natural_seen_mlp | mlp_cusum | 0.046 | -72 (4) | 1 of 5 (0 to 3) | 0.025 | -184 (3) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_mlp | combined_cusum | 0.053 | -56 (4) | 1 of 5 (0 to 3) | 0.029 | -68 (4) | 1 of 5 (0 to 3) |
| results/pi05/natural_seen_mlp | mlp_phys | 0.059 | -64 (4) | 1 of 5 (0 to 3) | 0.023 | -164 (4) | 1 of 5 (0 to 3) |
| results/pi05/natural_seen_mlp | mlp_phys_cusum | 0.044 | -64 (4) | 1 of 5 (0 to 3) | 0.027 | -112 (4) | 1 of 5 (0 to 3) |
| results/pi05/natural_seen_mlp | mlp_physvla | 0.053 | -84 (4) | 1 of 5 (0 to 3) | 0.019 | -184 (3) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_mlp | mlp_physvla_cusum | 0.051 | -80 (4) | 1 of 5 (0 to 3) | 0.019 | -184 (3) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_mlp | mlp_physall | 0.053 | -56 (4) | 1 of 5 (0 to 3) | 0.029 | -72 (4) | 1 of 5 (0 to 3) |
| results/pi05/natural_seen_mlp | mlp_physall_cusum | 0.059 | -56 (4) | 1 of 5 (0 to 3) | 0.029 | -72 (4) | 1 of 5 (0 to 3) |
| results/pi05/natural_seen_gru | progress | 0.046 | -40 (5) | 1 of 5 (0 to 3) | 0.019 | -104 (5) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_gru | gru | 0.040 | -144 (4) | 0 of 5 (0 to 0) | 0.027 | -152 (4) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_gru | gru_cusum | 0.053 | -140 (4) | 1 of 5 (0 to 3) | 0.025 | -152 (4) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_gru | gru_phys | 0.044 | -16 (4) | 2 of 5 (0 to 4) | 0.021 | -24 (4) | 2 of 5 (0 to 4) |
| results/pi05/natural_seen_gru | gru_phys_cusum | 0.051 | -12 (4) | 2 of 5 (0 to 4) | 0.021 | -144 (4) | 1 of 5 (0 to 3) |
| results/pi05/natural_seen_gru | gru_physvla | 0.048 | -152 (4) | 0 of 5 (0 to 0) | 0.021 | -160 (4) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_gru | gru_physvla_cusum | 0.046 | -72 (4) | 1 of 5 (0 to 3) | 0.025 | -156 (4) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_gru | gru_physall | 0.042 | -80 (4) | 1 of 5 (0 to 3) | 0.019 | -100 (4) | 1 of 5 (0 to 3) |
| results/pi05/natural_seen_gru | gru_physall_cusum | 0.040 | -80 (4) | 1 of 5 (0 to 3) | 0.019 | -100 (4) | 1 of 5 (0 to 3) |
| results/pi05/natural_seen_conv | progress | 0.046 | -40 (5) | 1 of 5 (0 to 3) | 0.019 | -104 (5) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_conv | conv | 0.055 | -108 (4) | 1 of 5 (0 to 3) | 0.021 | -136 (4) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_conv | conv_cusum | 0.055 | -104 (4) | 1 of 5 (0 to 3) | 0.025 | -136 (4) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_conv | conv_phys | 0.061 | -60 (4) | 2 of 5 (0 to 4) | 0.021 | -76 (4) | 2 of 5 (0 to 4) |
| results/pi05/natural_seen_conv | conv_phys_cusum | 0.053 | -52 (4) | 2 of 5 (0 to 4) | 0.019 | -84 (4) | 2 of 5 (0 to 4) |
| results/pi05/natural_seen_conv | conv_physvla | 0.053 | -144 (4) | 1 of 5 (0 to 3) | 0.021 | -156 (4) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_conv | conv_physvla_cusum | 0.051 | -144 (4) | 1 of 5 (0 to 3) | 0.023 | -152 (4) | 0 of 5 (0 to 0) |
| results/pi05/natural_seen_conv | conv_physall | 0.053 | -112 (5) | 1 of 5 (0 to 3) | 0.023 | -100 (4) | 1 of 5 (0 to 3) |
| results/pi05/natural_seen_conv | conv_physall_cusum | 0.059 | -112 (5) | 1 of 5 (0 to 3) | 0.023 | -100 (4) | 1 of 5 (0 to 3) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.05

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/pi05/natural_seen_mlp | progress | 1 of 5 (0 to 3) | 4 / 0 |  | +40 (5) | 22 of 475 (0.046) | 3 of 3 | 0.046 of 475 / none |
| results/pi05/natural_seen_mlp | mlp | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +72 (4) | 24 of 475 (0.051) | 0 of 3 | 0.051 of 475 / none |
| results/pi05/natural_seen_mlp | combined | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +56 (4) | 24 of 475 (0.051) | 0 of 3 | 0.051 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_cusum | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +72 (4) | 22 of 475 (0.046) | 0 of 3 | 0.046 of 475 / none |
| results/pi05/natural_seen_mlp | combined_cusum | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +56 (4) | 25 of 475 (0.053) | 0 of 3 | 0.053 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_phys | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +64 (4) | 28 of 475 (0.059) | 0 of 3 | 0.059 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_phys_cusum | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +64 (4) | 21 of 475 (0.044) | 0 of 3 | 0.044 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_physvla | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +84 (4) | 25 of 475 (0.053) | 0 of 3 | 0.053 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_physvla_cusum | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +80 (4) | 24 of 475 (0.051) | 0 of 3 | 0.051 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_physall | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +56 (4) | 25 of 475 (0.053) | 0 of 3 | 0.053 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_physall_cusum | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +56 (4) | 28 of 475 (0.059) | 0 of 3 | 0.059 of 475 / none |
| results/pi05/natural_seen_gru | progress | 1 of 5 (0 to 3) | 4 / 0 |  | +40 (5) | 22 of 475 (0.046) | 3 of 3 | 0.046 of 475 / none |
| results/pi05/natural_seen_gru | gru | 0 of 5 (0 to 0) | 4 / 1 | -1 (-3 to +0) | +144 (4) | 19 of 475 (0.040) | 0 of 3 | 0.040 of 475 / none |
| results/pi05/natural_seen_gru | gru_cusum | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +140 (4) | 25 of 475 (0.053) | 1 of 3 | 0.053 of 475 / none |
| results/pi05/natural_seen_gru | gru_phys | 2 of 5 (0 to 4) | 2 / 1 | +1 (+0 to +3) | +16 (4) | 21 of 475 (0.044) | 0 of 3 | 0.044 of 475 / none |
| results/pi05/natural_seen_gru | gru_phys_cusum | 2 of 5 (0 to 4) | 2 / 1 | +1 (+0 to +3) | +12 (4) | 24 of 475 (0.051) | 0 of 3 | 0.051 of 475 / none |
| results/pi05/natural_seen_gru | gru_physvla | 0 of 5 (0 to 0) | 4 / 1 | -1 (-3 to +0) | +152 (4) | 23 of 475 (0.048) | 0 of 3 | 0.048 of 475 / none |
| results/pi05/natural_seen_gru | gru_physvla_cusum | 1 of 5 (0 to 3) | 3 / 1 | +0 (-3 to +3) | +72 (4) | 22 of 475 (0.046) | 1 of 3 | 0.046 of 475 / none |
| results/pi05/natural_seen_gru | gru_physall | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +80 (4) | 20 of 475 (0.042) | 1 of 3 | 0.042 of 475 / none |
| results/pi05/natural_seen_gru | gru_physall_cusum | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +80 (4) | 19 of 475 (0.040) | 1 of 3 | 0.040 of 475 / none |
| results/pi05/natural_seen_conv | progress | 1 of 5 (0 to 3) | 4 / 0 |  | +40 (5) | 22 of 475 (0.046) | 3 of 3 | 0.046 of 475 / none |
| results/pi05/natural_seen_conv | conv | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +108 (4) | 26 of 475 (0.055) | 1 of 3 | 0.055 of 475 / none |
| results/pi05/natural_seen_conv | conv_cusum | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +104 (4) | 26 of 475 (0.055) | 1 of 3 | 0.055 of 475 / none |
| results/pi05/natural_seen_conv | conv_phys | 2 of 5 (0 to 4) | 2 / 1 | +1 (+0 to +3) | +60 (4) | 29 of 475 (0.061) | 0 of 3 | 0.061 of 475 / none |
| results/pi05/natural_seen_conv | conv_phys_cusum | 2 of 5 (0 to 4) | 2 / 1 | +1 (+0 to +3) | +52 (4) | 25 of 475 (0.053) | 0 of 3 | 0.053 of 475 / none |
| results/pi05/natural_seen_conv | conv_physvla | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +144 (4) | 25 of 475 (0.053) | 1 of 3 | 0.053 of 475 / none |
| results/pi05/natural_seen_conv | conv_physvla_cusum | 1 of 5 (0 to 3) | 3 / 1 | +0 (+0 to +0) | +144 (4) | 24 of 475 (0.051) | 1 of 3 | 0.051 of 475 / none |
| results/pi05/natural_seen_conv | conv_physall | 1 of 5 (0 to 3) | 4 / 0 | +0 (+0 to +0) | +112 (5) | 25 of 475 (0.053) | 1 of 3 | 0.053 of 475 / none |
| results/pi05/natural_seen_conv | conv_physall_cusum | 1 of 5 (0 to 3) | 4 / 0 | +0 (+0 to +0) | +112 (5) | 28 of 475 (0.059) | 1 of 3 | 0.059 of 475 / none |
