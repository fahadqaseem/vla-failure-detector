# Regression and ablation, seen tasks

Pi0.5: natural (500) + perturbed 2 to 3 cm, seeds 0 and 1, gate-passed tasks only, pooled. Timely of failures with t_pnr > 0; false alarms natural / perturbed successes; unnecessary = alarms on recoverable failures; window = median t_alarm - t_pnr (negative = before t_pnr).

| failure threshold | model | timely 0.05 | false alarms 0.05 | unnecessary 0.05 | window 0.05 | timely 0.025 | false alarms 0.025 | unnecessary 0.025 | window 0.025 |
|---|---|---|---|---|---|---|---|---|---|
| 50% | progress | 6 of 27 | 0.038 / 0.057 | 6 of 7 | +96 | 1 of 27 | 0.017 / 0.024 | 6 of 7 | +160 |
| 50% | gru_phys | 10 of 27 | 0.021 / 0.086 | 3 of 7 | +56 | 7 of 27 | 0.011 / 0.040 | 2 of 7 | +72 |
| 50% | gru_phys_frac | 11 of 27 | 0.025 / 0.088 | 5 of 7 | +32 | 9 of 27 | 0.013 / 0.031 | 2 of 7 | +56 |
| 50% | gru_phys_ttp | 11 of 27 | 0.023 / 0.079 | 3 of 7 | +28 | 10 of 27 | 0.013 / 0.033 | 1 of 7 | -32 |
| 70% | progress | 9 of 31 | 0.038 / 0.057 | 6 of 7 | +76 | 6 of 31 | 0.017 / 0.024 | 6 of 7 | +152 |
| 70% | gru_phys | 14 of 31 | 0.027 / 0.084 | 3 of 7 | -16 | 9 of 31 | 0.019 / 0.033 | 2 of 7 | +36 |
| 70% | gru_phys_frac | 17 of 31 | 0.029 / 0.088 | 5 of 7 | -32 | 11 of 31 | 0.015 / 0.033 | 4 of 7 | +32 |
| 70% | gru_phys_ttp | 17 of 31 | 0.029 / 0.088 | 2 of 7 | -36 | 13 of 31 | 0.017 / 0.033 | 2 of 7 | -8 |
| 80% | progress | 18 of 33 | 0.038 / 0.057 | 7 of 8 | -44 | 12 of 33 | 0.017 / 0.024 | 7 of 8 | +40 |
| 80% | gru_phys | 18 of 33 | 0.032 / 0.102 | 4 of 8 | -88 | 13 of 33 | 0.017 / 0.022 | 4 of 8 | -32 |
| 80% | gru_phys_frac | 20 of 33 | 0.027 / 0.088 | 5 of 8 | -128 | 17 of 33 | 0.019 / 0.022 | 3 of 8 | -64 |
| 80% | gru_phys_ttp | 19 of 33 | 0.027 / 0.084 | 4 of 8 | -104 | 17 of 33 | 0.017 / 0.022 | 3 of 8 | -72 |

## Regression error

| failure threshold | model | error | value |
|---|---|---|---|
| 50% | gru_phys_frac | MAE failure fraction, scanned queries (2955) | 0.326 |
| 50% | gru_phys_frac | MAE failure fraction, all known queries (32032) | 0.118 |
| 50% | gru_phys_ttp | MAE steps until t_pnr, all queries (32292) | 25.7 |
| 50% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (694) | 81.3 |
| 70% | gru_phys_frac | MAE failure fraction, scanned queries (2955) | 0.326 |
| 70% | gru_phys_frac | MAE failure fraction, all known queries (32032) | 0.105 |
| 70% | gru_phys_ttp | MAE steps until t_pnr, all queries (32292) | 20.9 |
| 70% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (966) | 72.9 |
| 80% | gru_phys_frac | MAE failure fraction, scanned queries (2955) | 0.328 |
| 80% | gru_phys_frac | MAE failure fraction, all known queries (32032) | 0.091 |
| 80% | gru_phys_ttp | MAE steps until t_pnr, all queries (32292) | 18.6 |
| 80% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (1234) | 77.6 |
