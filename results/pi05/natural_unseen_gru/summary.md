# Per-step t_pnr predictor, leave-one-task-out

Labels: full replay scans, K 4, tau 0.5 (>= 3 of 4 succeed = recoverable). Scanned failures: 9; doomed from start (t_pnr 0, left out of timing): 1. Training and test use all natural successes. Threshold (headline table): fixed conformal, alpha 0.05, from cross-fitted scores of all training-group successes. epochs 300, lr 0.001, weight decay 0.001, hidden 256, seed 0, lead 0 steps, progress 0.01 m.

Timely = alarm at or before t_pnr; late = after; lead = t_pnr - t_alarm (positive = early); |err| = mean |t_alarm - t_pnr|; all over alarmed failures with t_pnr > 0. Time-matched AUROC: label-1 steps vs success steps in the same 64-step bin only. Unnecessary alarms on recoverable failures = alarms on failures that never pass a t_pnr.

Episodes: natural: 9 labelled failures, 475 successes (pooled in every number below).

| model | unnecessary alarms on recoverable failures | false alarms on successes | per-step AUROC | time-matched AUROC | failures with t_pnr > 0 | recall | timely | late | missed | median lead (steps) | mean abs err (steps) | median eta |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| progress | 3 of 3 | 0.046 (of 475) | 0.880 | 0.816 | 5 | 1.00 | 1 | 4 | 0 | -48.0 | 105.6 | 1.75 |
| gru | 3 of 3 | 0.032 (of 475) | 0.586 | 0.484 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| gru_cusum | 3 of 3 | 0.027 (of 475) | 0.653 | 0.515 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| gru_phys | 0 of 3 | 0.032 (of 475) | 0.467 | 0.456 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| gru_phys_cusum | 0 of 3 | 0.080 (of 475) | 0.532 | 0.411 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| gru_physvla | 2 of 3 | 0.021 (of 475) | 0.497 | 0.369 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| gru_physvla_cusum | 2 of 3 | 0.013 (of 475) | 0.591 | 0.412 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| gru_physall | 3 of 3 | 0.021 (of 475) | 0.734 | 0.606 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |
| gru_physall_cusum | 3 of 3 | 0.019 (of 475) | 0.762 | 0.633 | 5 | 0.00 | 0 | 0 | 5 | nan | nan | nan |

Timely alarms (at or before t_pnr) / late / missed of the failures with t_pnr > 0, and false alarms on successes, for each threshold and false-alarm limit:

