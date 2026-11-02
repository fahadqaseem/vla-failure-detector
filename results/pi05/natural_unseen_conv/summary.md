# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 9; doomed from start (t_pnr 0, left out of timing): 1. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 9 labelled failures, 475 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 3 of 3 | 0.046 (of 475) | 0.880 | 0.816 | 5 | 1.00 | 1 | 4 | 0 | -48.0 | 105.6 | 1.75 |
| conv | 3 of 3 | 0.032 (of 475) | 0.673 | 0.548 | 5 | 0.40 | 0 | 2 | 3 | -108.0 | 108.0 | 2.75 |
| conv_cusum | 3 of 3 | 0.032 (of 475) | 0.691 | 0.552 | 5 | 0.40 | 0 | 2 | 3 | -108.0 | 108.0 | 2.75 |
| conv_phys | 0 of 3 | 0.078 (of 475) | 0.376 | 0.378 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| conv_phys_cusum | 0 of 3 | 0.078 (of 475) | 0.494 | 0.444 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| conv_physvla | 2 of 3 | 0.074 (of 475) | 0.591 | 0.435 | 5 | 0.20 | 0 | 1 | 4 | -208.0 | 208.0 | 4.71 |
| conv_physvla_cusum | 2 of 3 | 0.074 (of 475) | 0.631 | 0.456 | 5 | 0.20 | 0 | 1 | 4 | -208.0 | 208.0 | 4.71 |
| conv_physall | 3 of 3 | 0.076 (of 475) | 0.804 | 0.679 | 5 | 0.40 | 0 | 2 | 3 | -208.0 | 208.0 | 2.53 |
| conv_physall_cusum | 3 of 3 | 0.076 (of 475) | 0.831 | 0.717 | 5 | 0.40 | 0 | 2 | 3 | -208.0 | 208.0 | 2.53 |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 20.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 20.0% |
|---|---|---|---|---|---|---|---|---|
| progress | 0 / 5 / 0, FA 0.021 | 1 / 4 / 0, FA 0.046 | 1 / 4 / 0, FA 0.097 | 1 / 4 / 0, FA 0.185 | 0 / 5 / 0, FA 0.019 | 0 / 5 / 0, FA 0.074 | 1 / 4 / 0, FA 0.131 | 1 / 4 / 0, FA 0.139 |
| conv | 0 / 2 / 3, FA 0.023 | 0 / 2 / 3, FA 0.032 | 0 / 2 / 3, FA 0.080 | 0 / 3 / 2, FA 0.177 | 0 / 1 / 4, FA 0.021 | 0 / 2 / 3, FA 0.053 | 0 / 3 / 2, FA 0.086 | 0 / 3 / 2, FA 0.154 |
| conv_cusum | 0 / 2 / 3, FA 0.021 | 0 / 2 / 3, FA 0.032 | 0 / 3 / 2, FA 0.082 | 0 / 3 / 2, FA 0.181 | 0 / 1 / 4, FA 0.021 | 0 / 2 / 3, FA 0.057 | 0 / 3 / 2, FA 0.086 | 0 / 3 / 2, FA 0.149 |
| conv_phys | 0 / 0 / 5, FA 0.076 | 0 / 0 / 5, FA 0.078 | 0 / 0 / 5, FA 0.175 | 0 / 0 / 5, FA 0.261 | 0 / 1 / 4, FA 0.093 | 0 / 1 / 4, FA 0.177 | 0 / 1 / 4, FA 0.185 | 0 / 1 / 4, FA 0.291 |
| conv_phys_cusum | 0 / 0 / 5, FA 0.078 | 0 / 0 / 5, FA 0.078 | 0 / 0 / 5, FA 0.080 | 0 / 0 / 5, FA 0.158 | 0 / 1 / 4, FA 0.080 | 0 / 1 / 4, FA 0.133 | 0 / 1 / 4, FA 0.173 | 0 / 1 / 4, FA 0.185 |
| conv_physvla | 0 / 0 / 5, FA 0.038 | 0 / 1 / 4, FA 0.074 | 0 / 3 / 2, FA 0.103 | 0 / 3 / 2, FA 0.158 | 0 / 0 / 5, FA 0.013 | 0 / 0 / 5, FA 0.053 | 0 / 0 / 5, FA 0.105 | 0 / 1 / 4, FA 0.168 |
| conv_physvla_cusum | 0 / 0 / 5, FA 0.038 | 0 / 1 / 4, FA 0.074 | 0 / 3 / 2, FA 0.103 | 0 / 3 / 2, FA 0.164 | 0 / 0 / 5, FA 0.015 | 0 / 0 / 5, FA 0.057 | 0 / 0 / 5, FA 0.122 | 0 / 1 / 4, FA 0.192 |
| conv_physall | 0 / 1 / 4, FA 0.034 | 0 / 2 / 3, FA 0.076 | 0 / 3 / 2, FA 0.099 | 0 / 4 / 1, FA 0.160 | 0 / 0 / 5, FA 0.011 | 0 / 0 / 5, FA 0.034 | 0 / 0 / 5, FA 0.116 | 0 / 3 / 2, FA 0.196 |
| conv_physall_cusum | 0 / 1 / 4, FA 0.034 | 0 / 2 / 3, FA 0.076 | 0 / 3 / 2, FA 0.103 | 0 / 4 / 1, FA 0.160 | 0 / 0 / 5, FA 0.008 | 0 / 0 / 5, FA 0.040 | 0 / 0 / 5, FA 0.126 | 0 / 4 / 1, FA 0.196 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- progress t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 112 (lead -112, threshold 6.000)
- progress t00_e49_n0: t_pnr 64 -> t_alarm 112 (lead -48, threshold 6.000)
- conv t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.815)
- conv t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.815)
- conv_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.748)
- conv_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.748)
- conv_phys t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.998)
- conv_phys t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.998)
- conv_phys_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.872)
- conv_phys_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.872)
- conv_physvla t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.372)
- conv_physvla t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.372)
- conv_physvla_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.316)
- conv_physvla_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.316)
- conv_physall t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.321)
- conv_physall t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.321)
- conv_physall_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.154)
- conv_physall_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.154)
- progress t06_e21_n0: t_pnr 304 -> t_alarm 192 (lead 112, threshold 6.000)
- progress t06_e32_n0: t_pnr 56 -> t_alarm 168 (lead -112, threshold 6.000)
- progress t06_e39_n0: t_pnr 128 -> t_alarm 160 (lead -32, threshold 6.000)
- progress t06_e46_n0: t_pnr 56 -> t_alarm 280 (lead -224, threshold 6.000)
- conv t06_e21_n0: t_pnr 304 -> t_alarm 328 (lead -24, threshold 0.374)
- conv t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.374)
- conv t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.374)
- conv t06_e46_n0: t_pnr 56 -> t_alarm 248 (lead -192, threshold 0.374)
- conv_cusum t06_e21_n0: t_pnr 304 -> t_alarm 328 (lead -24, threshold 0.332)
- conv_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.332)
- conv_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.332)
- conv_cusum t06_e46_n0: t_pnr 56 -> t_alarm 248 (lead -192, threshold 0.332)
- conv_phys t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.998)
- conv_phys t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.998)
- conv_phys t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.998)
- conv_phys t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.998)
- conv_phys_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.995)
- conv_phys_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.995)
- conv_phys_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.995)
- conv_phys_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.995)
- conv_physvla t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.599)
- conv_physvla t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.599)
- conv_physvla t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.599)
- conv_physvla t06_e46_n0: t_pnr 56 -> t_alarm 264 (lead -208, threshold 0.599)
- conv_physvla_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.593)
- conv_physvla_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.593)
- conv_physvla_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.593)
- conv_physvla_cusum t06_e46_n0: t_pnr 56 -> t_alarm 264 (lead -208, threshold 0.593)
- conv_physall t06_e21_n0: t_pnr 304 -> t_alarm 344 (lead -40, threshold 0.410)
- conv_physall t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.410)
- conv_physall t06_e39_n0: t_pnr 128 -> t_alarm 504 (lead -376, threshold 0.410)
- conv_physall t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.410)
- conv_physall_cusum t06_e21_n0: t_pnr 304 -> t_alarm 344 (lead -40, threshold 0.408)
- conv_physall_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.408)
- conv_physall_cusum t06_e39_n0: t_pnr 128 -> t_alarm 504 (lead -376, threshold 0.408)
- conv_physall_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.408)
- progress t07_e03_n0: t_pnr None -> t_alarm 168 (lead None, threshold 6.000)
- progress t07_e16_n0: t_pnr None -> t_alarm 176 (lead None, threshold 6.000)
- progress t07_e33_n0: t_pnr None -> t_alarm 184 (lead None, threshold 6.000)
- conv t07_e03_n0: t_pnr None -> t_alarm 168 (lead None, threshold 0.499)
- conv t07_e16_n0: t_pnr None -> t_alarm 152 (lead None, threshold 0.499)
- conv t07_e33_n0: t_pnr None -> t_alarm 160 (lead None, threshold 0.499)
- conv_cusum t07_e03_n0: t_pnr None -> t_alarm 168 (lead None, threshold 0.499)
- conv_cusum t07_e16_n0: t_pnr None -> t_alarm 152 (lead None, threshold 0.499)
- conv_cusum t07_e33_n0: t_pnr None -> t_alarm 160 (lead None, threshold 0.499)
- conv_phys t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 1.000)
- conv_phys t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 1.000)
- conv_phys t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 1.000)
- conv_phys_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 1.000)
- conv_phys_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 1.000)
- conv_phys_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 1.000)
- conv_physvla t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.726)
- conv_physvla t07_e16_n0: t_pnr None -> t_alarm 152 (lead None, threshold 0.726)
- conv_physvla t07_e33_n0: t_pnr None -> t_alarm 168 (lead None, threshold 0.726)
- conv_physvla_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.723)
- conv_physvla_cusum t07_e16_n0: t_pnr None -> t_alarm 152 (lead None, threshold 0.723)
- conv_physvla_cusum t07_e33_n0: t_pnr None -> t_alarm 168 (lead None, threshold 0.723)
- conv_physall t07_e03_n0: t_pnr None -> t_alarm 152 (lead None, threshold 0.439)
- conv_physall t07_e16_n0: t_pnr None -> t_alarm 152 (lead None, threshold 0.439)
- conv_physall t07_e33_n0: t_pnr None -> t_alarm 152 (lead None, threshold 0.439)
- conv_physall_cusum t07_e03_n0: t_pnr None -> t_alarm 152 (lead None, threshold 0.438)
- conv_physall_cusum t07_e16_n0: t_pnr None -> t_alarm 152 (lead None, threshold 0.438)
- conv_physall_cusum t07_e33_n0: t_pnr None -> t_alarm 152 (lead None, threshold 0.438)
