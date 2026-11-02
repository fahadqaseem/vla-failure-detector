# Per-step t_pnr predictor, SEEN TASKS: 5 folds by episode_idx % 5 within each task (diagnostic)

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 9; doomed from start (t_pnr 0, left out of timing): 1. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 9 labelled failures, 475 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 3 of 3 | 0.046 (of 475) | 0.880 | 0.816 | 5 | 1.00 | 1 | 4 | 0 | -40.0 | 102.4 | 1.62 |
| gru | 0 of 3 | 0.040 (of 475) | 0.824 | 0.675 | 5 | 0.80 | 0 | 4 | 1 | -144.0 | 146.0 | 3.05 |
| gru_cusum | 1 of 3 | 0.053 (of 475) | 0.863 | 0.727 | 5 | 0.80 | 1 | 3 | 1 | -140.0 | 170.0 | 2.98 |
| gru_phys | 0 of 3 | 0.044 (of 475) | 0.751 | 0.711 | 5 | 0.80 | 2 | 2 | 1 | -16.0 | 130.0 | 1.65 |
| gru_phys_cusum | 0 of 3 | 0.051 (of 475) | 0.670 | 0.539 | 5 | 0.80 | 2 | 2 | 1 | -12.0 | 130.0 | 1.58 |
| gru_physvla | 0 of 3 | 0.048 (of 475) | 0.796 | 0.675 | 5 | 0.80 | 0 | 4 | 1 | -152.0 | 136.0 | 2.99 |
| gru_physvla_cusum | 1 of 3 | 0.046 (of 475) | 0.832 | 0.695 | 5 | 0.80 | 1 | 3 | 1 | -72.0 | 90.0 | 2.17 |
| gru_physall | 1 of 3 | 0.042 (of 475) | 0.885 | 0.780 | 5 | 0.80 | 1 | 3 | 1 | -80.0 | 118.0 | 2.19 |
| gru_physall_cusum | 1 of 3 | 0.040 (of 475) | 0.889 | 0.787 | 5 | 0.80 | 1 | 3 | 1 | -80.0 | 118.0 | 2.19 |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 20.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 20.0% |
|---|---|---|---|---|---|---|---|---|
| progress | 0 / 5 / 0, FA 0.019 | 1 / 4 / 0, FA 0.046 | 1 / 4 / 0, FA 0.076 | 2 / 3 / 0, FA 0.141 | 0 / 3 / 2, FA 0.011 | 0 / 5 / 0, FA 0.038 | 1 / 4 / 0, FA 0.074 | 1 / 4 / 0, FA 0.093 |
| gru | 0 / 4 / 1, FA 0.027 | 0 / 4 / 1, FA 0.040 | 1 / 3 / 1, FA 0.082 | 2 / 2 / 1, FA 0.187 | 0 / 0 / 5, FA 0.021 | 0 / 4 / 1, FA 0.038 | 1 / 3 / 1, FA 0.078 | 1 / 3 / 1, FA 0.171 |
| gru_cusum | 0 / 4 / 1, FA 0.025 | 1 / 3 / 1, FA 0.053 | 1 / 3 / 1, FA 0.091 | 2 / 2 / 1, FA 0.189 | 0 / 2 / 3, FA 0.017 | 0 / 4 / 1, FA 0.042 | 1 / 3 / 1, FA 0.086 | 2 / 2 / 1, FA 0.192 |
| gru_phys | 2 / 2 / 1, FA 0.021 | 2 / 2 / 1, FA 0.044 | 2 / 2 / 1, FA 0.120 | 2 / 2 / 1, FA 0.253 | 2 / 2 / 1, FA 0.021 | 2 / 2 / 1, FA 0.048 | 2 / 2 / 1, FA 0.118 | 2 / 2 / 1, FA 0.238 |
| gru_phys_cusum | 1 / 3 / 1, FA 0.021 | 2 / 2 / 1, FA 0.051 | 2 / 2 / 1, FA 0.103 | 2 / 2 / 1, FA 0.246 | 2 / 1 / 2, FA 0.021 | 2 / 2 / 1, FA 0.059 | 2 / 2 / 1, FA 0.107 | 2 / 2 / 1, FA 0.232 |
| gru_physvla | 0 / 4 / 1, FA 0.021 | 0 / 4 / 1, FA 0.048 | 2 / 2 / 1, FA 0.101 | 2 / 2 / 1, FA 0.202 | 0 / 1 / 4, FA 0.015 | 0 / 3 / 2, FA 0.036 | 1 / 3 / 1, FA 0.082 | 2 / 2 / 1, FA 0.179 |
| gru_physvla_cusum | 0 / 4 / 1, FA 0.025 | 1 / 3 / 1, FA 0.046 | 2 / 2 / 1, FA 0.101 | 2 / 2 / 1, FA 0.202 | 0 / 2 / 3, FA 0.019 | 1 / 3 / 1, FA 0.040 | 1 / 3 / 1, FA 0.097 | 2 / 2 / 1, FA 0.215 |
| gru_physall | 1 / 3 / 1, FA 0.019 | 1 / 3 / 1, FA 0.042 | 2 / 3 / 0, FA 0.082 | 2 / 3 / 0, FA 0.202 | 1 / 0 / 4, FA 0.011 | 1 / 3 / 1, FA 0.036 | 1 / 3 / 1, FA 0.074 | 2 / 2 / 1, FA 0.213 |
| gru_physall_cusum | 1 / 3 / 1, FA 0.019 | 1 / 3 / 1, FA 0.040 | 2 / 3 / 0, FA 0.093 | 2 / 3 / 0, FA 0.196 | 1 / 1 / 3, FA 0.013 | 1 / 3 / 1, FA 0.036 | 1 / 3 / 1, FA 0.076 | 2 / 2 / 1, FA 0.198 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- progress t06_e21_n0: t_pnr 304 -> t_alarm 192 (lead 112, threshold 6.000)
- progress t06_e46_n0: t_pnr 56 -> t_alarm 280 (lead -224, threshold 6.000)
- progress t07_e16_n0: t_pnr None -> t_alarm 176 (lead None, threshold 6.000)
- gru t06_e21_n0: t_pnr 304 -> t_alarm 336 (lead -32, threshold 0.324)
- gru t06_e46_n0: t_pnr 56 -> t_alarm 240 (lead -184, threshold 0.324)
- gru t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.324)
- gru_cusum t06_e21_n0: t_pnr 304 -> t_alarm 88 (lead 216, threshold 0.112)
- gru_cusum t06_e46_n0: t_pnr 56 -> t_alarm 240 (lead -184, threshold 0.112)
- gru_cusum t07_e16_n0: t_pnr None -> t_alarm 360 (lead None, threshold 0.112)
- gru_phys t06_e21_n0: t_pnr 304 -> t_alarm 136 (lead 168, threshold 0.917)
- gru_phys t06_e46_n0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.917)
- gru_phys t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.917)
- gru_phys_cusum t06_e21_n0: t_pnr 304 -> t_alarm 128 (lead 176, threshold 0.796)
- gru_phys_cusum t06_e46_n0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.796)
- gru_phys_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.796)
- gru_physvla t06_e21_n0: t_pnr 304 -> t_alarm 328 (lead -24, threshold 0.187)
- gru_physvla t06_e46_n0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.187)
- gru_physvla t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.187)
- gru_physvla_cusum t06_e21_n0: t_pnr 304 -> t_alarm 320 (lead -16, threshold 0.127)
- gru_physvla_cusum t06_e46_n0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.127)
- gru_physvla_cusum t07_e16_n0: t_pnr None -> t_alarm 360 (lead None, threshold 0.127)
- gru_physall t06_e21_n0: t_pnr 304 -> t_alarm 168 (lead 136, threshold 0.161)
- gru_physall t06_e46_n0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.161)
- gru_physall t07_e16_n0: t_pnr None -> t_alarm 328 (lead None, threshold 0.161)
- gru_physall_cusum t06_e21_n0: t_pnr 304 -> t_alarm 168 (lead 136, threshold 0.160)
- gru_physall_cusum t06_e46_n0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.160)
- gru_physall_cusum t07_e16_n0: t_pnr None -> t_alarm 328 (lead None, threshold 0.160)
- progress t06_e32_n0: t_pnr 56 -> t_alarm 168 (lead -112, threshold 6.000)
- gru t06_e32_n0: t_pnr 56 -> t_alarm 320 (lead -264, threshold 0.394)
- gru_cusum t06_e32_n0: t_pnr 56 -> t_alarm 232 (lead -176, threshold 0.246)
- gru_phys t06_e32_n0: t_pnr 56 -> t_alarm 160 (lead -104, threshold 0.900)
- gru_phys_cusum t06_e32_n0: t_pnr 56 -> t_alarm 152 (lead -96, threshold 0.755)
- gru_physvla t06_e32_n0: t_pnr 56 -> t_alarm 184 (lead -128, threshold 0.241)
- gru_physvla_cusum t06_e32_n0: t_pnr 56 -> t_alarm 184 (lead -128, threshold 0.212)
- gru_physall t06_e32_n0: t_pnr 56 -> t_alarm 168 (lead -112, threshold 0.205)
- gru_physall_cusum t06_e32_n0: t_pnr 56 -> t_alarm 168 (lead -112, threshold 0.163)
- progress t07_e03_n0: t_pnr None -> t_alarm 168 (lead None, threshold 6.000)
- progress t07_e33_n0: t_pnr None -> t_alarm 184 (lead None, threshold 6.000)
- gru t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.437)
- gru t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.437)
- gru_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.379)
- gru_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.379)
- gru_phys t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.868)
- gru_phys t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.868)
- gru_phys_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.822)
- gru_phys_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.822)
- gru_physvla t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.172)
- gru_physvla t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.172)
- gru_physvla_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.166)
- gru_physvla_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.166)
- gru_physall t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.235)
- gru_physall t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.235)
- gru_physall_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.176)
- gru_physall_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.176)
- progress t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 104 (lead -104, threshold 5.000)
- progress t00_e49_n0: t_pnr 64 -> t_alarm 104 (lead -40, threshold 5.000)
- progress t06_e39_n0: t_pnr 128 -> t_alarm 152 (lead -24, threshold 5.000)
- gru t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.242)
- gru t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.242)
- gru t06_e39_n0: t_pnr 128 -> t_alarm 232 (lead -104, threshold 0.242)
- gru_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.144)
- gru_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.144)
- gru_cusum t06_e39_n0: t_pnr 128 -> t_alarm 232 (lead -104, threshold 0.144)
- gru_phys t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.754)
- gru_phys t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.754)
- gru_phys t06_e39_n0: t_pnr 128 -> t_alarm 56 (lead 72, threshold 0.754)
- gru_phys_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.753)
- gru_phys_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.753)
- gru_phys_cusum t06_e39_n0: t_pnr 128 -> t_alarm 56 (lead 72, threshold 0.753)
- gru_physvla t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.116)
- gru_physvla t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.116)
- gru_physvla t06_e39_n0: t_pnr 128 -> t_alarm 344 (lead -216, threshold 0.116)
- gru_physvla_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.074)
- gru_physvla_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.074)
- gru_physvla_cusum t06_e39_n0: t_pnr 128 -> t_alarm 88 (lead 40, threshold 0.074)
- gru_physall t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 256 (lead -256, threshold 0.104)
- gru_physall t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.104)
- gru_physall t06_e39_n0: t_pnr 128 -> t_alarm 176 (lead -48, threshold 0.104)
- gru_physall_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 256 (lead -256, threshold 0.104)
- gru_physall_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.104)
- gru_physall_cusum t06_e39_n0: t_pnr 128 -> t_alarm 176 (lead -48, threshold 0.104)
