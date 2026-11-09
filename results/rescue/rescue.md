# Rescue value of alarms, unseen tasks

Rescue value (Fahad, Nov 7, item 5), unseen tasks: for every alarm on a scanned failure, the retry success fraction at the last scanned checkpoint at or before the alarm (existing replay scans, K 4, plus the K 12 refinement for OpenVLA-OFT), summed into expected rescues per 100 held-out runs, next to false alarms per 100 runs (alarmed successes). Two versions: retries as scanned (up to 200 steps past the 520-step limit) and only retries that succeed by step 520. Alarms on unscanned failures (pre-check recoverable) are counted apart, with no value. A retry here is the same policy restarted from the saved state with action noise 0.05, not a human intervention.

| policy | rule | budget | model | runs | alarms on scanned failures | expected rescues / 100 runs (as scanned) | (by step 520) | false alarms / 100 runs | alarms on unscanned failures |
|---|---|---|---|---|---|---|---|---|---|
| OpenVLA-OFT | 50% | 0.025 | progress | 1238 | 91 | 1.39 | 0.90 | 2.18 | 12 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s0 | 1238 | 90 | 0.71 | 0.53 | 0.65 | 2 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s1 | 1238 | 98 | 0.75 | 0.55 | 0.97 | 2 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s2 | 1238 | 96 | 0.68 | 0.47 | 1.70 | 2 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s3 | 1238 | 99 | 0.86 | 0.64 | 3.96 | 2 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s4 | 1238 | 97 | 0.62 | 0.40 | 3.72 | 1 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp_ens | 1238 | 101 | 0.93 | 0.67 | 1.37 | 3 |
| OpenVLA-OFT | 50% | 0.025 | or_progress_ttp s0 | 1238 | 122 | 1.64 | 1.02 | 1.53 | 12 |
| OpenVLA-OFT | 50% | 0.025 | or_progress_ttp s1 | 1238 | 125 | 1.76 | 1.16 | 1.86 | 12 |
| OpenVLA-OFT | 50% | 0.025 | or_progress_ttp s2 | 1238 | 122 | 1.57 | 0.98 | 1.62 | 12 |
| OpenVLA-OFT | 50% | 0.025 | or_progress_ttp s3 | 1238 | 125 | 1.76 | 1.16 | 2.91 | 12 |
| OpenVLA-OFT | 50% | 0.025 | or_progress_ttp s4 | 1238 | 122 | 1.51 | 0.90 | 2.02 | 12 |
| OpenVLA-OFT | 50% | 0.025 | or_progress_ens | 1238 | 122 | 1.62 | 1.01 | 1.53 | 12 |
| OpenVLA-OFT | 50% | 0.05 | progress | 1238 | 114 | 1.67 | 1.15 | 4.12 | 15 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s0 | 1238 | 95 | 0.81 | 0.59 | 4.68 | 2 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s1 | 1238 | 113 | 0.93 | 0.79 | 2.58 | 5 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s2 | 1238 | 109 | 0.91 | 0.67 | 6.87 | 4 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s3 | 1238 | 103 | 1.10 | 0.83 | 5.98 | 4 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s4 | 1238 | 102 | 0.74 | 0.51 | 4.68 | 2 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp_ens | 1238 | 111 | 0.91 | 0.67 | 4.77 | 3 |
| OpenVLA-OFT | 50% | 0.05 | or_progress_ttp s0 | 1238 | 127 | 1.67 | 1.06 | 3.63 | 13 |
| OpenVLA-OFT | 50% | 0.05 | or_progress_ttp s1 | 1238 | 138 | 1.73 | 1.24 | 3.63 | 14 |
| OpenVLA-OFT | 50% | 0.05 | or_progress_ttp s2 | 1238 | 132 | 1.77 | 1.12 | 4.44 | 14 |
| OpenVLA-OFT | 50% | 0.05 | or_progress_ttp s3 | 1238 | 131 | 1.87 | 1.32 | 7.59 | 15 |
| OpenVLA-OFT | 50% | 0.05 | or_progress_ttp s4 | 1238 | 129 | 1.66 | 1.01 | 6.22 | 14 |
| OpenVLA-OFT | 50% | 0.05 | or_progress_ens | 1238 | 132 | 1.85 | 1.18 | 3.80 | 14 |
| OpenVLA-OFT | 70% (main) | 0.025 | progress | 1238 | 91 | 1.39 | 0.90 | 2.18 | 12 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s0 | 1238 | 94 | 0.73 | 0.51 | 0.65 | 1 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s1 | 1238 | 102 | 0.88 | 0.59 | 1.21 | 2 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s2 | 1238 | 99 | 0.78 | 0.57 | 1.29 | 2 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s3 | 1238 | 101 | 0.93 | 0.73 | 2.42 | 5 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s4 | 1238 | 96 | 0.60 | 0.36 | 1.29 | 1 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp_ens | 1238 | 100 | 0.85 | 0.58 | 1.21 | 2 |
| OpenVLA-OFT | 70% (main) | 0.025 | or_progress_ttp s0 | 1238 | 124 | 1.48 | 0.94 | 1.62 | 12 |
| OpenVLA-OFT | 70% (main) | 0.025 | or_progress_ttp s1 | 1238 | 132 | 1.73 | 1.04 | 2.18 | 12 |
| OpenVLA-OFT | 70% (main) | 0.025 | or_progress_ttp s2 | 1238 | 130 | 1.54 | 0.93 | 2.18 | 12 |
| OpenVLA-OFT | 70% (main) | 0.025 | or_progress_ttp s3 | 1238 | 130 | 1.76 | 1.14 | 2.83 | 12 |
| OpenVLA-OFT | 70% (main) | 0.025 | or_progress_ttp s4 | 1238 | 130 | 1.55 | 0.85 | 1.86 | 12 |
| OpenVLA-OFT | 70% (main) | 0.025 | or_progress_ens | 1238 | 129 | 1.65 | 0.92 | 2.02 | 12 |
| OpenVLA-OFT | 70% (main) | 0.05 | progress | 1238 | 114 | 1.67 | 1.15 | 4.12 | 15 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s0 | 1238 | 99 | 0.92 | 0.67 | 1.53 | 4 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s1 | 1238 | 109 | 0.90 | 0.69 | 2.50 | 4 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s2 | 1238 | 103 | 0.88 | 0.67 | 2.10 | 3 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s3 | 1238 | 107 | 1.17 | 0.89 | 4.68 | 5 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s4 | 1238 | 104 | 0.96 | 0.67 | 2.10 | 4 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp_ens | 1238 | 106 | 0.88 | 0.62 | 2.10 | 4 |
| OpenVLA-OFT | 70% (main) | 0.05 | or_progress_ttp s0 | 1238 | 134 | 1.75 | 1.15 | 2.91 | 14 |
| OpenVLA-OFT | 70% (main) | 0.05 | or_progress_ttp s1 | 1238 | 139 | 1.88 | 1.24 | 3.63 | 15 |
| OpenVLA-OFT | 70% (main) | 0.05 | or_progress_ttp s2 | 1238 | 136 | 1.80 | 1.18 | 3.47 | 14 |
| OpenVLA-OFT | 70% (main) | 0.05 | or_progress_ttp s3 | 1238 | 134 | 2.03 | 1.47 | 5.41 | 15 |
| OpenVLA-OFT | 70% (main) | 0.05 | or_progress_ttp s4 | 1238 | 137 | 1.86 | 1.18 | 3.47 | 14 |
| OpenVLA-OFT | 70% (main) | 0.05 | or_progress_ens | 1238 | 138 | 1.88 | 1.24 | 3.31 | 14 |
| OpenVLA-OFT | 80% | 0.025 | progress | 1238 | 91 | 1.39 | 0.90 | 2.18 | 12 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s0 | 1238 | 90 | 0.74 | 0.58 | 1.05 | 3 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s1 | 1238 | 102 | 0.94 | 0.63 | 1.21 | 4 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s2 | 1238 | 96 | 0.80 | 0.55 | 1.21 | 3 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s3 | 1238 | 101 | 0.75 | 0.53 | 2.67 | 4 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s4 | 1238 | 94 | 0.80 | 0.55 | 2.10 | 4 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp_ens | 1238 | 98 | 0.84 | 0.59 | 1.62 | 4 |
| OpenVLA-OFT | 80% | 0.025 | or_progress_ttp s0 | 1238 | 124 | 1.55 | 1.06 | 1.62 | 13 |
| OpenVLA-OFT | 80% | 0.025 | or_progress_ttp s1 | 1238 | 132 | 1.79 | 1.20 | 1.86 | 13 |
| OpenVLA-OFT | 80% | 0.025 | or_progress_ttp s2 | 1238 | 128 | 1.60 | 0.94 | 2.10 | 13 |
| OpenVLA-OFT | 80% | 0.025 | or_progress_ttp s3 | 1238 | 131 | 1.58 | 1.01 | 2.58 | 13 |
| OpenVLA-OFT | 80% | 0.025 | or_progress_ttp s4 | 1238 | 130 | 1.59 | 1.08 | 1.86 | 13 |
| OpenVLA-OFT | 80% | 0.025 | or_progress_ens | 1238 | 132 | 1.69 | 1.14 | 1.94 | 13 |
| OpenVLA-OFT | 80% | 0.05 | progress | 1238 | 114 | 1.67 | 1.15 | 4.12 | 15 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s0 | 1238 | 104 | 0.80 | 0.54 | 2.18 | 3 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s1 | 1238 | 109 | 1.02 | 0.82 | 1.86 | 5 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s2 | 1238 | 106 | 1.00 | 0.75 | 1.94 | 4 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s3 | 1238 | 105 | 0.88 | 0.67 | 5.17 | 4 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s4 | 1238 | 104 | 1.04 | 0.85 | 2.67 | 4 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp_ens | 1238 | 109 | 0.86 | 0.68 | 2.10 | 5 |
| OpenVLA-OFT | 80% | 0.05 | or_progress_ttp s0 | 1238 | 135 | 1.79 | 1.22 | 3.31 | 15 |
| OpenVLA-OFT | 80% | 0.05 | or_progress_ttp s1 | 1238 | 137 | 1.87 | 1.22 | 3.55 | 15 |
| OpenVLA-OFT | 80% | 0.05 | or_progress_ttp s2 | 1238 | 136 | 1.86 | 1.16 | 3.07 | 15 |
| OpenVLA-OFT | 80% | 0.05 | or_progress_ttp s3 | 1238 | 136 | 1.82 | 1.22 | 4.60 | 15 |
| OpenVLA-OFT | 80% | 0.05 | or_progress_ttp s4 | 1238 | 135 | 1.88 | 1.24 | 4.28 | 15 |
| OpenVLA-OFT | 80% | 0.05 | or_progress_ens | 1238 | 136 | 1.88 | 1.28 | 3.88 | 15 |
| Pi0.5 | 50% | 0.025 | progress | 972 | 34 | 0.28 | 0.21 | 2.37 | 3 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s0 | 972 | 17 | 0.41 | 0.33 | 0.51 | 1 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s1 | 972 | 16 | 0.49 | 0.44 | 1.44 | 0 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s2 | 972 | 9 | 0.23 | 0.18 | 0.41 | 0 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s3 | 972 | 6 | 0.08 | 0.05 | 0.41 | 1 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s4 | 972 | 9 | 0.21 | 0.13 | 0.00 | 0 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp_ens | 972 | 10 | 0.18 | 0.18 | 0.00 | 0 |
| Pi0.5 | 50% | 0.025 | or_progress_ttp s0 | 972 | 36 | 0.69 | 0.41 | 1.65 | 3 |
| Pi0.5 | 50% | 0.025 | or_progress_ttp s1 | 972 | 35 | 0.59 | 0.31 | 2.26 | 2 |
| Pi0.5 | 50% | 0.025 | or_progress_ttp s2 | 972 | 33 | 0.62 | 0.31 | 1.44 | 2 |
| Pi0.5 | 50% | 0.025 | or_progress_ttp s3 | 972 | 32 | 0.46 | 0.18 | 1.23 | 3 |
| Pi0.5 | 50% | 0.025 | or_progress_ttp s4 | 972 | 33 | 0.59 | 0.26 | 1.23 | 2 |
| Pi0.5 | 50% | 0.025 | or_progress_ens | 972 | 33 | 0.59 | 0.26 | 1.34 | 2 |
| Pi0.5 | 50% | 0.05 | progress | 972 | 37 | 0.44 | 0.31 | 4.73 | 3 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s0 | 972 | 17 | 0.49 | 0.36 | 0.82 | 1 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s1 | 972 | 17 | 0.51 | 0.49 | 1.75 | 0 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s2 | 972 | 9 | 0.21 | 0.15 | 0.62 | 0 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s3 | 972 | 7 | 0.10 | 0.10 | 0.82 | 1 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s4 | 972 | 12 | 0.28 | 0.23 | 0.51 | 0 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp_ens | 972 | 13 | 0.28 | 0.23 | 0.62 | 1 |
| Pi0.5 | 50% | 0.05 | or_progress_ttp s0 | 972 | 38 | 0.87 | 0.51 | 2.78 | 4 |
| Pi0.5 | 50% | 0.05 | or_progress_ttp s1 | 972 | 38 | 0.98 | 0.64 | 3.70 | 3 |
| Pi0.5 | 50% | 0.05 | or_progress_ttp s2 | 972 | 36 | 0.64 | 0.36 | 2.67 | 3 |
| Pi0.5 | 50% | 0.05 | or_progress_ttp s3 | 972 | 36 | 0.49 | 0.23 | 2.67 | 4 |
| Pi0.5 | 50% | 0.05 | or_progress_ttp s4 | 972 | 36 | 0.62 | 0.31 | 2.47 | 3 |
| Pi0.5 | 50% | 0.05 | or_progress_ens | 972 | 37 | 0.72 | 0.33 | 2.57 | 3 |
| Pi0.5 | 70% (main) | 0.025 | progress | 972 | 34 | 0.28 | 0.21 | 2.37 | 3 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s0 | 972 | 14 | 0.33 | 0.33 | 0.72 | 0 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s1 | 972 | 16 | 0.46 | 0.39 | 1.23 | 1 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s2 | 972 | 4 | 0.15 | 0.10 | 0.62 | 0 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s3 | 972 | 5 | 0.03 | 0.03 | 0.31 | 1 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s4 | 972 | 7 | 0.10 | 0.10 | 0.31 | 0 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp_ens | 972 | 9 | 0.23 | 0.23 | 0.31 | 0 |
| Pi0.5 | 70% (main) | 0.025 | or_progress_ttp s0 | 972 | 35 | 0.69 | 0.46 | 1.65 | 2 |
| Pi0.5 | 70% (main) | 0.025 | or_progress_ttp s1 | 972 | 37 | 0.80 | 0.51 | 2.26 | 3 |
| Pi0.5 | 70% (main) | 0.025 | or_progress_ttp s2 | 972 | 32 | 0.51 | 0.15 | 1.54 | 2 |
| Pi0.5 | 70% (main) | 0.025 | or_progress_ttp s3 | 972 | 31 | 0.41 | 0.13 | 1.23 | 3 |
| Pi0.5 | 70% (main) | 0.025 | or_progress_ttp s4 | 972 | 32 | 0.51 | 0.23 | 1.44 | 2 |
| Pi0.5 | 70% (main) | 0.025 | or_progress_ens | 972 | 32 | 0.49 | 0.26 | 1.34 | 2 |
| Pi0.5 | 70% (main) | 0.05 | progress | 972 | 37 | 0.44 | 0.31 | 4.73 | 3 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s0 | 972 | 15 | 0.54 | 0.36 | 1.34 | 0 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s1 | 972 | 16 | 0.44 | 0.44 | 1.65 | 1 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s2 | 972 | 6 | 0.26 | 0.23 | 0.72 | 0 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s3 | 972 | 7 | 0.15 | 0.03 | 0.51 | 1 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s4 | 972 | 11 | 0.26 | 0.26 | 0.72 | 0 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp_ens | 972 | 13 | 0.33 | 0.21 | 0.62 | 0 |
| Pi0.5 | 70% (main) | 0.05 | or_progress_ttp s0 | 972 | 38 | 0.77 | 0.49 | 3.09 | 3 |
| Pi0.5 | 70% (main) | 0.05 | or_progress_ttp s1 | 972 | 38 | 0.93 | 0.57 | 3.19 | 4 |
| Pi0.5 | 70% (main) | 0.05 | or_progress_ttp s2 | 972 | 37 | 0.67 | 0.28 | 3.09 | 3 |
| Pi0.5 | 70% (main) | 0.05 | or_progress_ttp s3 | 972 | 36 | 0.44 | 0.21 | 2.67 | 4 |
| Pi0.5 | 70% (main) | 0.05 | or_progress_ttp s4 | 972 | 36 | 0.51 | 0.28 | 2.78 | 3 |
| Pi0.5 | 70% (main) | 0.05 | or_progress_ens | 972 | 38 | 0.80 | 0.46 | 2.67 | 3 |
| Pi0.5 | 80% | 0.025 | progress | 972 | 34 | 0.28 | 0.21 | 2.37 | 3 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s0 | 972 | 9 | 0.23 | 0.21 | 0.21 | 0 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s1 | 972 | 3 | 0.08 | 0.08 | 0.51 | 0 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s2 | 972 | 8 | 0.21 | 0.13 | 0.21 | 0 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s3 | 972 | 2 | 0.08 | 0.00 | 0.21 | 0 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s4 | 972 | 4 | 0.08 | 0.08 | 0.00 | 0 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp_ens | 972 | 4 | 0.13 | 0.10 | 0.21 | 0 |
| Pi0.5 | 80% | 0.025 | or_progress_ttp s0 | 972 | 35 | 0.64 | 0.36 | 1.34 | 2 |
| Pi0.5 | 80% | 0.025 | or_progress_ttp s1 | 972 | 31 | 0.41 | 0.10 | 1.34 | 2 |
| Pi0.5 | 80% | 0.025 | or_progress_ttp s2 | 972 | 33 | 0.49 | 0.26 | 1.44 | 2 |
| Pi0.5 | 80% | 0.025 | or_progress_ttp s3 | 972 | 31 | 0.41 | 0.13 | 1.34 | 2 |
| Pi0.5 | 80% | 0.025 | or_progress_ttp s4 | 972 | 31 | 0.44 | 0.15 | 1.23 | 2 |
| Pi0.5 | 80% | 0.025 | or_progress_ens | 972 | 32 | 0.51 | 0.21 | 1.34 | 2 |
| Pi0.5 | 80% | 0.05 | progress | 972 | 37 | 0.44 | 0.31 | 4.73 | 3 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s0 | 972 | 10 | 0.31 | 0.31 | 0.51 | 0 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s1 | 972 | 4 | 0.05 | 0.03 | 1.34 | 0 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s2 | 972 | 9 | 0.23 | 0.23 | 0.41 | 0 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s3 | 972 | 2 | 0.08 | 0.08 | 0.62 | 0 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s4 | 972 | 5 | 0.10 | 0.10 | 0.21 | 0 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp_ens | 972 | 6 | 0.15 | 0.10 | 0.31 | 0 |
| Pi0.5 | 80% | 0.05 | or_progress_ttp s0 | 972 | 38 | 0.77 | 0.49 | 2.57 | 3 |
| Pi0.5 | 80% | 0.05 | or_progress_ttp s1 | 972 | 35 | 0.49 | 0.26 | 2.78 | 3 |
| Pi0.5 | 80% | 0.05 | or_progress_ttp s2 | 972 | 36 | 0.62 | 0.39 | 2.47 | 3 |
| Pi0.5 | 80% | 0.05 | or_progress_ttp s3 | 972 | 35 | 0.49 | 0.26 | 2.57 | 3 |
| Pi0.5 | 80% | 0.05 | or_progress_ttp s4 | 972 | 35 | 0.49 | 0.26 | 2.37 | 3 |
| Pi0.5 | 80% | 0.05 | or_progress_ens | 972 | 35 | 0.54 | 0.36 | 2.47 | 3 |
