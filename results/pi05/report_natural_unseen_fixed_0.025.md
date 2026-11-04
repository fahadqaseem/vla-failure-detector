# Headline: episode-level false positive rate on successes, and lead time before t_pnr

Lead = t_pnr - t_alarm (positive = alarm before t_pnr), median over the alarmed failures with t_pnr > 0 (number alarmed in brackets); timely = lead >= 0, with bootstrap 95% interval.

| run | model | FPR fixed 0.05 | lead fixed 0.05 | timely fixed 0.05 | FPR fixed 0.025 | lead fixed 0.025 | timely fixed 0.025 |
|---|---|---|---|---|---|---|---|
| results/pi05/natural_unseen_mlp | progress | 0.046 | -48 (5) | 1 of 5 (0 to 3) | 0.021 | -96 (5) | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_mlp | mlp | 0.088 | none | 0 of 5 (0 to 0) | 0.046 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_mlp | combined | 0.065 | none | 0 of 5 (0 to 0) | 0.027 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_mlp | mlp_cusum | 0.088 | none | 0 of 5 (0 to 0) | 0.046 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_mlp | combined_cusum | 0.063 | none | 0 of 5 (0 to 0) | 0.027 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_mlp | mlp_phys | 0.120 | none | 0 of 5 (0 to 0) | 0.069 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_mlp | mlp_phys_cusum | 0.078 | none | 0 of 5 (0 to 0) | 0.078 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_mlp | mlp_physvla | 0.091 | none | 0 of 5 (0 to 0) | 0.076 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_mlp | mlp_physvla_cusum | 0.091 | none | 0 of 5 (0 to 0) | 0.076 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_mlp | mlp_physall | 0.063 | none | 0 of 5 (0 to 0) | 0.023 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_mlp | mlp_physall_cusum | 0.063 | none | 0 of 5 (0 to 0) | 0.023 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_gru | progress | 0.046 | -48 (5) | 1 of 5 (0 to 3) | 0.021 | -96 (5) | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_gru | gru | 0.032 | none | 0 of 5 (0 to 0) | 0.017 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_gru | gru_cusum | 0.027 | none | 0 of 5 (0 to 0) | 0.015 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_gru | gru_phys | 0.032 | none | 0 of 5 (0 to 0) | 0.013 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_gru | gru_phys_cusum | 0.080 | none | 0 of 5 (0 to 0) | 0.080 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_gru | gru_physvla | 0.021 | none | 0 of 5 (0 to 0) | 0.013 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_gru | gru_physvla_cusum | 0.013 | none | 0 of 5 (0 to 0) | 0.013 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_gru | gru_physall | 0.021 | none | 0 of 5 (0 to 0) | 0.015 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_gru | gru_physall_cusum | 0.019 | none | 0 of 5 (0 to 0) | 0.015 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_conv | progress | 0.046 | -48 (5) | 1 of 5 (0 to 3) | 0.021 | -96 (5) | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_conv | conv | 0.032 | -108 (2) | 0 of 5 (0 to 0) | 0.023 | -116 (2) | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_conv | conv_cusum | 0.032 | -108 (2) | 0 of 5 (0 to 0) | 0.021 | -116 (2) | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_conv | conv_phys | 0.078 | none | 0 of 5 (0 to 0) | 0.076 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_conv | conv_phys_cusum | 0.078 | none | 0 of 5 (0 to 0) | 0.078 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_conv | conv_physvla | 0.074 | -208 (1) | 0 of 5 (0 to 0) | 0.038 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_conv | conv_physvla_cusum | 0.074 | -208 (1) | 0 of 5 (0 to 0) | 0.038 | none | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_conv | conv_physall | 0.076 | -208 (2) | 0 of 5 (0 to 0) | 0.034 | -40 (1) | 0 of 5 (0 to 0) |
| results/pi05/natural_unseen_conv | conv_physall_cusum | 0.076 | -208 (2) | 0 of 5 (0 to 0) | 0.034 | -40 (1) | 0 of 5 (0 to 0) |

# Timely alarms with bootstrap 95% intervals, threshold fixed 0.025

Timely = alarm at or before t_pnr, of the failures with t_pnr > 0 (interval: bootstrap over these failures, 10000 draws). Window = t_alarm - t_pnr, median over alarmed failures (negative = before t_pnr). vs progress = paired bootstrap interval of the difference in timely counts.

