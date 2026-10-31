# Regression and ablation, seen tasks

Natural + perturbed (7 of 10 tasks) + perturbed_v2 (tasks 0, 1, 4, 7), pooled. Timely of failures with t_pnr > 0; false alarms natural / perturbed successes; unnecessary = alarms on recoverable failures; window = median t_alarm - t_pnr (negative = before t_pnr).

| failure threshold | model | timely 0.05 | false alarms 0.05 | unnecessary 0.05 | window 0.05 | timely 0.025 | false alarms 0.025 | unnecessary 0.025 | window 0.025 |
|---|---|---|---|---|---|---|---|---|---|
| 50% | progress | 16 of 81 | 0.049 / 0.043 | 26 of 31 | +144 | 11 of 81 | 0.032 / 0.022 | 22 of 31 | +180 |
| 50% | gru_phys | 23 of 81 | 0.032 / 0.067 | 15 of 31 | +48 | 19 of 81 | 0.015 / 0.032 | 10 of 31 | +64 |
| 50% | gru_phys_frac | 19 of 81 | 0.030 / 0.063 | 23 of 31 | +56 | 17 of 81 | 0.013 / 0.037 | 12 of 31 | +64 |
| 50% | gru_phys_ttp | 18 of 81 | 0.034 / 0.060 | 18 of 31 | +56 | 17 of 81 | 0.013 / 0.035 | 10 of 31 | +64 |
| 50% | gru_robot | 17 of 81 | 0.019 / 0.063 | 14 of 31 | +84 | 11 of 81 | 0.015 / 0.025 | 9 of 31 | +120 |
| 50% | gru_robotobj1 | 16 of 81 | 0.021 / 0.058 | 19 of 31 | +92 | 9 of 81 | 0.006 / 0.035 | 14 of 31 | +124 |
| 50% | gru_robotobj2 | 17 of 81 | 0.021 / 0.063 | 18 of 31 | +80 | 10 of 81 | 0.008 / 0.035 | 12 of 31 | +124 |
| 70% | progress | 22 of 91 | 0.049 / 0.043 | 29 of 35 | +112 | 15 of 91 | 0.032 / 0.022 | 25 of 35 | +136 |
| 70% | gru_phys | 36 of 91 | 0.025 / 0.062 | 20 of 35 | +16 | 27 of 91 | 0.006 / 0.025 | 14 of 35 | +32 |
| 70% | gru_phys_frac | 35 of 91 | 0.030 / 0.063 | 26 of 35 | +24 | 28 of 91 | 0.013 / 0.035 | 18 of 35 | +48 |
| 70% | gru_phys_ttp | 34 of 91 | 0.030 / 0.060 | 20 of 35 | +24 | 28 of 91 | 0.015 / 0.033 | 14 of 35 | +48 |
| 70% | gru_robot | 29 of 91 | 0.025 / 0.058 | 15 of 35 | +56 | 19 of 91 | 0.013 / 0.027 | 13 of 35 | +80 |
| 70% | gru_robotobj1 | 31 of 91 | 0.021 / 0.072 | 18 of 35 | +40 | 22 of 91 | 0.004 / 0.037 | 13 of 35 | +72 |
| 70% | gru_robotobj2 | 31 of 91 | 0.023 / 0.075 | 17 of 35 | +24 | 21 of 91 | 0.004 / 0.037 | 15 of 35 | +72 |
| 80% | progress | 28 of 102 | 0.049 / 0.043 | 33 of 39 | +104 | 18 of 102 | 0.032 / 0.022 | 28 of 39 | +128 |
| 80% | gru_phys | 49 of 102 | 0.021 / 0.055 | 17 of 39 | +0 | 35 of 102 | 0.006 / 0.033 | 16 of 39 | +24 |
| 80% | gru_phys_frac | 52 of 102 | 0.030 / 0.060 | 27 of 39 | +0 | 35 of 102 | 0.013 / 0.032 | 18 of 39 | +32 |
| 80% | gru_phys_ttp | 51 of 102 | 0.028 / 0.075 | 18 of 39 | +0 | 37 of 102 | 0.011 / 0.033 | 14 of 39 | +32 |
| 80% | gru_robot | 38 of 102 | 0.025 / 0.058 | 18 of 39 | +40 | 29 of 102 | 0.013 / 0.025 | 16 of 39 | +60 |
| 80% | gru_robotobj1 | 38 of 102 | 0.021 / 0.073 | 15 of 39 | +24 | 31 of 102 | 0.004 / 0.033 | 13 of 39 | +40 |
| 80% | gru_robotobj2 | 38 of 102 | 0.017 / 0.062 | 16 of 39 | +24 | 30 of 102 | 0.006 / 0.038 | 14 of 39 | +48 |

## Regression error

| failure threshold | model | error | value |
|---|---|---|---|
| 50% | gru_phys_frac | MAE failure fraction, scanned queries (10465) | 0.205 |
| 50% | gru_phys_frac | MAE failure fraction, all known queries (44193) | 0.147 |
| 50% | gru_phys_ttp | MAE steps until t_pnr, all queries (45233) | 33.3 |
| 50% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (1691) | 75.4 |
| 70% | gru_phys_frac | MAE failure fraction, scanned queries (10465) | 0.210 |
| 70% | gru_phys_frac | MAE failure fraction, all known queries (44193) | 0.134 |
| 70% | gru_phys_ttp | MAE steps until t_pnr, all queries (45233) | 27.6 |
| 70% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (2376) | 71.1 |
| 80% | gru_phys_frac | MAE failure fraction, scanned queries (10465) | 0.216 |
| 80% | gru_phys_frac | MAE failure fraction, all known queries (44193) | 0.127 |
| 80% | gru_phys_ttp | MAE steps until t_pnr, all queries (45233) | 24.3 |
| 80% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (2728) | 69.4 |
