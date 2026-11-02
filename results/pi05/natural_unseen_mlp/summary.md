# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 9; doomed from start (t_pnr 0, left out of timing): 1. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 9 labelled failures, 475 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 3 of 3 | 0.046 (of 475) | 0.880 | 0.816 | 5 | 1.00 | 1 | 4 | 0 | -48.0 | 105.6 | 1.75 |
| mlp | 0 of 3 | 0.088 (of 475) | 0.562 | 0.555 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| combined | 0 of 3 | 0.065 (of 475) | 0.644 | 0.674 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| mlp_cusum | 0 of 3 | 0.088 (of 475) | 0.588 | 0.532 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| combined_cusum | 0 of 3 | 0.063 (of 475) | 0.690 | 0.689 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| mlp_phys | 0 of 3 | 0.120 (of 475) | 0.234 | 0.237 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| mlp_phys_cusum | 0 of 3 | 0.078 (of 475) | 0.415 | 0.356 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| mlp_physvla | 0 of 3 | 0.091 (of 475) | 0.525 | 0.534 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| mlp_physvla_cusum | 0 of 3 | 0.091 (of 475) | 0.562 | 0.520 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| mlp_physall | 0 of 3 | 0.063 (of 475) | 0.646 | 0.678 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| mlp_physall_cusum | 0 of 3 | 0.063 (of 475) | 0.694 | 0.695 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 20.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 20.0% |
|---|---|---|---|---|---|---|---|---|
| progress | 0 / 5 / 0, FA 0.021 | 1 / 4 / 0, FA 0.046 | 1 / 4 / 0, FA 0.097 | 1 / 4 / 0, FA 0.185 | 0 / 5 / 0, FA 0.019 | 0 / 5 / 0, FA 0.074 | 1 / 4 / 0, FA 0.131 | 1 / 4 / 0, FA 0.139 |
| mlp | 0 / 0 / 5, FA 0.046 | 0 / 0 / 5, FA 0.088 | 0 / 0 / 5, FA 0.137 | 0 / 1 / 4, FA 0.194 | 0 / 1 / 4, FA 0.137 | 0 / 2 / 3, FA 0.160 | 0 / 3 / 2, FA 0.204 | 0 / 3 / 2, FA 0.242 |
| combined | 0 / 0 / 5, FA 0.027 | 0 / 0 / 5, FA 0.065 | 0 / 0 / 5, FA 0.122 | 0 / 0 / 5, FA 0.223 | 0 / 1 / 4, FA 0.101 | 0 / 1 / 4, FA 0.147 | 0 / 2 / 3, FA 0.192 | 0 / 2 / 3, FA 0.221 |
| mlp_cusum | 0 / 0 / 5, FA 0.046 | 0 / 0 / 5, FA 0.088 | 0 / 0 / 5, FA 0.137 | 0 / 1 / 4, FA 0.192 | 0 / 1 / 4, FA 0.135 | 0 / 1 / 4, FA 0.154 | 0 / 3 / 2, FA 0.206 | 0 / 3 / 2, FA 0.248 |
| combined_cusum | 0 / 0 / 5, FA 0.027 | 0 / 0 / 5, FA 0.063 | 0 / 0 / 5, FA 0.122 | 0 / 0 / 5, FA 0.223 | 0 / 1 / 4, FA 0.074 | 0 / 1 / 4, FA 0.141 | 0 / 2 / 3, FA 0.183 | 0 / 2 / 3, FA 0.229 |
| mlp_phys | 0 / 0 / 5, FA 0.069 | 0 / 0 / 5, FA 0.120 | 0 / 0 / 5, FA 0.171 | 0 / 0 / 5, FA 0.280 | 0 / 0 / 5, FA 0.082 | 0 / 0 / 5, FA 0.082 | 0 / 0 / 5, FA 0.179 | 0 / 0 / 5, FA 0.246 |
| mlp_phys_cusum | 0 / 0 / 5, FA 0.078 | 0 / 0 / 5, FA 0.078 | 0 / 0 / 5, FA 0.171 | 0 / 0 / 5, FA 0.183 | 0 / 0 / 5, FA 0.179 | 0 / 0 / 5, FA 0.183 | 0 / 0 / 5, FA 0.196 | 0 / 0 / 5, FA 0.234 |
| mlp_physvla | 0 / 0 / 5, FA 0.076 | 0 / 0 / 5, FA 0.091 | 0 / 0 / 5, FA 0.122 | 0 / 0 / 5, FA 0.200 | 0 / 1 / 4, FA 0.137 | 0 / 1 / 4, FA 0.168 | 0 / 1 / 4, FA 0.215 | 0 / 1 / 4, FA 0.255 |
| mlp_physvla_cusum | 0 / 0 / 5, FA 0.076 | 0 / 0 / 5, FA 0.091 | 0 / 0 / 5, FA 0.122 | 0 / 0 / 5, FA 0.202 | 0 / 1 / 4, FA 0.128 | 0 / 1 / 4, FA 0.175 | 0 / 1 / 4, FA 0.215 | 0 / 1 / 4, FA 0.267 |
| mlp_physall | 0 / 0 / 5, FA 0.023 | 0 / 0 / 5, FA 0.063 | 0 / 0 / 5, FA 0.124 | 0 / 0 / 5, FA 0.198 | 0 / 0 / 5, FA 0.084 | 0 / 0 / 5, FA 0.109 | 0 / 1 / 4, FA 0.181 | 0 / 1 / 4, FA 0.215 |
| mlp_physall_cusum | 0 / 0 / 5, FA 0.023 | 0 / 0 / 5, FA 0.063 | 0 / 0 / 5, FA 0.124 | 0 / 0 / 5, FA 0.194 | 0 / 0 / 5, FA 0.078 | 0 / 0 / 5, FA 0.099 | 0 / 1 / 4, FA 0.177 | 0 / 1 / 4, FA 0.213 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- progress t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 112 (lead -112, threshold 6.000)
- progress t00_e49_n0: t_pnr 64 -> t_alarm 112 (lead -48, threshold 6.000)
- mlp t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.975)
- mlp t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.975)
- combined t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.895)
- combined t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.895)
- mlp_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.975)
- mlp_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.975)
- combined_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.895)
- combined_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.895)
- mlp_phys t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.887)
- mlp_phys t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.887)
- mlp_phys_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.872)
- mlp_phys_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.872)
- mlp_physvla t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.925)
- mlp_physvla t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.925)
- mlp_physvla_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.925)
- mlp_physvla_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.925)
- mlp_physall t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.868)
- mlp_physall t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.868)
- mlp_physall_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.867)
- mlp_physall_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.867)
- progress t06_e21_n0: t_pnr 304 -> t_alarm 192 (lead 112, threshold 6.000)
- progress t06_e32_n0: t_pnr 56 -> t_alarm 168 (lead -112, threshold 6.000)
- progress t06_e39_n0: t_pnr 128 -> t_alarm 160 (lead -32, threshold 6.000)
- progress t06_e46_n0: t_pnr 56 -> t_alarm 280 (lead -224, threshold 6.000)
- mlp t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.926)
- mlp t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.926)
- mlp t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.926)
- mlp t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.926)
- combined t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.873)
- combined t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.873)
- combined t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.873)
- combined t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.873)
- mlp_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.926)
- mlp_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.926)
- mlp_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.926)
- mlp_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.926)
- combined_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.873)
- combined_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.873)
- combined_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.873)
- combined_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.873)
- mlp_phys t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.997)
- mlp_phys t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.997)
- mlp_phys t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.997)
- mlp_phys t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.997)
- mlp_phys_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.905)
- mlp_phys_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.905)
- mlp_phys_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.905)
- mlp_phys_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.905)
- mlp_physvla t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.823)
- mlp_physvla t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.823)
- mlp_physvla t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.823)
- mlp_physvla t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.823)
- mlp_physvla_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.823)
- mlp_physvla_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.823)
- mlp_physvla_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.823)
- mlp_physvla_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.823)
- mlp_physall t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.849)
- mlp_physall t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.849)
- mlp_physall t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.849)
- mlp_physall t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.849)
- mlp_physall_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.849)
- mlp_physall_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.849)
- mlp_physall_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.849)
- mlp_physall_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.849)
- progress t07_e03_n0: t_pnr None -> t_alarm 168 (lead None, threshold 6.000)
- progress t07_e16_n0: t_pnr None -> t_alarm 176 (lead None, threshold 6.000)
- progress t07_e33_n0: t_pnr None -> t_alarm 184 (lead None, threshold 6.000)
- mlp t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.997)
- mlp t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.997)
- mlp t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.997)
- combined t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.987)
- combined t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.987)
- combined t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.987)
- mlp_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.997)
- mlp_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.997)
- mlp_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.997)
- combined_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.987)
- combined_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.987)
- combined_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.987)
- mlp_phys t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.998)
- mlp_phys t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.998)
- mlp_phys t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.998)
- mlp_phys_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.967)
- mlp_phys_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.967)
- mlp_phys_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.967)
- mlp_physvla t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.984)
- mlp_physvla t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.984)
- mlp_physvla t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.984)
- mlp_physvla_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.984)
- mlp_physvla_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.984)
- mlp_physvla_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.984)
- mlp_physall t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.960)
- mlp_physall t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.960)
- mlp_physall t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.960)
- mlp_physall_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.960)
- mlp_physall_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.960)
- mlp_physall_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.960)