| model | fixed 2.5% | fixed 5.0% | fixed 10.0% | fixed 20.0% | time-varying 2.5% | time-varying 5.0% | time-varying 10.0% | time-varying 20.0% |
|---|---|---|---|---|---|---|---|---|
| progress | 0 / 5 / 0, FA 0.021 | 1 / 4 / 0, FA 0.046 | 1 / 4 / 0, FA 0.097 | 1 / 4 / 0, FA 0.185 | 0 / 5 / 0, FA 0.019 | 0 / 5 / 0, FA 0.074 | 1 / 4 / 0, FA 0.131 | 1 / 4 / 0, FA 0.139 |
| gru | 0 / 0 / 5, FA 0.017 | 0 / 0 / 5, FA 0.032 | 0 / 0 / 5, FA 0.065 | 0 / 1 / 4, FA 0.126 | 0 / 0 / 5, FA 0.023 | 0 / 0 / 5, FA 0.046 | 0 / 0 / 5, FA 0.067 | 0 / 1 / 4, FA 0.137 |
| gru_cusum | 0 / 0 / 5, FA 0.015 | 0 / 0 / 5, FA 0.027 | 0 / 0 / 5, FA 0.063 | 0 / 1 / 4, FA 0.143 | 0 / 0 / 5, FA 0.025 | 0 / 0 / 5, FA 0.048 | 0 / 0 / 5, FA 0.059 | 0 / 1 / 4, FA 0.131 |
| gru_phys | 0 / 0 / 5, FA 0.013 | 0 / 0 / 5, FA 0.032 | 0 / 0 / 5, FA 0.082 | 0 / 0 / 5, FA 0.263 | 0 / 0 / 5, FA 0.103 | 0 / 0 / 5, FA 0.116 | 0 / 0 / 5, FA 0.141 | 0 / 0 / 5, FA 0.192 |
| gru_phys_cusum | 0 / 0 / 5, FA 0.080 | 0 / 0 / 5, FA 0.080 | 0 / 0 / 5, FA 0.088 | 0 / 0 / 5, FA 0.206 | 0 / 0 / 5, FA 0.076 | 0 / 0 / 5, FA 0.116 | 0 / 0 / 5, FA 0.126 | 0 / 0 / 5, FA 0.219 |
| gru_physvla | 0 / 0 / 5, FA 0.013 | 0 / 0 / 5, FA 0.021 | 0 / 0 / 5, FA 0.036 | 0 / 0 / 5, FA 0.097 | 0 / 0 / 5, FA 0.008 | 0 / 0 / 5, FA 0.017 | 0 / 0 / 5, FA 0.044 | 0 / 0 / 5, FA 0.065 |
| gru_physvla_cusum | 0 / 0 / 5, FA 0.013 | 0 / 0 / 5, FA 0.013 | 0 / 0 / 5, FA 0.023 | 0 / 0 / 5, FA 0.099 | 0 / 0 / 5, FA 0.011 | 0 / 0 / 5, FA 0.019 | 0 / 0 / 5, FA 0.042 | 0 / 0 / 5, FA 0.072 |
| gru_physall | 0 / 0 / 5, FA 0.015 | 0 / 0 / 5, FA 0.021 | 0 / 0 / 5, FA 0.048 | 0 / 3 / 2, FA 0.133 | 0 / 0 / 5, FA 0.006 | 0 / 0 / 5, FA 0.015 | 0 / 0 / 5, FA 0.036 | 0 / 0 / 5, FA 0.128 |
| gru_physall_cusum | 0 / 0 / 5, FA 0.015 | 0 / 0 / 5, FA 0.019 | 0 / 0 / 5, FA 0.046 | 0 / 3 / 2, FA 0.147 | 0 / 0 / 5, FA 0.004 | 0 / 0 / 5, FA 0.011 | 0 / 0 / 5, FA 0.042 | 0 / 0 / 5, FA 0.126 |

Labelled failures, per model: t_pnr -> t_alarm (lead time)

