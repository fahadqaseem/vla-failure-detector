# Few-shot calibration on the held-out task, unseen tasks

Few-shot calibration on the held-out task (Fahad, Nov 7, item 7), existing scores, no retraining, unseen tasks: for each held-out task, k = 5, 10, 20 successes of that task drawn at random (20 draws, seed 0) give the threshold (fixed conformal at the budget; when k is too small for the budget the conformal rule is infinite, so the max of the k is used instead, which aims at about 1 / (k + 1) false alarms). Scored on the task's other runs: realized false alarms on its other successes and timely alarms on its failures with t_pnr > 0. Tasks with fewer than k + 1 successes are left out at that k. "training-task threshold" = the usual threshold of the same model.

| policy | rule | budget | model | threshold from | tasks | timely (mean over draws) | false alarms on other successes (mean) |
|---|---|---|---|---|---|---|---|
| OpenVLA-OFT | 50% | 0.025 | progress | training tasks | 10 | 11 of 81 | 0.025 |
| OpenVLA-OFT | 50% | 0.025 | progress | k = 5 of the held-out task | 10 | 20.1 of 81 | 0.105 |
| OpenVLA-OFT | 50% | 0.025 | progress | k = 10 of the held-out task | 10 | 17.0 of 81 | 0.065 |
| OpenVLA-OFT | 50% | 0.025 | progress | k = 20 of the held-out task | 10 | 13.2 of 81 | 0.034 |
| OpenVLA-OFT | 50% | 0.05 | progress | training tasks | 10 | 17 of 81 | 0.048 |
| OpenVLA-OFT | 50% | 0.05 | progress | k = 5 of the held-out task | 10 | 20.1 of 81 | 0.105 |
| OpenVLA-OFT | 50% | 0.05 | progress | k = 10 of the held-out task | 10 | 17.0 of 81 | 0.065 |
| OpenVLA-OFT | 50% | 0.05 | progress | k = 20 of the held-out task | 10 | 13.2 of 81 | 0.034 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s0 | training tasks | 10 | 10 of 81 | 0.007 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 26.4 of 81 | 0.178 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 19.7 of 81 | 0.084 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 14.0 of 81 | 0.047 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s0 | training tasks | 10 | 11 of 81 | 0.054 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 26.4 of 81 | 0.178 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 19.7 of 81 | 0.084 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 14.0 of 81 | 0.047 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp_ens | training tasks | 10 | 15 of 81 | 0.016 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 25.1 of 81 | 0.181 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 18.3 of 81 | 0.086 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 13.1 of 81 | 0.046 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp_ens | training tasks | 10 | 16 of 81 | 0.055 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 25.1 of 81 | 0.181 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 18.3 of 81 | 0.086 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 13.1 of 81 | 0.046 |
| OpenVLA-OFT | 70% (main) | 0.025 | progress | training tasks | 10 | 13 of 91 | 0.025 |
| OpenVLA-OFT | 70% (main) | 0.025 | progress | k = 5 of the held-out task | 10 | 32.2 of 91 | 0.105 |
| OpenVLA-OFT | 70% (main) | 0.025 | progress | k = 10 of the held-out task | 10 | 26.9 of 91 | 0.065 |
| OpenVLA-OFT | 70% (main) | 0.025 | progress | k = 20 of the held-out task | 10 | 19.3 of 91 | 0.034 |
| OpenVLA-OFT | 70% (main) | 0.05 | progress | training tasks | 10 | 22 of 91 | 0.048 |
| OpenVLA-OFT | 70% (main) | 0.05 | progress | k = 5 of the held-out task | 10 | 32.2 of 91 | 0.105 |
| OpenVLA-OFT | 70% (main) | 0.05 | progress | k = 10 of the held-out task | 10 | 26.9 of 91 | 0.065 |
| OpenVLA-OFT | 70% (main) | 0.05 | progress | k = 20 of the held-out task | 10 | 19.3 of 91 | 0.034 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s0 | training tasks | 10 | 16 of 91 | 0.007 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 35.8 of 91 | 0.182 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 27.1 of 91 | 0.085 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 20.9 of 91 | 0.047 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s0 | training tasks | 10 | 22 of 91 | 0.018 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 35.8 of 91 | 0.182 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 27.1 of 91 | 0.085 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 20.9 of 91 | 0.047 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp_ens | training tasks | 10 | 20 of 91 | 0.014 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 35.6 of 91 | 0.182 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 26.8 of 91 | 0.082 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 21.8 of 91 | 0.047 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp_ens | training tasks | 10 | 24 of 91 | 0.024 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 35.6 of 91 | 0.182 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 26.8 of 91 | 0.082 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 21.8 of 91 | 0.047 |
| OpenVLA-OFT | 80% | 0.025 | progress | training tasks | 10 | 17 of 102 | 0.025 |
| OpenVLA-OFT | 80% | 0.025 | progress | k = 5 of the held-out task | 10 | 39.4 of 102 | 0.105 |
| OpenVLA-OFT | 80% | 0.025 | progress | k = 10 of the held-out task | 10 | 32.5 of 102 | 0.065 |
| OpenVLA-OFT | 80% | 0.025 | progress | k = 20 of the held-out task | 10 | 24.1 of 102 | 0.034 |
| OpenVLA-OFT | 80% | 0.05 | progress | training tasks | 10 | 29 of 102 | 0.048 |
| OpenVLA-OFT | 80% | 0.05 | progress | k = 5 of the held-out task | 10 | 39.4 of 102 | 0.105 |
| OpenVLA-OFT | 80% | 0.05 | progress | k = 10 of the held-out task | 10 | 32.5 of 102 | 0.065 |
| OpenVLA-OFT | 80% | 0.05 | progress | k = 20 of the held-out task | 10 | 24.1 of 102 | 0.034 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s0 | training tasks | 10 | 20 of 102 | 0.012 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 41.0 of 102 | 0.180 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 30.9 of 102 | 0.088 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 24.4 of 102 | 0.049 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s0 | training tasks | 10 | 24 of 102 | 0.025 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 41.0 of 102 | 0.180 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 30.9 of 102 | 0.088 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 24.4 of 102 | 0.049 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp_ens | training tasks | 10 | 24 of 102 | 0.019 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 41.6 of 102 | 0.173 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 31.7 of 102 | 0.086 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 25.3 of 102 | 0.047 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp_ens | training tasks | 10 | 28 of 102 | 0.024 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 41.6 of 102 | 0.173 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 31.7 of 102 | 0.086 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 25.3 of 102 | 0.047 |
| Pi0.5 | 50% | 0.025 | progress | training tasks | 10 | 2 of 27 | 0.025 |
| Pi0.5 | 50% | 0.025 | progress | k = 5 of the held-out task | 10 | 8.7 of 27 | 0.112 |
| Pi0.5 | 50% | 0.025 | progress | k = 10 of the held-out task | 10 | 4.5 of 27 | 0.065 |
| Pi0.5 | 50% | 0.025 | progress | k = 20 of the held-out task | 10 | 3.5 of 27 | 0.042 |
| Pi0.5 | 50% | 0.05 | progress | training tasks | 10 | 5 of 27 | 0.050 |
| Pi0.5 | 50% | 0.05 | progress | k = 5 of the held-out task | 10 | 8.7 of 27 | 0.112 |
| Pi0.5 | 50% | 0.05 | progress | k = 10 of the held-out task | 10 | 4.5 of 27 | 0.065 |
| Pi0.5 | 50% | 0.05 | progress | k = 20 of the held-out task | 10 | 3.5 of 27 | 0.042 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s0 | training tasks | 10 | 8 of 27 | 0.005 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 11.9 of 27 | 0.149 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 11.2 of 27 | 0.088 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 10.3 of 27 | 0.053 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s0 | training tasks | 10 | 9 of 27 | 0.009 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 11.9 of 27 | 0.149 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 11.2 of 27 | 0.088 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 10.3 of 27 | 0.053 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp_ens | training tasks | 10 | 5 of 27 | 0.000 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 11.9 of 27 | 0.153 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 10.8 of 27 | 0.085 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 10.2 of 27 | 0.052 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp_ens | training tasks | 10 | 6 of 27 | 0.006 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 11.9 of 27 | 0.153 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 10.8 of 27 | 0.085 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 10.2 of 27 | 0.052 |
| Pi0.5 | 70% (main) | 0.025 | progress | training tasks | 10 | 6 of 31 | 0.025 |
| Pi0.5 | 70% (main) | 0.025 | progress | k = 5 of the held-out task | 10 | 14.4 of 31 | 0.112 |
| Pi0.5 | 70% (main) | 0.025 | progress | k = 10 of the held-out task | 10 | 10.2 of 31 | 0.065 |
| Pi0.5 | 70% (main) | 0.025 | progress | k = 20 of the held-out task | 10 | 8.5 of 31 | 0.042 |
| Pi0.5 | 70% (main) | 0.05 | progress | training tasks | 10 | 8 of 31 | 0.050 |
| Pi0.5 | 70% (main) | 0.05 | progress | k = 5 of the held-out task | 10 | 14.4 of 31 | 0.112 |
| Pi0.5 | 70% (main) | 0.05 | progress | k = 10 of the held-out task | 10 | 10.2 of 31 | 0.065 |
| Pi0.5 | 70% (main) | 0.05 | progress | k = 20 of the held-out task | 10 | 8.5 of 31 | 0.042 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s0 | training tasks | 10 | 9 of 31 | 0.008 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 14.3 of 31 | 0.172 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 11.8 of 31 | 0.086 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 10.4 of 31 | 0.053 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s0 | training tasks | 10 | 10 of 31 | 0.014 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 14.3 of 31 | 0.172 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 11.8 of 31 | 0.086 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 10.4 of 31 | 0.053 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp_ens | training tasks | 10 | 5 of 31 | 0.003 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 14.6 of 31 | 0.162 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 12.1 of 31 | 0.084 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 10.1 of 31 | 0.052 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp_ens | training tasks | 10 | 6 of 31 | 0.006 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 14.6 of 31 | 0.162 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 12.1 of 31 | 0.084 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 10.1 of 31 | 0.052 |
| Pi0.5 | 80% | 0.025 | progress | training tasks | 10 | 12 of 33 | 0.025 |
| Pi0.5 | 80% | 0.025 | progress | k = 5 of the held-out task | 10 | 20.5 of 33 | 0.112 |
| Pi0.5 | 80% | 0.025 | progress | k = 10 of the held-out task | 10 | 15.4 of 33 | 0.065 |
| Pi0.5 | 80% | 0.025 | progress | k = 20 of the held-out task | 10 | 13.8 of 33 | 0.042 |
| Pi0.5 | 80% | 0.05 | progress | training tasks | 10 | 17 of 33 | 0.050 |
| Pi0.5 | 80% | 0.05 | progress | k = 5 of the held-out task | 10 | 20.5 of 33 | 0.112 |
| Pi0.5 | 80% | 0.05 | progress | k = 10 of the held-out task | 10 | 15.4 of 33 | 0.065 |
| Pi0.5 | 80% | 0.05 | progress | k = 20 of the held-out task | 10 | 13.8 of 33 | 0.042 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s0 | training tasks | 10 | 6 of 33 | 0.002 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 15.2 of 33 | 0.167 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 13.6 of 33 | 0.087 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 10.8 of 33 | 0.050 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s0 | training tasks | 10 | 7 of 33 | 0.005 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s0 | k = 5 of the held-out task | 10 | 15.2 of 33 | 0.167 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s0 | k = 10 of the held-out task | 10 | 13.6 of 33 | 0.087 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s0 | k = 20 of the held-out task | 10 | 10.8 of 33 | 0.050 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp_ens | training tasks | 10 | 3 of 33 | 0.002 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 14.2 of 33 | 0.167 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 12.6 of 33 | 0.090 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 10.7 of 33 | 0.052 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp_ens | training tasks | 10 | 5 of 33 | 0.003 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp_ens | k = 5 of the held-out task | 10 | 14.2 of 33 | 0.167 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp_ens | k = 10 of the held-out task | 10 | 12.6 of 33 | 0.090 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp_ens | k = 20 of the held-out task | 10 | 10.7 of 33 | 0.052 |
