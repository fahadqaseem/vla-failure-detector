# Breakdowns, unseen tasks

Breakdowns (Fahad, Nov 7, item 9), unseen tasks, both policies, all rules (70% main): (1) natural episodes only (timely of natural failures with t_pnr > 0, false alarms on natural successes); (2) lead-time curve: failures caught at least L = 0, 16, 32, 64 steps before t_pnr; (3) histogram of alarm steps of the timely catches (70%, both budgets), lead_time.png and alarm_steps.png.

## Natural episodes only

| policy | rule | budget | model | natural timely | natural false alarms |
|---|---|---|---|---|---|
| OpenVLA-OFT | 50% | 0.025 | progress | 5 of 11 | 14 of 472 (0.030) |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s0 | 3 of 11 | 2 of 472 (0.004) |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp_ens | 4 of 11 | 5 of 472 (0.011) |
| OpenVLA-OFT | 50% | 0.025 | or_progress_ttp s0 | 5 of 11 | 9 of 472 (0.019) |
| OpenVLA-OFT | 50% | 0.025 | or_progress_ens | 6 of 11 | 8 of 472 (0.017) |
| OpenVLA-OFT | 50% | 0.05 | progress | 6 of 11 | 23 of 472 (0.049) |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s0 | 4 of 11 | 51 of 472 (0.108) |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp_ens | 4 of 11 | 38 of 472 (0.081) |
| OpenVLA-OFT | 50% | 0.05 | or_progress_ttp s0 | 5 of 11 | 26 of 472 (0.055) |
| OpenVLA-OFT | 50% | 0.05 | or_progress_ens | 6 of 11 | 22 of 472 (0.047) |
| OpenVLA-OFT | 70% (main) | 0.025 | progress | 3 of 10 | 14 of 472 (0.030) |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s0 | 2 of 10 | 0 of 472 (0.000) |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp_ens | 2 of 10 | 1 of 472 (0.002) |
| OpenVLA-OFT | 70% (main) | 0.025 | or_progress_ttp s0 | 4 of 10 | 11 of 472 (0.023) |
| OpenVLA-OFT | 70% (main) | 0.025 | or_progress_ens | 4 of 10 | 11 of 472 (0.023) |
| OpenVLA-OFT | 70% (main) | 0.05 | progress | 4 of 10 | 23 of 472 (0.049) |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s0 | 3 of 10 | 3 of 472 (0.006) |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp_ens | 3 of 10 | 4 of 472 (0.008) |
| OpenVLA-OFT | 70% (main) | 0.05 | or_progress_ttp s0 | 4 of 10 | 16 of 472 (0.034) |
| OpenVLA-OFT | 70% (main) | 0.05 | or_progress_ens | 4 of 10 | 16 of 472 (0.034) |
| OpenVLA-OFT | 80% | 0.025 | progress | 2 of 8 | 14 of 472 (0.030) |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s0 | 0 of 8 | 1 of 472 (0.002) |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp_ens | 0 of 8 | 3 of 472 (0.006) |
| OpenVLA-OFT | 80% | 0.025 | or_progress_ttp s0 | 1 of 8 | 10 of 472 (0.021) |
| OpenVLA-OFT | 80% | 0.025 | or_progress_ens | 1 of 8 | 11 of 472 (0.023) |
| OpenVLA-OFT | 80% | 0.05 | progress | 3 of 8 | 23 of 472 (0.049) |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s0 | 0 of 8 | 3 of 472 (0.006) |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp_ens | 1 of 8 | 3 of 472 (0.006) |
| OpenVLA-OFT | 80% | 0.05 | or_progress_ttp s0 | 2 of 8 | 15 of 472 (0.032) |
| OpenVLA-OFT | 80% | 0.05 | or_progress_ens | 2 of 8 | 18 of 472 (0.038) |
| Pi0.5 | 50% | 0.025 | progress | 0 of 5 | 10 of 475 (0.021) |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s0 | 1 of 5 | 2 of 475 (0.004) |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp_ens | 1 of 5 | 0 of 475 (0.000) |
| Pi0.5 | 50% | 0.025 | or_progress_ttp s0 | 1 of 5 | 6 of 475 (0.013) |
| Pi0.5 | 50% | 0.025 | or_progress_ens | 1 of 5 | 5 of 475 (0.011) |
| Pi0.5 | 50% | 0.05 | progress | 1 of 5 | 19 of 475 (0.040) |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s0 | 1 of 5 | 3 of 475 (0.006) |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp_ens | 1 of 5 | 1 of 475 (0.002) |
| Pi0.5 | 50% | 0.05 | or_progress_ttp s0 | 1 of 5 | 12 of 475 (0.025) |
| Pi0.5 | 50% | 0.05 | or_progress_ens | 1 of 5 | 10 of 475 (0.021) |
| Pi0.5 | 70% (main) | 0.025 | progress | 2 of 5 | 10 of 475 (0.021) |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s0 | 2 of 5 | 2 of 475 (0.004) |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp_ens | 1 of 5 | 0 of 475 (0.000) |
| Pi0.5 | 70% (main) | 0.025 | or_progress_ttp s0 | 3 of 5 | 6 of 475 (0.013) |
| Pi0.5 | 70% (main) | 0.025 | or_progress_ens | 2 of 5 | 5 of 475 (0.011) |
| Pi0.5 | 70% (main) | 0.05 | progress | 2 of 5 | 19 of 475 (0.040) |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s0 | 2 of 5 | 4 of 475 (0.008) |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp_ens | 1 of 5 | 1 of 475 (0.002) |
| Pi0.5 | 70% (main) | 0.05 | or_progress_ttp s0 | 3 of 5 | 12 of 475 (0.025) |
| Pi0.5 | 70% (main) | 0.05 | or_progress_ens | 2 of 5 | 10 of 475 (0.021) |
| Pi0.5 | 80% | 0.025 | progress | 3 of 5 | 10 of 475 (0.021) |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s0 | 1 of 5 | 1 of 475 (0.002) |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp_ens | 1 of 5 | 0 of 475 (0.000) |
| Pi0.5 | 80% | 0.025 | or_progress_ttp s0 | 3 of 5 | 6 of 475 (0.013) |
| Pi0.5 | 80% | 0.025 | or_progress_ens | 3 of 5 | 5 of 475 (0.011) |
| Pi0.5 | 80% | 0.05 | progress | 3 of 5 | 19 of 475 (0.040) |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s0 | 2 of 5 | 1 of 475 (0.002) |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp_ens | 1 of 5 | 0 of 475 (0.000) |
| Pi0.5 | 80% | 0.05 | or_progress_ttp s0 | 3 of 5 | 11 of 475 (0.023) |
| Pi0.5 | 80% | 0.05 | or_progress_ens | 3 of 5 | 10 of 475 (0.021) |