- progress t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 112 (lead -112, threshold 6.000)
- progress t00_e49_n0: t_pnr 64 -> t_alarm 112 (lead -48, threshold 6.000)
- gru t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.957)
- gru t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.957)
- gru_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.907)
- gru_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.907)
- gru_phys t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.994)
- gru_phys t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.994)
- gru_phys_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.927)
- gru_phys_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.927)
- gru_physvla t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.863)
- gru_physvla t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.863)
- gru_physvla_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.687)
- gru_physvla_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.687)
- gru_physall t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm None (lead None, threshold 0.698)
- gru_physall t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.698)
- gru_physall_cusum t00_e14_n0: t_pnr 0 (doomed from start) -> t_alarm 408 (lead -408, threshold 0.336)
- gru_physall_cusum t00_e49_n0: t_pnr 64 -> t_alarm None (lead None, threshold 0.336)
- progress t06_e21_n0: t_pnr 304 -> t_alarm 192 (lead 112, threshold 6.000)
- progress t06_e32_n0: t_pnr 56 -> t_alarm 168 (lead -112, threshold 6.000)
- progress t06_e39_n0: t_pnr 128 -> t_alarm 160 (lead -32, threshold 6.000)
- progress t06_e46_n0: t_pnr 56 -> t_alarm 280 (lead -224, threshold 6.000)
- gru t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.523)
- gru t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.523)
- gru t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.523)
- gru t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.523)
- gru_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.522)
- gru_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.522)
- gru_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.522)
- gru_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.522)
- gru_phys t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.999)
- gru_phys t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.999)
- gru_phys t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.999)
- gru_phys t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.999)
- gru_phys_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.996)
- gru_phys_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.996)
- gru_phys_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.996)
- gru_phys_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.996)
- gru_physvla t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.859)
- gru_physvla t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.859)
- gru_physvla t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.859)
- gru_physvla t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.859)
- gru_physvla_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.856)
- gru_physvla_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.856)
- gru_physvla_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.856)
- gru_physvla_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.856)
- gru_physall t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.884)
- gru_physall t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.884)
- gru_physall t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.884)
- gru_physall t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.884)
- gru_physall_cusum t06_e21_n0: t_pnr 304 -> t_alarm None (lead None, threshold 0.799)
- gru_physall_cusum t06_e32_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.799)
- gru_physall_cusum t06_e39_n0: t_pnr 128 -> t_alarm None (lead None, threshold 0.799)
- gru_physall_cusum t06_e46_n0: t_pnr 56 -> t_alarm None (lead None, threshold 0.799)
- progress t07_e03_n0: t_pnr None -> t_alarm 168 (lead None, threshold 6.000)
- progress t07_e16_n0: t_pnr None -> t_alarm 176 (lead None, threshold 6.000)
- progress t07_e33_n0: t_pnr None -> t_alarm 184 (lead None, threshold 6.000)
- gru t07_e03_n0: t_pnr None -> t_alarm 304 (lead None, threshold 0.828)
- gru t07_e16_n0: t_pnr None -> t_alarm 168 (lead None, threshold 0.828)
- gru t07_e33_n0: t_pnr None -> t_alarm 168 (lead None, threshold 0.828)
- gru_cusum t07_e03_n0: t_pnr None -> t_alarm 296 (lead None, threshold 0.816)
- gru_cusum t07_e16_n0: t_pnr None -> t_alarm 160 (lead None, threshold 0.816)
- gru_cusum t07_e33_n0: t_pnr None -> t_alarm 168 (lead None, threshold 0.816)
- gru_phys t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.999)
- gru_phys t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.999)
- gru_phys t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.999)
- gru_phys_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.972)
- gru_phys_cusum t07_e16_n0: t_pnr None -> t_alarm None (lead None, threshold 0.972)
- gru_phys_cusum t07_e33_n0: t_pnr None -> t_alarm None (lead None, threshold 0.972)
- gru_physvla t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.855)
- gru_physvla t07_e16_n0: t_pnr None -> t_alarm 192 (lead None, threshold 0.855)
- gru_physvla t07_e33_n0: t_pnr None -> t_alarm 176 (lead None, threshold 0.855)
- gru_physvla_cusum t07_e03_n0: t_pnr None -> t_alarm None (lead None, threshold 0.837)
- gru_physvla_cusum t07_e16_n0: t_pnr None -> t_alarm 184 (lead None, threshold 0.837)
- gru_physvla_cusum t07_e33_n0: t_pnr None -> t_alarm 176 (lead None, threshold 0.837)
- gru_physall t07_e03_n0: t_pnr None -> t_alarm 160 (lead None, threshold 0.724)
- gru_physall t07_e16_n0: t_pnr None -> t_alarm 160 (lead None, threshold 0.724)
- gru_physall t07_e33_n0: t_pnr None -> t_alarm 168 (lead None, threshold 0.724)
- gru_physall_cusum t07_e03_n0: t_pnr None -> t_alarm 160 (lead None, threshold 0.683)
- gru_physall_cusum t07_e16_n0: t_pnr None -> t_alarm 160 (lead None, threshold 0.683)
- gru_physall_cusum t07_e33_n0: t_pnr None -> t_alarm 160 (lead None, threshold 0.683)
