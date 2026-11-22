# Pure regression of the point of no return score, seed 0 (plan: results/plan_nov13.md)

Target = replay failure fraction at each query; MSE only, every episode weighted equally; leave one task out (10 held-out tasks, pooled over points). (i) scanned checkpoints of failed runs, (ii) successes (target 0 unless scanned), (iii) all known points. Spearman on failed runs: pooled over points / median per episode (episodes with a non-constant target). Floor = binomial noise of the retries (K 4, or 16 where refined); it is the error a perfect predictor of the true failure probability would still have. Seeds 1 to 4 of every learned model are in seeds.md; nothing was picked on test results.

INTERIM SMOOTHING, NOT THE 20-REPLAY GROUND TRUTH (results/plan_nov22_gt20.md, Step 4): target and floor here use the pooled failure fraction = failed / all replays over the scan checkpoints k-1, k, k+1 (about 12 replays, or more where refined), on the same episodes, exclusions, t_pnr values and models as results/regression_v2. The floor treats the pooled count as binomial, so it is approximate. Compare with results/regression_v2/main.md (raw K 4 target).

## OpenVLA-OFT

Kept: 1207 episodes (136 failures, 1071 successes), 43218 known points. Excluded failures: 16 recoverable by pre-check, 15 scanned and recoverable (50% rule), 0 unscanned (no target). Hidden states present in every kept episode.

| model | MSE (i) fail | MAE (i) | MSE (ii) succ | MAE (ii) | MSE (iii) all | MAE (iii) | Spearman fail pooled | per episode (n) |
|---|---|---|---|---|---|---|---|---|
| gru_phys_frac | 0.2328 | 0.3526 | 0.0189 | 0.0693 | 0.0627 | 0.1272 | 0.5135 | 0.5807 (110) |
| safe_lin | 0.1401 | 0.2226 | 0.2107 | 0.3225 | 0.1963 | 0.3020 | 0.4190 | 0.5058 (110) |
| safe_mlp | 0.2348 | 0.3604 | 0.1161 | 0.1840 | 0.1404 | 0.2201 | 0.3543 | 0.4742 (110) |
| safe_lstm | 0.2917 | 0.3900 | 0.1020 | 0.1559 | 0.1408 | 0.2038 | 0.3496 | 0.4628 (110) |
| gru_physvla_frac | 0.1781 | 0.2854 | 0.0652 | 0.1348 | 0.0883 | 0.1656 | 0.5401 | 0.6084 (110) |
| const | 0.6550 | 0.7703 | 0.0092 | 0.0953 | 0.1413 | 0.2334 | -0.1413 | n/a (0) |
| progress_iso | 0.5039 | 0.6367 | 0.0126 | 0.0797 | 0.1131 | 0.1936 | 0.0816 | 0.2889 (110) |
| timer_iso | 0.3877 | 0.5258 | 0.0230 | 0.0791 | 0.0976 | 0.1704 | 0.3948 | 0.7441 (110) |
| noise floor | 0.0050 | 0.0292 | 0.0000 | 0.0003 | 0.0011 | 0.0062 |  |  |

Points: (i) 8840, (ii) 34378, (iii) 43218. timer_iso is a check (policy step mapped by isotonic regression), not a candidate.

## Pi0.5

Kept: 965 episodes (37 failures, 928 successes), 31837 known points. Excluded failures: 4 recoverable by pre-check, 3 scanned and recoverable (50% rule), 16 unscanned (no target). Hidden states present in every kept episode.

| model | MSE (i) fail | MAE (i) | MSE (ii) succ | MAE (ii) | MSE (iii) all | MAE (iii) | Spearman fail pooled | per episode (n) |
|---|---|---|---|---|---|---|---|---|
| gru_phys_frac | 0.3882 | 0.5197 | 0.0131 | 0.0521 | 0.0414 | 0.0874 | 0.2343 | 0.3485 (34) |
| safe_lin | 0.1992 | 0.3416 | 0.2135 | 0.3487 | 0.2124 | 0.3481 | 0.2725 | 0.4250 (34) |
| safe_mlp | 0.4788 | 0.6147 | 0.0051 | 0.0402 | 0.0409 | 0.0836 | 0.3180 | 0.4497 (34) |
| safe_lstm | 0.5904 | 0.6848 | 0.0124 | 0.0440 | 0.0561 | 0.0924 | 0.0786 | -0.0242 (34) |
| gru_physvla_frac | 0.4094 | 0.5208 | 0.0257 | 0.0687 | 0.0547 | 0.1028 | 0.1487 | 0.2751 (34) |
| const | 0.6799 | 0.7666 | 0.0009 | 0.0295 | 0.0522 | 0.0852 | 0.0092 | n/a (0) |
| progress_iso | 0.4265 | 0.5623 | 0.0042 | 0.0237 | 0.0361 | 0.0644 | 0.3736 | 0.3746 (34) |
| timer_iso | 0.4315 | 0.5697 | 0.0068 | 0.0289 | 0.0389 | 0.0697 | 0.4457 | 0.6689 (34) |
| noise floor | 0.0066 | 0.0377 | 0.0000 | 0.0000 | 0.0005 | 0.0028 |  |  |

Points: (i) 2405, (ii) 29432, (iii) 31837. timer_iso is a check (policy step mapped by isotonic regression), not a candidate.