## Lead time (failures with t_pnr > 0 caught at least L steps before t_pnr)

| policy | rule | budget | model | timed failures | lead >= 0 | lead >= 16 | lead >= 32 | lead >= 64 |
|---|---|---|---|---|---|---|---|---|
| OpenVLA-OFT | 50% | 0.025 | progress | 81 | 11 | 11 | 10 | 8 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp s0 | 81 | 10 | 9 | 7 | 6 |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp_ens | 81 | 15 | 14 | 13 | 9 |
| OpenVLA-OFT | 50% | 0.025 | or_progress_ttp s0 | 81 | 13 | 12 | 10 | 7 |
| OpenVLA-OFT | 50% | 0.025 | or_progress_ens | 81 | 14 | 13 | 12 | 8 |
| OpenVLA-OFT | 50% | 0.05 | progress | 81 | 17 | 15 | 14 | 13 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp s0 | 81 | 11 | 10 | 9 | 6 |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp_ens | 81 | 16 | 16 | 15 | 10 |
| OpenVLA-OFT | 50% | 0.05 | or_progress_ttp s0 | 81 | 16 | 15 | 14 | 10 |
| OpenVLA-OFT | 50% | 0.05 | or_progress_ens | 81 | 21 | 20 | 18 | 13 |
| OpenVLA-OFT | 70% (main) | 0.025 | progress | 91 | 13 | 13 | 13 | 13 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp s0 | 91 | 16 | 14 | 13 | 13 |
| OpenVLA-OFT | 70% (main) | 0.025 | gru_phys_ttp_ens | 91 | 20 | 17 | 17 | 16 |
| OpenVLA-OFT | 70% (main) | 0.025 | or_progress_ttp s0 | 91 | 21 | 21 | 20 | 14 |
| OpenVLA-OFT | 70% (main) | 0.025 | or_progress_ens | 91 | 23 | 22 | 21 | 17 |
| OpenVLA-OFT | 70% (main) | 0.05 | progress | 91 | 22 | 22 | 17 | 16 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp s0 | 91 | 22 | 22 | 20 | 18 |
| OpenVLA-OFT | 70% (main) | 0.05 | gru_phys_ttp_ens | 91 | 24 | 24 | 21 | 20 |
| OpenVLA-OFT | 70% (main) | 0.05 | or_progress_ttp s0 | 91 | 26 | 23 | 22 | 22 |
| OpenVLA-OFT | 70% (main) | 0.05 | or_progress_ens | 91 | 29 | 28 | 26 | 25 |
| OpenVLA-OFT | 80% | 0.025 | progress | 102 | 17 | 16 | 16 | 14 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp s0 | 102 | 20 | 19 | 18 | 15 |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp_ens | 102 | 24 | 23 | 21 | 17 |
| OpenVLA-OFT | 80% | 0.025 | or_progress_ttp s0 | 102 | 24 | 24 | 22 | 19 |
| OpenVLA-OFT | 80% | 0.025 | or_progress_ens | 102 | 26 | 26 | 25 | 21 |
| OpenVLA-OFT | 80% | 0.05 | progress | 102 | 29 | 25 | 21 | 20 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp s0 | 102 | 24 | 23 | 21 | 19 |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp_ens | 102 | 28 | 27 | 26 | 21 |
| OpenVLA-OFT | 80% | 0.05 | or_progress_ttp s0 | 102 | 31 | 31 | 28 | 24 |
| OpenVLA-OFT | 80% | 0.05 | or_progress_ens | 102 | 35 | 33 | 31 | 25 |
| Pi0.5 | 50% | 0.025 | progress | 27 | 2 | 2 | 2 | 2 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp s0 | 27 | 8 | 8 | 8 | 8 |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp_ens | 27 | 5 | 5 | 5 | 5 |
| Pi0.5 | 50% | 0.025 | or_progress_ttp s0 | 27 | 9 | 9 | 9 | 9 |
| Pi0.5 | 50% | 0.025 | or_progress_ens | 27 | 5 | 5 | 5 | 5 |
| Pi0.5 | 50% | 0.05 | progress | 27 | 5 | 5 | 4 | 4 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp s0 | 27 | 9 | 8 | 8 | 8 |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp_ens | 27 | 6 | 6 | 6 | 6 |
| Pi0.5 | 50% | 0.05 | or_progress_ttp s0 | 27 | 9 | 9 | 9 | 9 |
| Pi0.5 | 50% | 0.05 | or_progress_ens | 27 | 7 | 6 | 6 | 6 |
| Pi0.5 | 70% (main) | 0.025 | progress | 31 | 6 | 6 | 6 | 5 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp s0 | 31 | 9 | 8 | 8 | 7 |
| Pi0.5 | 70% (main) | 0.025 | gru_phys_ttp_ens | 31 | 5 | 5 | 5 | 5 |
| Pi0.5 | 70% (main) | 0.025 | or_progress_ttp s0 | 31 | 12 | 10 | 10 | 10 |
| Pi0.5 | 70% (main) | 0.025 | or_progress_ens | 31 | 8 | 7 | 7 | 7 |
| Pi0.5 | 70% (main) | 0.05 | progress | 31 | 8 | 8 | 8 | 8 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp s0 | 31 | 10 | 9 | 9 | 8 |
| Pi0.5 | 70% (main) | 0.05 | gru_phys_ttp_ens | 31 | 6 | 6 | 6 | 6 |
| Pi0.5 | 70% (main) | 0.05 | or_progress_ttp s0 | 31 | 12 | 11 | 11 | 11 |
| Pi0.5 | 70% (main) | 0.05 | or_progress_ens | 31 | 10 | 10 | 10 | 10 |
| Pi0.5 | 80% | 0.025 | progress | 33 | 12 | 12 | 12 | 9 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp s0 | 33 | 6 | 6 | 6 | 5 |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp_ens | 33 | 3 | 3 | 2 | 2 |
| Pi0.5 | 80% | 0.025 | or_progress_ttp s0 | 33 | 12 | 11 | 11 | 10 |
| Pi0.5 | 80% | 0.025 | or_progress_ens | 33 | 10 | 9 | 9 | 7 |
| Pi0.5 | 80% | 0.05 | progress | 33 | 17 | 16 | 15 | 14 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp s0 | 33 | 7 | 7 | 7 | 7 |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp_ens | 33 | 5 | 5 | 4 | 4 |
| Pi0.5 | 80% | 0.05 | or_progress_ttp s0 | 33 | 15 | 15 | 15 | 13 |
| Pi0.5 | 80% | 0.05 | or_progress_ens | 33 | 12 | 12 | 12 | 10 |
