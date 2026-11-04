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

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/pi05/natural_seen_mlp | progress | 0 of 5 (0 to 0) | 5 / 0 |  | +104 (5) | 9 of 475 (0.019) | 3 of 3 | 0.019 of 475 / none |
| results/pi05/natural_seen_mlp | mlp | 0 of 5 (0 to 0) | 3 / 2 | +0 (+0 to +0) | +184 (3) | 12 of 475 (0.025) | 0 of 3 | 0.025 of 475 / none |
| results/pi05/natural_seen_mlp | combined | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +68 (4) | 12 of 475 (0.025) | 0 of 3 | 0.025 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_cusum | 0 of 5 (0 to 0) | 3 / 2 | +0 (+0 to +0) | +184 (3) | 12 of 475 (0.025) | 0 of 3 | 0.025 of 475 / none |
| results/pi05/natural_seen_mlp | combined_cusum | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +68 (4) | 14 of 475 (0.029) | 0 of 3 | 0.029 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_phys | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +164 (4) | 11 of 475 (0.023) | 0 of 3 | 0.023 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_phys_cusum | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +112 (4) | 13 of 475 (0.027) | 0 of 3 | 0.027 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_physvla | 0 of 5 (0 to 0) | 3 / 2 | +0 (+0 to +0) | +184 (3) | 9 of 475 (0.019) | 0 of 3 | 0.019 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_physvla_cusum | 0 of 5 (0 to 0) | 3 / 2 | +0 (+0 to +0) | +184 (3) | 9 of 475 (0.019) | 0 of 3 | 0.019 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_physall | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +72 (4) | 14 of 475 (0.029) | 0 of 3 | 0.029 of 475 / none |
| results/pi05/natural_seen_mlp | mlp_physall_cusum | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +72 (4) | 14 of 475 (0.029) | 0 of 3 | 0.029 of 475 / none |
| results/pi05/natural_seen_gru | progress | 0 of 5 (0 to 0) | 5 / 0 |  | +104 (5) | 9 of 475 (0.019) | 3 of 3 | 0.019 of 475 / none |
| results/pi05/natural_seen_gru | gru | 0 of 5 (0 to 0) | 4 / 1 | +0 (+0 to +0) | +152 (4) | 13 of 475 (0.027) | 0 of 3 | 0.027 of 475 / none |
| results/pi05/natural_seen_gru | gru_cusum | 0 of 5 (0 to 0) | 4 / 1 | +0 (+0 to +0) | +152 (4) | 12 of 475 (0.025) | 0 of 3 | 0.025 of 475 / none |
| results/pi05/natural_seen_gru | gru_phys | 2 of 5 (0 to 4) | 2 / 1 | +2 (+0 to +4) | +24 (4) | 10 of 475 (0.021) | 0 of 3 | 0.021 of 475 / none |
| results/pi05/natural_seen_gru | gru_phys_cusum | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +144 (4) | 10 of 475 (0.021) | 0 of 3 | 0.021 of 475 / none |
| results/pi05/natural_seen_gru | gru_physvla | 0 of 5 (0 to 0) | 4 / 1 | +0 (+0 to +0) | +160 (4) | 10 of 475 (0.021) | 0 of 3 | 0.021 of 475 / none |
| results/pi05/natural_seen_gru | gru_physvla_cusum | 0 of 5 (0 to 0) | 4 / 1 | +0 (+0 to +0) | +156 (4) | 12 of 475 (0.025) | 0 of 3 | 0.025 of 475 / none |
| results/pi05/natural_seen_gru | gru_physall | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +100 (4) | 9 of 475 (0.019) | 0 of 3 | 0.019 of 475 / none |
| results/pi05/natural_seen_gru | gru_physall_cusum | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +100 (4) | 9 of 475 (0.019) | 0 of 3 | 0.019 of 475 / none |
| results/pi05/natural_seen_conv | progress | 0 of 5 (0 to 0) | 5 / 0 |  | +104 (5) | 9 of 475 (0.019) | 3 of 3 | 0.019 of 475 / none |
| results/pi05/natural_seen_conv | conv | 0 of 5 (0 to 0) | 4 / 1 | +0 (+0 to +0) | +136 (4) | 10 of 475 (0.021) | 0 of 3 | 0.021 of 475 / none |
| results/pi05/natural_seen_conv | conv_cusum | 0 of 5 (0 to 0) | 4 / 1 | +0 (+0 to +0) | +136 (4) | 12 of 475 (0.025) | 0 of 3 | 0.025 of 475 / none |
| results/pi05/natural_seen_conv | conv_phys | 2 of 5 (0 to 4) | 2 / 1 | +2 (+0 to +4) | +76 (4) | 10 of 475 (0.021) | 0 of 3 | 0.021 of 475 / none |
| results/pi05/natural_seen_conv | conv_phys_cusum | 2 of 5 (0 to 4) | 2 / 1 | +2 (+0 to +4) | +84 (4) | 9 of 475 (0.019) | 0 of 3 | 0.019 of 475 / none |
| results/pi05/natural_seen_conv | conv_physvla | 0 of 5 (0 to 0) | 4 / 1 | +0 (+0 to +0) | +156 (4) | 10 of 475 (0.021) | 0 of 3 | 0.021 of 475 / none |
| results/pi05/natural_seen_conv | conv_physvla_cusum | 0 of 5 (0 to 0) | 4 / 1 | +0 (+0 to +0) | +152 (4) | 11 of 475 (0.023) | 0 of 3 | 0.023 of 475 / none |
| results/pi05/natural_seen_conv | conv_physall | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +100 (4) | 11 of 475 (0.023) | 0 of 3 | 0.023 of 475 / none |
| results/pi05/natural_seen_conv | conv_physall_cusum | 1 of 5 (0 to 3) | 3 / 1 | +1 (+0 to +3) | +100 (4) | 11 of 475 (0.023) | 0 of 3 | 0.023 of 475 / none |
