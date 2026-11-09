# Timely vs realized false alarms, every method, 70% rule, unseen tasks

One curve per policy, every method (Fahad, Nov 7, item 4), 70% rule, unseen tasks: timely alarms (at or before t_pnr, failures with t_pnr > 0) against the realized false-alarm rate on held-out successes, 0 to 10%. Thresholds are swept on the held-out successes, pooled over folds, so this is descriptive, not a deployable rule. Methods: progress, SAFE-style and Hide-and-Seek-style (06, data/base70), FailureSpot (mlp, lstm) and its action probe (Pi0.5) from results/*/failurespot/loto, the gru_phys_ttp seed ensemble, and progress OR the ensemble (common level q for both parts on the held-out successes, best q at each rate). FailureSpot scores were trained on 50% labels; they are scored here against the 70% t_pnr. Evaluation set: the held-out episodes of our 70% runs that each method scored.

| policy | method | timed failures | timely at <= 1.0% (realized) | timely at <= 2.5% (realized) | timely at <= 5.0% (realized) | timely at <= 10.0% (realized) |
|---|---|---|---|---|---|---|
| OpenVLA-OFT | progress | 91 | 13 (0.007) | 15 (0.024) | 24 (0.047) | 34 (0.092) |
| OpenVLA-OFT | safe | 91 | 10 (0.009) | 20 (0.024) | 25 (0.049) | 32 (0.100) |
| OpenVLA-OFT | hideseek | 91 | 15 (0.009) | 18 (0.024) | 19 (0.049) | 22 (0.100) |
| OpenVLA-OFT | failurespot_mlp | 91 | 0 (0.009) | 2 (0.024) | 5 (0.049) | 14 (0.100) |
| OpenVLA-OFT | failurespot_lstm | 91 | 3 (0.009) | 4 (0.024) | 11 (0.049) | 24 (0.100) |
| OpenVLA-OFT | gru_phys_ttp_ens | 91 | 14 (0.009) | 26 (0.024) | 32 (0.049) | 38 (0.100) |
| OpenVLA-OFT | or_progress_ens | 91 | 14 (0.009) | 27 (0.022) | 35 (0.046) | 42 (0.092) |
| Pi0.5 | progress | 31 | 3 (0.008) | 6 (0.023) | 8 (0.046) | 13 (0.077) |
| Pi0.5 | safe | 31 | 1 (0.010) | 3 (0.025) | 4 (0.050) | 9 (0.099) |
| Pi0.5 | hideseek | 31 | 4 (0.010) | 5 (0.025) | 6 (0.050) | 6 (0.099) |
| Pi0.5 | failurespot_mlp | 31 | 0 (0.010) | 0 (0.025) | 1 (0.050) | 2 (0.099) |
| Pi0.5 | failurespot_lstm | 31 | 1 (0.010) | 1 (0.025) | 2 (0.050) | 3 (0.099) |
| Pi0.5 | actprobe_mlp | 31 | 3 (0.010) | 5 (0.025) | 11 (0.050) | 15 (0.099) |
| Pi0.5 | actprobe_lstm | 31 | 6 (0.010) | 9 (0.025) | 14 (0.050) | 16 (0.099) |
| Pi0.5 | gru_phys_ttp_ens | 31 | 9 (0.010) | 10 (0.025) | 10 (0.050) | 12 (0.099) |
| Pi0.5 | or_progress_ens | 31 | 11 (0.008) | 12 (0.020) | 13 (0.045) | 13 (0.045) |
