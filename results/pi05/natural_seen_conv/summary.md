# Per-step t_pnr predictor, SEEN TASKS: 5 folds by episode_idx % 5 within each task (diagnostic)

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 9; doomed from start (t_pnr 0, left out of timing): 1. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 9 labelled failures, 475 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 3 of 3 | 0.046 (of 475) | 0.880 | 0.816 | 5 | 1.00 | 1 | 4 | 0 | -40.0 | 102.4 | 1.62 |
| conv | 1 of 3 | 0.055 (of 475) | 0.881 | 0.793 | 5 | 0.80 | 1 | 3 | 1 | -108.0 | 152.0 | 2.61 |
| conv_cusum | 1 of 3 | 0.055 (of 475) | 0.879 | 0.772 | 5 | 0.80 | 1 | 3 | 1 | -104.0 | 150.0 | 2.54 |
| conv_phys | 0 of 3 | 0.061 (of 475) | 0.743 | 0.742 | 5 | 0.80 | 2 | 2 | 1 | -60.0 | 182.0 | 2.44 |
| conv_phys_cusum | 0 of 3 | 0.053 (of 475) | 0.770 | 0.737 | 5 | 0.80 | 2 | 2 | 1 | -52.0 | 180.0 | 2.29 |
| conv_physvla | 1 of 3 | 0.053 (of 475) | 0.865 | 0.762 | 5 | 0.80 | 1 | 3 | 1 | -144.0 | 178.0 | 2.82 |
| conv_physvla_cusum | 1 of 3 | 0.051 (of 475) | 0.877 | 0.766 | 5 | 0.80 | 1 | 3 | 1 | -144.0 | 178.0 | 2.82 |
| conv_physall | 1 of 3 | 0.053 (of 475) | 0.934 | 0.857 | 5 | 1.00 | 1 | 4 | 0 | -112.0 | 137.6 | 3.00 |
| conv_physall_cusum | 1 of 3 | 0.059 (of 475) | 0.938 | 0.870 | 5 | 1.00 | 1 | 4 | 0 | -112.0 | 137.6 | 3.00 |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 20.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 20.0% |
|---|---|---|---|---|---|---|---|---|
| progress | 0 / 5 / 0, FA 0.019 | 1 / 4 / 0, FA 0.046 | 1 / 4 / 0, FA 0.076 | 2 / 3 / 0, FA 0.141 | 0 / 3 / 2, FA 0.011 | 0 / 5 / 0, FA 0.038 | 1 / 4 / 0, FA 0.074 | 1 / 4 / 0, FA 0.093 |
| conv | 0 / 4 / 1, FA 0.021 | 1 / 3 / 1, FA 0.055 | 2 / 2 / 1, FA 0.118 | 3 / 1 / 1, FA 0.211 | 0 / 1 / 4, FA 0.015 | 1 / 3 / 1, FA 0.053 | 1 / 3 / 1, FA 0.099 | 3 / 1 / 1, FA 0.202 |
| conv_cusum | 0 / 4 / 1, FA 0.025 | 1 / 3 / 1, FA 0.055 | 2 / 2 / 1, FA 0.122 | 3 / 1 / 1, FA 0.208 | 0 / 0 / 5, FA 0.015 | 1 / 3 / 1, FA 0.044 | 3 / 1 / 1, FA 0.107 | 3 / 1 / 1, FA 0.211 |
| conv_phys | 2 / 2 / 1, FA 0.021 | 2 / 2 / 1, FA 0.061 | 2 / 2 / 1, FA 0.122 | 2 / 2 / 1, FA 0.234 | 2 / 2 / 1, FA 0.023 | 2 / 2 / 1, FA 0.044 | 2 / 2 / 1, FA 0.128 | 2 / 3 / 0, FA 0.240 |
| conv_phys_cusum | 2 / 2 / 1, FA 0.019 | 2 / 2 / 1, FA 0.053 | 2 / 2 / 1, FA 0.124 | 2 / 3 / 0, FA 0.225 | 2 / 2 / 1, FA 0.023 | 2 / 2 / 1, FA 0.059 | 2 / 2 / 1, FA 0.135 | 2 / 3 / 0, FA 0.244 |
| conv_physvla | 0 / 4 / 1, FA 0.021 | 1 / 3 / 1, FA 0.053 | 2 / 2 / 1, FA 0.105 | 3 / 1 / 1, FA 0.189 | 0 / 2 / 3, FA 0.021 | 1 / 3 / 1, FA 0.055 | 2 / 2 / 1, FA 0.093 | 3 / 1 / 1, FA 0.192 |
| conv_physvla_cusum | 0 / 4 / 1, FA 0.023 | 1 / 3 / 1, FA 0.051 | 2 / 2 / 1, FA 0.107 | 3 / 1 / 1, FA 0.183 | 0 / 2 / 3, FA 0.023 | 1 / 3 / 1, FA 0.046 | 3 / 1 / 1, FA 0.103 | 3 / 1 / 1, FA 0.185 |
| conv_physall | 1 / 3 / 1, FA 0.023 | 1 / 4 / 0, FA 0.053 | 1 / 4 / 0, FA 0.101 | 3 / 2 / 0, FA 0.187 | 1 / 2 / 2, FA 0.029 | 1 / 3 / 1, FA 0.044 | 1 / 3 / 1, FA 0.095 | 3 / 2 / 0, FA 0.221 |
| conv_physall_cusum | 1 / 3 / 1, FA 0.023 | 1 / 4 / 0, FA 0.059 | 1 / 4 / 0, FA 0.103 | 3 / 2 / 0, FA 0.192 | 1 / 1 / 3, FA 0.023 | 1 / 3 / 1, FA 0.048 | 2 / 2 / 1, FA 0.101 | 3 / 2 / 0, FA 0.196 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- progress t06_e21_n0: t_pnr 304 -> t_alarm 192 (lead 112, threshold 6.000)
- progress t06_e46_n0: t_pnr 56 -> t_alarm 280 (lead -224, threshold 6.000)
- progress t07_e16_n0: t_pnr None -> t_alarm 176 (lead None, threshold 6.000)
- conv t06_e21_n0: t_pnr 304 -> t_alarm 80 (lead 224, threshold 0.097)
- conv t06_e46_n0: t_pnr 56 -> t_alarm 224 (lead -168, threshold 0.097)
- conv t07_e16_n0: t_pnr None -> t_alarm 160 (lead None, threshold 0.097)
- conv_cusum t06_e21_n0: t_pnr 304 -> t_alarm 80 (lead 224, threshold 0.085)
- conv_cusum t06_e46_n0: t_pnr 56 -> t_alarm 224 (lead -168, threshold 0.085)
- conv_cusum t07_e16_n0: t_pnr None -> t_alarm 160 (lead None, threshold 0.085)
- conv_phys t06_e21_n0: t_pnr 304 -> t_alarm 136 (lead 168, threshold 0.701)
- conv_phys t06_e46_n0: t_pnr 56 -> t_alarm 248 (lead -192, threshold 0.701)
- conv_phys t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.701)
- conv_phys_cusum t06_e21_n0: t_pnr 304 -> t_alarm 128 (lead 176, threshold 0.487)
- conv_phys_cusum t06_e46_n0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.487)
- conv_phys_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.487)
- conv_physvla t06_e21_n0: t_pnr 304 -> t_alarm 72 (lead 232, threshold 0.066)
- conv_physvla t06_e46_n0: t_pnr 56 -> t_alarm 224 (lead -168, threshold 0.066)
- conv_physvla t07_e16_n0: t_pnr None -> t_alarm 208 (lead None, threshold 0.066)
- conv_physvla_cusum t06_e21_n0: t_pnr 304 -> t_alarm 72 (lead 232, threshold 0.065)
- conv_physvla_cusum t06_e46_n0: t_pnr 56 -> t_alarm 224 (lead -168, threshold 0.065)
- conv_physvla_cusum t07_e16_n0: t_pnr None -> t_alarm 208 (lead None, threshold 0.065)
- conv_physall t06_e21_n0: t_pnr 304 -> t_alarm 152 (lead 152, threshold 0.064)
- conv_physall t06_e46_n0: t_pnr 56 -> t_alarm 216 (lead -160, threshold 0.064)
- conv_physall t07_e16_n0: t_pnr None -> t_alarm 192 (lead None, threshold 0.064)
- conv_physall_cusum t06_e21_n0: t_pnr 304 -> t_alarm 152 (lead 152, threshold 0.062)
- conv_physall_cusum t06_e46_n0: t_pnr 56 -> t_alarm 216 (lead -160, threshold 0.062)
- conv_physall_cusum t07_e16_n0: t_pnr None -> t_alarm 192 (lead None, threshold 0.062)
- progress t06_e32_n0: t_pnr 56 -> t_alarm 168 (lead -112, threshold 6.000)
- conv t06_e32_n0: t_pnr 56 -> t_alarm 208 (lead -152, threshold 0.128)
- conv_cusum t06_e32_n0: t_pnr 56 -> t_alarm 200 (lead -144, threshold 0.102)
- conv_phys t06_e32_n0: t_pnr 56 -> t_alarm 352 (lead -296, threshold 0.699)
- conv_phys_cusum t06_e32_n0: t_pnr 56 -> t_alarm 352 (lead -296, threshold 0.458)
- conv_physvla t06_e32_n0: t_pnr 56 -> t_alarm 176 (lead -120, threshold 0.087)
- conv_physvla_cusum t06_e32_n0: t_pnr 56 -> t_alarm 176 (lead -120, threshold 0.064)
- conv_physall t06_e32_n0: t_pnr 56 -> t_alarm 168 (lead -112, threshold 0.084)
- conv_physall_cusum t06_e32_n0: t_pnr 56 -> t_alarm 168 (lead -112, threshold 0.073)
- progress t07_e03_n0: t_pnr None -> t_alarm 168 (lead None, threshold 6.000)
- progress t07_e33_n0: t_pnr None -> t_alarm 184 (lead None, threshold 6.000)
- conv t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.227)
- conv t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.227)
- conv_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.142)
- conv_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.142)
- conv_phys t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.802)
- conv_phys t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.802)
- conv_phys_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.670)
- conv_phys_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.670)
- conv_physvla t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.124)
- conv_physvla t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.124)
- conv_physvla_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.097)
- conv_physvla_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.097)
- conv_physall t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.108)
- conv_physall t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.108)
- conv_physall_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.102)
- conv_physall_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.102)
- progress t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 104 (lead -104, threshold 5.000)
- progress t00_e49_n0: t_pnr 64 -> t_alarm 104 (lead -40, threshold 5.000)
- progress t06_e39_n0: t_pnr 128 -> t_alarm 152 (lead -24, threshold 5.000)
- conv t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.149)
- conv t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.149)
- conv t06_e39_n0: t_pnr 128 -> t_alarm 192 (lead -64, threshold 0.149)
- conv_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.148)
- conv_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.148)
- conv_cusum t06_e39_n0: t_pnr 128 -> t_alarm 192 (lead -64, threshold 0.148)
- conv_phys t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.670)
- conv_phys t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.670)
- conv_phys t06_e39_n0: t_pnr 128 -> t_alarm 56 (lead 72, threshold 0.670)
- conv_phys_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.669)
- conv_phys_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.669)
- conv_phys_cusum t06_e39_n0: t_pnr 128 -> t_alarm 56 (lead 72, threshold 0.669)
- conv_physvla t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.057)
- conv_physvla t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.057)
- conv_physvla t06_e39_n0: t_pnr 128 -> t_alarm 320 (lead -192, threshold 0.057)
- conv_physvla_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.057)
- conv_physvla_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.057)
- conv_physvla_cusum t06_e39_n0: t_pnr 128 -> t_alarm 320 (lead -192, threshold 0.057)
- conv_physall t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 232 (lead -232, threshold 0.062)
- conv_physall t00_e49_n0: t_pnr 64 -> t_alarm 296 (lead -232, threshold 0.062)
- conv_physall t06_e39_n0: t_pnr 128 -> t_alarm 160 (lead -32, threshold 0.062)
- conv_physall_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 232 (lead -232, threshold 0.062)
- conv_physall_cusum t00_e49_n0: t_pnr 64 -> t_alarm 296 (lead -232, threshold 0.062)
- conv_physall_cusum t06_e39_n0: t_pnr 128 -> t_alarm 160 (lead -32, threshold 0.062)
