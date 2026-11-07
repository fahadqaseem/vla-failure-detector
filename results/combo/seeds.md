# progress OR gru_phys_ttp over seeds 0 to 4, unseen tasks

OR combination over seeds (Fahad, Nov 7): progress OR gru_phys_ttp for seeds 0 to 4, both policies, three rules, unseen tasks, budgets 2.5% and 5%, thresholds from the training-task calibration successes of each fold (47_combo.py, same rule as results/combo). Seed 0 = data/combo/{policy}/thr{T}/merged, seeds 1 to 4 = data/combo_seeds/{policy}/thr{T}/s{S}/merged (gru_phys_ttp retrained with --save_calib; progress has no seed and is reused). Per setting: mean and min to max over the 5 seeds of timely (alarm at or before t_pnr, failures with t_pnr > 0), false alarms on successes and unnecessary alarms on recoverable failures, and how many seeds beat progress (more timely; ties apart).

| policy | rule | budget | timely OR, mean (min to max) | progress timely | seeds beating progress (ties) | false alarms OR | progress false alarms | unnecessary OR | progress unnecessary |
|---|---|---|---|---|---|---|---|---|---|
| OpenVLA-OFT | 50% | 0.025 | 14.8 (13.0 to 18.0) of 81 | 11 | 5 of 5 (0) | 0.023 (0.018 to 0.034) | 0.025 | 21.0 (21.0 to 21.0) of 31 | 22 |
| OpenVLA-OFT | 50% | 0.05 | 19.2 (16.0 to 22.0) of 81 | 17 | 3 of 5 (1) | 0.059 (0.042 to 0.088) | 0.048 | 24.0 (23.0 to 25.0) of 31 | 27 |
| OpenVLA-OFT | 70% | 0.025 | 23.0 (21.0 to 27.0) of 91 | 13 | 5 of 5 (0) | 0.025 (0.019 to 0.033) | 0.025 | 24.8 (24.0 to 26.0) of 35 | 25 |
| OpenVLA-OFT | 70% | 0.05 | 28.6 (26.0 to 32.0) of 91 | 22 | 5 of 5 (0) | 0.044 (0.034 to 0.063) | 0.048 | 28.4 (28.0 to 30.0) of 35 | 31 |
| OpenVLA-OFT | 80% | 0.025 | 26.0 (24.0 to 29.0) of 102 | 17 | 5 of 5 (0) | 0.023 (0.019 to 0.030) | 0.025 | 29.2 (28.0 to 30.0) of 39 | 28 |
| OpenVLA-OFT | 80% | 0.05 | 33.4 (31.0 to 35.0) of 102 | 29 | 5 of 5 (0) | 0.044 (0.035 to 0.053) | 0.048 | 33.0 (33.0 to 33.0) of 39 | 35 |
| Pi0.5 | 50% | 0.025 | 5.8 (3.0 to 9.0) of 27 | 2 | 5 of 5 (0) | 0.016 (0.013 to 0.024) | 0.025 | 5.4 (5.0 to 6.0) of 7 | 6 |
| Pi0.5 | 50% | 0.05 | 6.8 (4.0 to 9.0) of 27 | 5 | 4 of 5 (0) | 0.030 (0.026 to 0.039) | 0.050 | 6.4 (6.0 to 7.0) of 7 | 6 |
| Pi0.5 | 70% | 0.025 | 9.0 (6.0 to 12.0) of 31 | 6 | 4 of 5 (1) | 0.017 (0.013 to 0.024) | 0.025 | 5.4 (5.0 to 6.0) of 7 | 6 |
| Pi0.5 | 70% | 0.05 | 10.0 (7.0 to 13.0) of 31 | 8 | 3 of 5 (1) | 0.031 (0.028 to 0.033) | 0.050 | 6.4 (6.0 to 7.0) of 7 | 6 |
| Pi0.5 | 80% | 0.025 | 10.4 (9.0 to 12.0) of 33 | 12 | 0 of 5 (1) | 0.014 (0.013 to 0.015) | 0.025 | 6.0 (6.0 to 6.0) of 8 | 7 |
| Pi0.5 | 80% | 0.05 | 13.4 (12.0 to 15.0) of 33 | 17 | 0 of 5 (0) | 0.027 (0.025 to 0.029) | 0.050 | 7.0 (7.0 to 7.0) of 8 | 7 |
