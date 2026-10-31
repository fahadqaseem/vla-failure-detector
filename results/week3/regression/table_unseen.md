# Regression and ablation, unseen tasks

Natural + perturbed (7 of 10 tasks) + perturbed_v2 (tasks 0, 1, 4, 7), pooled. Timely of failures with t_pnr > 0; false alarms natural / perturbed successes; unnecessary = alarms on recoverable failures; window = median t_alarm - t_pnr (negative = before t_pnr).

| failure threshold | model | timely 0.05 | false alarms 0.05 | unnecessary 0.05 | window 0.05 | timely 0.025 | false alarms 0.025 | unnecessary 0.025 | window 0.025 |
|---|---|---|---|---|---|---|---|---|---|
| 50% | progress | 17 of 81 | 0.049 / 0.047 | 27 of 31 | +144 | 11 of 81 | 0.030 / 0.022 | 22 of 31 | +200 |
| 50% | gru_phys | 12 of 81 | 0.000 / 0.025 | 2 of 31 | +112 | 10 of 81 | 0.000 / 0.025 | 2 of 31 | +136 |
| 50% | gru_phys_frac | 15 of 81 | 0.110 / 0.018 | 4 of 31 | +84 | 13 of 81 | 0.004 / 0.017 | 1 of 31 | +100 |
| 50% | gru_phys_ttp | 11 of 81 | 0.108 / 0.012 | 2 of 31 | +120 | 10 of 81 | 0.004 / 0.010 | 2 of 31 | +120 |
| 50% | gru_robot | 6 of 81 | 0.104 / 0.003 | 0 of 31 | +208 | 4 of 81 | 0.102 / 0.002 | 0 of 31 | +232 |
| 50% | gru_robotobj1 | 4 of 81 | 0.146 / 0.257 | 1 of 31 | +112 | 4 of 81 | 0.133 / 0.220 | 1 of 31 | +112 |
| 50% | gru_robotobj2 | 4 of 81 | 0.144 / 0.252 | 1 of 31 | +104 | 4 of 81 | 0.131 / 0.239 | 1 of 31 | +112 |
| 70% | progress | 22 of 91 | 0.049 / 0.047 | 31 of 35 | +108 | 13 of 91 | 0.030 / 0.022 | 25 of 35 | +156 |
| 70% | gru_phys | 19 of 91 | 0.019 / 0.078 | 8 of 35 | +72 | 17 of 91 | 0.015 / 0.060 | 7 of 35 | +80 |
| 70% | gru_phys_frac | 21 of 91 | 0.011 / 0.022 | 8 of 35 | +68 | 18 of 91 | 0.002 / 0.015 | 4 of 35 | +88 |
| 70% | gru_phys_ttp | 22 of 91 | 0.006 / 0.027 | 7 of 35 | +80 | 16 of 91 | 0.000 / 0.013 | 4 of 35 | +96 |
| 70% | gru_robot | 8 of 91 | 0.104 / 0.003 | 2 of 35 | +104 | 5 of 91 | 0.095 / 0.002 | 1 of 35 | +120 |
| 70% | gru_robotobj1 | 7 of 91 | 0.123 / 0.219 | 1 of 35 | +88 | 7 of 91 | 0.121 / 0.215 | 1 of 35 | +88 |
| 70% | gru_robotobj2 | 7 of 91 | 0.125 / 0.225 | 1 of 35 | +88 | 7 of 91 | 0.121 / 0.217 | 1 of 35 | +88 |
| 80% | progress | 29 of 102 | 0.049 / 0.047 | 35 of 39 | +96 | 17 of 102 | 0.030 / 0.022 | 28 of 39 | +144 |
| 80% | gru_phys | 19 of 102 | 0.017 / 0.067 | 6 of 39 | +52 | 16 of 102 | 0.015 / 0.062 | 6 of 39 | +56 |
| 80% | gru_phys_frac | 27 of 102 | 0.015 / 0.043 | 12 of 39 | +48 | 23 of 102 | 0.002 / 0.025 | 8 of 39 | +60 |
| 80% | gru_phys_ttp | 24 of 102 | 0.006 / 0.040 | 8 of 39 | +56 | 20 of 102 | 0.002 / 0.020 | 7 of 39 | +80 |
| 80% | gru_robot | 6 of 102 | 0.078 / 0.005 | 4 of 39 | +72 | 3 of 102 | 0.032 / 0.005 | 3 of 39 | +116 |
| 80% | gru_robotobj1 | 9 of 102 | 0.106 / 0.207 | 3 of 39 | +48 | 8 of 102 | 0.104 / 0.207 | 3 of 39 | +56 |
| 80% | gru_robotobj2 | 9 of 102 | 0.104 / 0.207 | 3 of 39 | +60 | 8 of 102 | 0.104 / 0.204 | 3 of 39 | +68 |

## Regression error

| failure threshold | model | error | value |
|---|---|---|---|
| 50% | gru_phys_frac | MAE failure fraction, scanned queries (10465) | 0.248 |
| 50% | gru_phys_frac | MAE failure fraction, all known queries (44193) | 0.212 |
| 50% | gru_phys_ttp | MAE steps until t_pnr, all queries (45233) | 47.3 |
| 50% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (1691) | 81.0 |
| 70% | gru_phys_frac | MAE failure fraction, scanned queries (10465) | 0.260 |
| 70% | gru_phys_frac | MAE failure fraction, all known queries (44193) | 0.203 |
| 70% | gru_phys_ttp | MAE steps until t_pnr, all queries (45233) | 41.9 |
| 70% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (2376) | 81.5 |
| 80% | gru_phys_frac | MAE failure fraction, scanned queries (10465) | 0.270 |
| 80% | gru_phys_frac | MAE failure fraction, all known queries (44193) | 0.189 |
| 80% | gru_phys_ttp | MAE steps until t_pnr, all queries (45233) | 36.8 |
| 80% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (2728) | 78.2 |
