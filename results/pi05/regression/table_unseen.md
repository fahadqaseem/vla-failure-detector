# Regression and ablation, unseen tasks

Pi0.5: natural (500) + perturbed 2 to 3 cm, seeds 0 and 1, gate-passed tasks only, pooled. Timely of failures with t_pnr > 0; false alarms natural / perturbed successes; unnecessary = alarms on recoverable failures; window = median t_alarm - t_pnr (negative = before t_pnr).

| failure threshold | model | timely 0.05 | false alarms 0.05 | unnecessary 0.05 | window 0.05 | timely 0.025 | false alarms 0.025 | unnecessary 0.025 | window 0.025 |
|---|---|---|---|---|---|---|---|---|---|
| 50% | progress | 5 of 27 | 0.040 / 0.060 | 6 of 7 | +104 | 2 of 27 | 0.021 / 0.029 | 6 of 7 | +144 |
| 50% | gru_phys | 3 of 27 | 0.006 / 0.024 | 1 of 7 | +72 | 3 of 27 | 0.002 / 0.015 | 1 of 7 | +128 |
| 50% | gru_phys_frac | 8 of 27 | 0.002 / 0.009 | 0 of 7 | -104 | 6 of 27 | 0.002 / 0.004 | 0 of 7 | -96 |
| 50% | gru_phys_ttp | 9 of 27 | 0.006 / 0.011 | 1 of 7 | -96 | 8 of 27 | 0.004 / 0.007 | 1 of 7 | -64 |
| 70% | progress | 8 of 31 | 0.040 / 0.060 | 6 of 7 | +84 | 6 of 31 | 0.021 / 0.029 | 6 of 7 | +136 |
| 70% | gru_phys | 3 of 31 | 0.000 / 0.009 | 1 of 7 | +44 | 3 of 31 | 0.000 / 0.000 | 1 of 7 | +56 |
| 70% | gru_phys_frac | 7 of 31 | 0.004 / 0.020 | 0 of 7 | -132 | 6 of 31 | 0.002 / 0.009 | 0 of 7 | -132 |
| 70% | gru_phys_ttp | 10 of 31 | 0.008 / 0.020 | 0 of 7 | -88 | 9 of 31 | 0.004 / 0.011 | 0 of 7 | -72 |
| 80% | progress | 17 of 33 | 0.040 / 0.060 | 7 of 8 | -28 | 12 of 33 | 0.021 / 0.029 | 7 of 8 | +40 |
| 80% | gru_phys | 0 of 33 | 0.000 / 0.002 | 0 of 8 | +144 | 0 of 33 | 0.000 / 0.000 | 0 of 8 | +156 |
| 80% | gru_phys_frac | 5 of 33 | 0.000 / 0.007 | 0 of 8 | -208 | 4 of 33 | 0.000 / 0.002 | 0 of 8 | -240 |
| 80% | gru_phys_ttp | 7 of 33 | 0.002 / 0.009 | 1 of 8 | -192 | 6 of 33 | 0.002 / 0.002 | 1 of 8 | -136 |

## Regression error

| failure threshold | model | error | value |
|---|---|---|---|
| 50% | gru_phys_frac | MAE failure fraction, scanned queries (2955) | 0.347 |
| 50% | gru_phys_frac | MAE failure fraction, all known queries (32032) | 0.175 |
| 50% | gru_phys_ttp | MAE steps until t_pnr, all queries (32292) | 34.8 |
| 50% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (694) | 83.5 |
| 70% | gru_phys_frac | MAE failure fraction, scanned queries (2955) | 0.400 |
| 70% | gru_phys_frac | MAE failure fraction, all known queries (32032) | 0.196 |
| 70% | gru_phys_ttp | MAE steps until t_pnr, all queries (32292) | 40.1 |
| 70% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (966) | 87.0 |
| 80% | gru_phys_frac | MAE failure fraction, scanned queries (2955) | 0.397 |
| 80% | gru_phys_frac | MAE failure fraction, all known queries (32032) | 0.209 |
| 80% | gru_phys_ttp | MAE steps until t_pnr, all queries (32292) | 44.2 |
| 80% | gru_phys_ttp | MAE steps until t_pnr, timed failures before t_pnr (1234) | 89.9 |