| run | model | timely (95% interval) | late / missed | vs progress | median window (alarmed) | false alarms on successes | unnecessary alarms on recoverable failures | false alarms natural / perturbed successes |
|---|---|---|---|---|---|---|---|---|
| results/pi05/natural_unseen_mlp | progress | 0 of 5 (0 to 0) | 5 / 0 |  | +96 (5) | 10 of 475 (0.021) | 3 of 3 | 0.021 of 475 / none |
| results/pi05/natural_unseen_mlp | mlp | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 22 of 475 (0.046) | 0 of 3 | 0.046 of 475 / none |
| results/pi05/natural_unseen_mlp | combined | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 13 of 475 (0.027) | 0 of 3 | 0.027 of 475 / none |
| results/pi05/natural_unseen_mlp | mlp_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 22 of 475 (0.046) | 0 of 3 | 0.046 of 475 / none |
| results/pi05/natural_unseen_mlp | combined_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 13 of 475 (0.027) | 0 of 3 | 0.027 of 475 / none |
| results/pi05/natural_unseen_mlp | mlp_phys | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 33 of 475 (0.069) | 0 of 3 | 0.069 of 475 / none |
| results/pi05/natural_unseen_mlp | mlp_phys_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 37 of 475 (0.078) | 0 of 3 | 0.078 of 475 / none |
| results/pi05/natural_unseen_mlp | mlp_physvla | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 36 of 475 (0.076) | 0 of 3 | 0.076 of 475 / none |
| results/pi05/natural_unseen_mlp | mlp_physvla_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 36 of 475 (0.076) | 0 of 3 | 0.076 of 475 / none |
| results/pi05/natural_unseen_mlp | mlp_physall | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 11 of 475 (0.023) | 0 of 3 | 0.023 of 475 / none |
| results/pi05/natural_unseen_mlp | mlp_physall_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 11 of 475 (0.023) | 0 of 3 | 0.023 of 475 / none |
| results/pi05/natural_unseen_gru | progress | 0 of 5 (0 to 0) | 5 / 0 |  | +96 (5) | 10 of 475 (0.021) | 3 of 3 | 0.021 of 475 / none |
| results/pi05/natural_unseen_gru | gru | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 8 of 475 (0.017) | 3 of 3 | 0.017 of 475 / none |
| results/pi05/natural_unseen_gru | gru_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 7 of 475 (0.015) | 3 of 3 | 0.015 of 475 / none |
| results/pi05/natural_unseen_gru | gru_phys | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 6 of 475 (0.013) | 0 of 3 | 0.013 of 475 / none |
| results/pi05/natural_unseen_gru | gru_phys_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 38 of 475 (0.080) | 0 of 3 | 0.080 of 475 / none |
| results/pi05/natural_unseen_gru | gru_physvla | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 6 of 475 (0.013) | 0 of 3 | 0.013 of 475 / none |
| results/pi05/natural_unseen_gru | gru_physvla_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 6 of 475 (0.013) | 1 of 3 | 0.013 of 475 / none |
| results/pi05/natural_unseen_gru | gru_physall | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 7 of 475 (0.015) | 3 of 3 | 0.015 of 475 / none |
| results/pi05/natural_unseen_gru | gru_physall_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 7 of 475 (0.015) | 3 of 3 | 0.015 of 475 / none |
| results/pi05/natural_unseen_conv | progress | 0 of 5 (0 to 0) | 5 / 0 |  | +96 (5) | 10 of 475 (0.021) | 3 of 3 | 0.021 of 475 / none |
| results/pi05/natural_unseen_conv | conv | 0 of 5 (0 to 0) | 2 / 3 | +0 (+0 to +0) | +116 (2) | 11 of 475 (0.023) | 3 of 3 | 0.023 of 475 / none |
| results/pi05/natural_unseen_conv | conv_cusum | 0 of 5 (0 to 0) | 2 / 3 | +0 (+0 to +0) | +116 (2) | 10 of 475 (0.021) | 3 of 3 | 0.021 of 475 / none |
| results/pi05/natural_unseen_conv | conv_phys | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 36 of 475 (0.076) | 0 of 3 | 0.076 of 475 / none |
| results/pi05/natural_unseen_conv | conv_phys_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 37 of 475 (0.078) | 0 of 3 | 0.078 of 475 / none |
| results/pi05/natural_unseen_conv | conv_physvla | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 18 of 475 (0.038) | 2 of 3 | 0.038 of 475 / none |
| results/pi05/natural_unseen_conv | conv_physvla_cusum | 0 of 5 (0 to 0) | 0 / 5 | +0 (+0 to +0) | none | 18 of 475 (0.038) | 2 of 3 | 0.038 of 475 / none |
| results/pi05/natural_unseen_conv | conv_physall | 0 of 5 (0 to 0) | 1 / 4 | +0 (+0 to +0) | +40 (1) | 16 of 475 (0.034) | 3 of 3 | 0.034 of 475 / none |
| results/pi05/natural_unseen_conv | conv_physall_cusum | 0 of 5 (0 to 0) | 1 / 4 | +0 (+0 to +0) | +40 (1) | 16 of 475 (0.034) | 3 of 3 | 0.034 of 475 / none |
