# Per-step t_pnr predictor, SEEN TASKS: 5 folds by episode_idx % 5 within each task (diagnostic)

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 9; doomed from start (t_pnr 0, left out of timing): 1. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 9 labelled failures, 475 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 3 of 3 | 0.046 (of 475) | 0.880 | 0.816 | 5 | 1.00 | 1 | 4 | 0 | -40.0 | 102.4 | 1.62 |
| mlp | 0 of 3 | 0.051 (of 475) | 0.866 | 0.800 | 5 | 0.80 | 1 | 3 | 1 | -72.0 | 108.0 | 2.17 |
| combined | 0 of 3 | 0.051 (of 475) | 0.918 | 0.835 | 5 | 0.80 | 1 | 3 | 1 | -56.0 | 102.0 | 1.96 |
| mlp_cusum | 0 of 3 | 0.046 (of 475) | 0.870 | 0.795 | 5 | 0.80 | 1 | 3 | 1 | -72.0 | 108.0 | 2.17 |
| combined_cusum | 0 of 3 | 0.053 (of 475) | 0.921 | 0.841 | 5 | 0.80 | 1 | 3 | 1 | -56.0 | 102.0 | 1.96 |
| mlp_phys | 0 of 3 | 0.059 (of 475) | 0.841 | 0.794 | 5 | 0.80 | 1 | 3 | 1 | -64.0 | 124.0 | 2.14 |
| mlp_phys_cusum | 0 of 3 | 0.044 (of 475) | 0.877 | 0.828 | 5 | 0.80 | 1 | 3 | 1 | -64.0 | 124.0 | 2.14 |
| mlp_physvla | 0 of 3 | 0.053 (of 475) | 0.885 | 0.822 | 5 | 0.80 | 1 | 3 | 1 | -84.0 | 130.0 | 2.18 |
| mlp_physvla_cusum | 0 of 3 | 0.051 (of 475) | 0.889 | 0.820 | 5 | 0.80 | 1 | 3 | 1 | -80.0 | 128.0 | 2.11 |
| mlp_physall | 0 of 3 | 0.053 (of 475) | 0.925 | 0.846 | 5 | 0.80 | 1 | 3 | 1 | -56.0 | 104.0 | 1.96 |
| mlp_physall_cusum | 0 of 3 | 0.059 (of 475) | 0.926 | 0.847 | 5 | 0.80 | 1 | 3 | 1 | -56.0 | 104.0 | 1.96 |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 20.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 20.0% |
|---|---|---|---|---|---|---|---|---|
| progress | 0 / 5 / 0, FA 0.019 | 1 / 4 / 0, FA 0.046 | 1 / 4 / 0, FA 0.076 | 2 / 3 / 0, FA 0.141 | 0 / 3 / 2, FA 0.011 | 0 / 5 / 0, FA 0.038 | 1 / 4 / 0, FA 0.074 | 1 / 4 / 0, FA 0.093 |
| mlp | 0 / 3 / 2, FA 0.025 | 1 / 3 / 1, FA 0.051 | 2 / 2 / 1, FA 0.124 | 2 / 2 / 1, FA 0.215 | 0 / 1 / 4, FA 0.019 | 0 / 3 / 2, FA 0.057 | 2 / 2 / 1, FA 0.122 | 2 / 2 / 1, FA 0.217 |
| combined | 1 / 3 / 1, FA 0.025 | 1 / 3 / 1, FA 0.051 | 2 / 3 / 0, FA 0.112 | 2 / 3 / 0, FA 0.211 | 0 / 3 / 2, FA 0.019 | 1 / 3 / 1, FA 0.044 | 2 / 2 / 1, FA 0.101 | 2 / 3 / 0, FA 0.204 |
| mlp_cusum | 0 / 3 / 2, FA 0.025 | 1 / 3 / 1, FA 0.046 | 2 / 2 / 1, FA 0.120 | 2 / 2 / 1, FA 0.208 | 0 / 1 / 4, FA 0.017 | 0 / 3 / 2, FA 0.053 | 2 / 2 / 1, FA 0.124 | 2 / 2 / 1, FA 0.217 |
| combined_cusum | 1 / 3 / 1, FA 0.029 | 1 / 3 / 1, FA 0.053 | 2 / 3 / 0, FA 0.109 | 2 / 3 / 0, FA 0.206 | 0 / 3 / 2, FA 0.019 | 1 / 3 / 1, FA 0.044 | 2 / 2 / 1, FA 0.097 | 3 / 2 / 0, FA 0.206 |
| mlp_phys | 1 / 3 / 1, FA 0.023 | 1 / 3 / 1, FA 0.059 | 2 / 2 / 1, FA 0.116 | 2 / 2 / 1, FA 0.229 | 1 / 2 / 2, FA 0.021 | 2 / 2 / 1, FA 0.055 | 2 / 2 / 1, FA 0.088 | 2 / 3 / 0, FA 0.221 |
| mlp_phys_cusum | 1 / 3 / 1, FA 0.027 | 1 / 3 / 1, FA 0.044 | 2 / 2 / 1, FA 0.097 | 2 / 2 / 1, FA 0.232 | 1 / 2 / 2, FA 0.021 | 2 / 2 / 1, FA 0.055 | 2 / 2 / 1, FA 0.103 | 3 / 2 / 0, FA 0.225 |
| mlp_physvla | 0 / 3 / 2, FA 0.019 | 1 / 3 / 1, FA 0.053 | 2 / 2 / 1, FA 0.118 | 2 / 2 / 1, FA 0.215 | 0 / 1 / 4, FA 0.019 | 1 / 2 / 2, FA 0.057 | 2 / 2 / 1, FA 0.128 | 2 / 2 / 1, FA 0.211 |
| mlp_physvla_cusum | 0 / 3 / 2, FA 0.019 | 1 / 3 / 1, FA 0.051 | 2 / 2 / 1, FA 0.118 | 2 / 2 / 1, FA 0.204 | 0 / 1 / 4, FA 0.017 | 0 / 2 / 3, FA 0.051 | 2 / 2 / 1, FA 0.128 | 2 / 2 / 1, FA 0.206 |
| mlp_physall | 1 / 3 / 1, FA 0.029 | 1 / 3 / 1, FA 0.053 | 2 / 3 / 0, FA 0.107 | 2 / 3 / 0, FA 0.202 | 1 / 3 / 1, FA 0.019 | 1 / 3 / 1, FA 0.034 | 2 / 2 / 1, FA 0.095 | 2 / 3 / 0, FA 0.187 |
| mlp_physall_cusum | 1 / 3 / 1, FA 0.029 | 1 / 3 / 1, FA 0.059 | 2 / 3 / 0, FA 0.114 | 2 / 3 / 0, FA 0.189 | 1 / 3 / 1, FA 0.015 | 1 / 3 / 1, FA 0.036 | 2 / 2 / 1, FA 0.099 | 2 / 3 / 0, FA 0.208 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- progress t06_e21_n0: t_pnr 304 -> t_alarm 192 (lead 112, threshold 6.000)
- progress t06_e46_n0: t_pnr 56 -> t_alarm 280 (lead -224, threshold 6.000)
- progress t07_e16_n0: t_pnr None -> t_alarm 176 (lead None, threshold 6.000)
- mlp t06_e21_n0: t_pnr 304 -> t_alarm 192 (lead 112, threshold 0.418)
- mlp t06_e46_n0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.418)
- mlp t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.418)
- combined t06_e21_n0: t_pnr 304 -> t_alarm 168 (lead 136, threshold 0.349)
- combined t06_e46_n0: t_pnr 56 -> t_alarm 216 (lead -160, threshold 0.349)
- combined t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.349)
- mlp_cusum t06_e21_n0: t_pnr 304 -> t_alarm 192 (lead 112, threshold 0.398)
- mlp_cusum t06_e46_n0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.398)
- mlp_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.398)
- combined_cusum t06_e21_n0: t_pnr 304 -> t_alarm 168 (lead 136, threshold 0.322)
- combined_cusum t06_e46_n0: t_pnr 56 -> t_alarm 216 (lead -160, threshold 0.322)
- combined_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.322)
- mlp_phys t06_e21_n0: t_pnr 304 -> t_alarm 104 (lead 200, threshold 0.950)
- mlp_phys t06_e46_n0: t_pnr 56 -> t_alarm 112 (lead -56, threshold 0.950)
- mlp_phys t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.950)
- mlp_phys_cusum t06_e21_n0: t_pnr 304 -> t_alarm 104 (lead 200, threshold 0.886)
- mlp_phys_cusum t06_e46_n0: t_pnr 56 -> t_alarm 112 (lead -56, threshold 0.886)
- mlp_phys_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.886)
- mlp_physvla t06_e21_n0: t_pnr 304 -> t_alarm 120 (lead 184, threshold 0.351)
- mlp_physvla t06_e46_n0: t_pnr 56 -> t_alarm 224 (lead -168, threshold 0.351)
- mlp_physvla t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.351)
- mlp_physvla_cusum t06_e21_n0: t_pnr 304 -> t_alarm 120 (lead 184, threshold 0.350)
- mlp_physvla_cusum t06_e46_n0: t_pnr 56 -> t_alarm 224 (lead -168, threshold 0.350)
- mlp_physvla_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.350)
- mlp_physall t06_e21_n0: t_pnr 304 -> t_alarm 160 (lead 144, threshold 0.377)
- mlp_physall t06_e46_n0: t_pnr 56 -> t_alarm 216 (lead -160, threshold 0.377)
- mlp_physall t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.377)
- mlp_physall_cusum t06_e21_n0: t_pnr 304 -> t_alarm 160 (lead 144, threshold 0.292)
- mlp_physall_cusum t06_e46_n0: t_pnr 56 -> t_alarm 216 (lead -160, threshold 0.292)
- mlp_physall_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.292)
- progress t06_e32_n0: t_pnr 56 -> t_alarm 168 (lead -112, threshold 6.000)
- mlp t06_e32_n0: t_pnr 56 -> t_alarm 176 (lead -120, threshold 0.500)
- combined t06_e32_n0: t_pnr 56 -> t_alarm 160 (lead -104, threshold 0.293)
- mlp_cusum t06_e32_n0: t_pnr 56 -> t_alarm 176 (lead -120, threshold 0.419)
- combined_cusum t06_e32_n0: t_pnr 56 -> t_alarm 160 (lead -104, threshold 0.260)
- mlp_phys t06_e32_n0: t_pnr 56 -> t_alarm 128 (lead -72, threshold 0.949)
- mlp_phys_cusum t06_e32_n0: t_pnr 56 -> t_alarm 128 (lead -72, threshold 0.854)
- mlp_physvla t06_e32_n0: t_pnr 56 -> t_alarm 160 (lead -104, threshold 0.414)
- mlp_physvla_cusum t06_e32_n0: t_pnr 56 -> t_alarm 152 (lead -96, threshold 0.361)
- mlp_physall t06_e32_n0: t_pnr 56 -> t_alarm 160 (lead -104, threshold 0.315)
- mlp_physall_cusum t06_e32_n0: t_pnr 56 -> t_alarm 160 (lead -104, threshold 0.298)
- progress t07_e03_n0: t_pnr None -> t_alarm 168 (lead None, threshold 6.000)
- progress t07_e33_n0: t_pnr None -> t_alarm 184 (lead None, threshold 6.000)
- mlp t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.482)
- mlp t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.482)
- combined t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.384)
- combined t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.384)
- mlp_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.391)
- mlp_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.391)
- combined_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.384)
- combined_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.384)
- mlp_phys t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.947)
- mlp_phys t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.947)
- mlp_phys_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.868)
- mlp_phys_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.868)
- mlp_physvla t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.485)
- mlp_physvla t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.485)
- mlp_physvla_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.390)
- mlp_physvla_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.390)
- mlp_physall t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.423)
- mlp_physall t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.423)
- mlp_physall_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.422)
- mlp_physall_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.422)
- progress t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 104 (lead -104, threshold 5.000)
- progress t00_e49_n0: t_pnr 64 -> t_alarm 104 (lead -40, threshold 5.000)
- progress t06_e39_n0: t_pnr 128 -> t_alarm 152 (lead -24, threshold 5.000)
- mlp t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.425)
- mlp t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.425)
- mlp t06_e39_n0: t_pnr 128 -> t_alarm 152 (lead -24, threshold 0.425)
- combined t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.342)
- combined t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.342)
- combined t06_e39_n0: t_pnr 128 -> t_alarm 136 (lead -8, threshold 0.342)
- mlp_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.422)
- mlp_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.422)
- mlp_cusum t06_e39_n0: t_pnr 128 -> t_alarm 152 (lead -24, threshold 0.422)
- combined_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.342)
- combined_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.342)
- combined_cusum t06_e39_n0: t_pnr 128 -> t_alarm 136 (lead -8, threshold 0.342)
- mlp_phys t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.893)
- mlp_phys t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.893)
- mlp_phys t06_e39_n0: t_pnr 128 -> t_alarm 296 (lead -168, threshold 0.893)
- mlp_phys_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.886)
- mlp_phys_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.886)
- mlp_phys_cusum t06_e39_n0: t_pnr 128 -> t_alarm 296 (lead -168, threshold 0.886)
- mlp_physvla t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.356)
- mlp_physvla t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.356)
- mlp_physvla t06_e39_n0: t_pnr 128 -> t_alarm 192 (lead -64, threshold 0.356)
- mlp_physvla_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.356)
- mlp_physvla_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.356)
- mlp_physvla_cusum t06_e39_n0: t_pnr 128 -> t_alarm 192 (lead -64, threshold 0.356)
- mlp_physall t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.310)
- mlp_physall t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.310)
- mlp_physall t06_e39_n0: t_pnr 128 -> t_alarm 136 (lead -8, threshold 0.310)
- mlp_physall_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.309)
- mlp_physall_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.309)
- mlp_physall_cusum t06_e39_n0: t_pnr 128 -> t_alarm 136 (lead -8, threshold 0.309)
