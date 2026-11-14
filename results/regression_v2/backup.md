# Backup only: alarms from the regression scores, seed 0

Threshold per held-out task = conformal quantile (alpha 0.025) of the per-run max score of the training-task successes, cross-fitted (each training task scored by a model trained on the other 8). Alarm = first query above it. Timely = alarm at or before t_pnr, of the kept failures with t_pnr > 0 under that rule. False alarms = held-out successes with any alarm.

| policy | model | timely 50% rule | timely 70% rule | false alarms on successes |
|---|---|---|---|---|
| OpenVLA-OFT | gru_phys_frac | 9 of 81 (11%) | 16 of 91 (18%) | 14 of 1071 (0.013) |
| OpenVLA-OFT | safe_lin | 14 of 81 (17%) | 31 of 91 (34%) | 38 of 1071 (0.035) |
| OpenVLA-OFT | safe_mlp | 13 of 81 (16%) | 25 of 91 (27%) | 103 of 1071 (0.096) |
| OpenVLA-OFT | safe_lstm | 16 of 81 (20%) | 27 of 91 (30%) | 122 of 1071 (0.114) |
| OpenVLA-OFT | gru_physvla_frac | 6 of 81 (7%) | 16 of 91 (18%) | 125 of 1071 (0.117) |
| OpenVLA-OFT | const | 0 of 81 (0%) | 0 of 91 (0%) | 0 of 1071 (0.000) |
| OpenVLA-OFT | progress_iso | 11 of 81 (14%) | 13 of 91 (14%) | 23 of 1071 (0.021) |
| OpenVLA-OFT | timer_iso | 6 of 81 (7%) | 9 of 91 (10%) | 47 of 1071 (0.044) |
| Pi0.5 | gru_phys_frac | 2 of 27 (7%) | 2 of 31 (6%) | 43 of 928 (0.046) |
| Pi0.5 | safe_lin | 0 of 27 (0%) | 0 of 31 (0%) | 99 of 928 (0.107) |
| Pi0.5 | safe_mlp | 2 of 27 (7%) | 4 of 31 (13%) | 34 of 928 (0.037) |
| Pi0.5 | safe_lstm | 1 of 27 (4%) | 1 of 31 (3%) | 8 of 928 (0.009) |
| Pi0.5 | gru_physvla_frac | 2 of 27 (7%) | 3 of 31 (10%) | 9 of 928 (0.010) |
| Pi0.5 | const | 0 of 27 (0%) | 0 of 31 (0%) | 0 of 928 (0.000) |
| Pi0.5 | progress_iso | 3 of 27 (11%) | 7 of 31 (23%) | 23 of 928 (0.025) |
| Pi0.5 | timer_iso | 1 of 27 (4%) | 5 of 31 (16%) | 38 of 928 (0.041) |
