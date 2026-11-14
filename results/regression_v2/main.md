# Pure regression of the point of no return score, seed 0 (plan: results/plan_nov13.md)

Target = replay failure fraction at each query; MSE only, every episode weighted equally; leave one task out (10 held-out tasks, pooled over points). (i) scanned checkpoints of failed runs, (ii) successes (target 0 unless scanned), (iii) all known points. Spearman on failed runs: pooled over points / median per episode (episodes with a non-constant target). Floor = binomial noise of the retries (K 4, or 16 where refined); it is the error a perfect predictor of the true failure probability would still have. Seeds 1 to 4 of every learned model are in seeds.md; nothing was picked on test results.

## OpenVLA-OFT

Kept: 1207 episodes (136 failures, 1071 successes), 43218 known points. Excluded failures: 16 recoverable by pre-check, 15 scanned and recoverable (50% rule), 0 unscanned (no target). Hidden states present in every kept episode.

| model | MSE (i) fail | MAE (i) | MSE (ii) succ | MAE (ii) | MSE (iii) all | MAE (iii) | Spearman fail pooled | per episode (n) |
|---|---|---|---|---|---|---|---|---|
| gru_phys_frac | 0.2436 | 0.3586 | 0.0191 | 0.0695 | 0.0650 | 0.1286 | 0.4650 | 0.4792 (110) |
| safe_lin | 0.1499 | 0.2285 | 0.2109 | 0.3227 | 0.1984 | 0.3034 | 0.3983 | 0.4274 (110) |
| safe_mlp | 0.2775 | 0.3879 | 0.0375 | 0.0872 | 0.0866 | 0.1487 | 0.3507 | 0.3717 (110) |
| safe_lstm | 0.3145 | 0.4071 | 0.1074 | 0.1616 | 0.1498 | 0.2118 | 0.3064 | 0.3940 (110) |
| gru_physvla_frac | 0.1887 | 0.2912 | 0.0648 | 0.1342 | 0.0902 | 0.1663 | 0.4932 | 0.4922 (110) |
| const | 0.6663 | 0.7753 | 0.0093 | 0.0957 | 0.1437 | 0.2347 | -0.1235 | n/a (0) |
| progress_iso | 0.5151 | 0.6420 | 0.0127 | 0.0800 | 0.1155 | 0.1949 | 0.0787 | 0.2384 (110) |
| timer_iso | 0.3987 | 0.5302 | 0.0231 | 0.0793 | 0.0999 | 0.1715 | 0.3636 | 0.6265 (110) |
| noise floor | 0.0150 | 0.0371 | 0.0001 | 0.0003 | 0.0032 | 0.0078 |  |  |

Points: (i) 8840, (ii) 34378, (iii) 43218. timer_iso is a check (policy step mapped by isotonic regression), not a candidate.

## Pi0.5

Kept: 965 episodes (37 failures, 928 successes), 31837 known points. Excluded failures: 4 recoverable by pre-check, 3 scanned and recoverable (50% rule), 16 unscanned (no target). Hidden states present in every kept episode.

| model | MSE (i) fail | MAE (i) | MSE (ii) succ | MAE (ii) | MSE (iii) all | MAE (iii) | Spearman fail pooled | per episode (n) |
|---|---|---|---|---|---|---|---|---|
| gru_phys_frac | 0.4022 | 0.5297 | 0.0131 | 0.0522 | 0.0425 | 0.0883 | 0.2315 | 0.3535 (34) |
| safe_lin | 0.2130 | 0.3537 | 0.2134 | 0.3486 | 0.2134 | 0.3490 | 0.2653 | 0.3455 (34) |
| safe_mlp | 0.4918 | 0.6192 | 0.0051 | 0.0402 | 0.0419 | 0.0839 | 0.2996 | 0.4078 (34) |
| safe_lstm | 0.6311 | 0.7140 | 0.0093 | 0.0384 | 0.0563 | 0.0895 | -0.0388 | -0.0999 (34) |
| gru_physvla_frac | 0.4234 | 0.5300 | 0.0257 | 0.0687 | 0.0558 | 0.1036 | 0.1407 | 0.1966 (34) |
| const | 0.6944 | 0.7695 | 0.0009 | 0.0295 | 0.0533 | 0.0854 | -0.0188 | n/a (0) |
| progress_iso | 0.4413 | 0.5660 | 0.0042 | 0.0237 | 0.0372 | 0.0647 | 0.3527 | 0.3177 (34) |
| timer_iso | 0.4458 | 0.5737 | 0.0068 | 0.0289 | 0.0399 | 0.0700 | 0.4265 | 0.6008 (34) |
| noise floor | 0.0189 | 0.0461 | 0.0000 | 0.0000 | 0.0014 | 0.0035 |  |  |

Points: (i) 2405, (ii) 29432, (iii) 31837. timer_iso is a check (policy step mapped by isotonic regression), not a candidate.

