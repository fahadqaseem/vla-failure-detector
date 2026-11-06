# Timely alarms at matched false-alarm rates, unseen tasks

Timely alarms at matched false-alarm rates (Fahad, Nov 6, pre-registered in results/plan_nov06.md, item 3). Existing seed 0 scores, no retraining. For every model the threshold is set on the held-out successes (pooled over the leave-one-task-out folds): the lowest threshold at which at most a fraction r of successes alarm. So this compares models at the SAME realized false-alarm rate; it is descriptive, not a deployable rule (a deployed threshold must come from training tasks). Matched rate = progress's realized rate at its own fixed 5% / 2.5% threshold. Timely = alarm at or before t_pnr, failures with t_pnr > 0. Paired bootstrap over those failures (10000 draws, seed 0, same draws for both models) with the thresholds held fixed.

## At progress's realized false-alarm rate

| policy | rule | progress budget | matched false-alarm rate | model | timely | vs progress (95%) |
|---|---|---|---|---|---|---|
| OpenVLA-OFT | 50% (tau 0.5) | 0.05 | 0.048 (model realized 0.047) | progress | 18 of 81 | reference |
| OpenVLA-OFT | 50% (tau 0.5) | 0.05 | 0.048 (model realized 0.048) | gru_phys | 21 of 81 | +3 (-6 to +12) |
| OpenVLA-OFT | 50% (tau 0.5) | 0.05 | 0.048 (model realized 0.048) | gru_phys_frac | 22 of 81 | +4 (-3 to +12) |
| OpenVLA-OFT | 50% (tau 0.5) | 0.05 | 0.048 (model realized 0.048) | gru_phys_ttp | 20 of 81 | +2 (-6 to +10) |
| OpenVLA-OFT | 50% (tau 0.5) | 0.025 | 0.025 (model realized 0.024) | progress | 11 of 81 | reference |
| OpenVLA-OFT | 50% (tau 0.5) | 0.025 | 0.025 (model realized 0.025) | gru_phys | 15 of 81 | +4 (-5 to +13) |
| OpenVLA-OFT | 50% (tau 0.5) | 0.025 | 0.025 (model realized 0.025) | gru_phys_frac | 20 of 81 | +9 (+1 to +17) |
| OpenVLA-OFT | 50% (tau 0.5) | 0.025 | 0.025 (model realized 0.025) | gru_phys_ttp | 18 of 81 | +7 (-1 to +15) |
| OpenVLA-OFT | 70% (3 of 4 fail) | 0.05 | 0.048 (model realized 0.047) | progress | 24 of 91 | reference |
| OpenVLA-OFT | 70% (3 of 4 fail) | 0.05 | 0.048 (model realized 0.048) | gru_phys | 19 of 91 | -5 (-14 to +5) |
| OpenVLA-OFT | 70% (3 of 4 fail) | 0.05 | 0.048 (model realized 0.048) | gru_phys_frac | 31 of 91 | +7 (-2 to +16) |
| OpenVLA-OFT | 70% (3 of 4 fail) | 0.05 | 0.048 (model realized 0.048) | gru_phys_ttp | 33 of 91 | +9 (+0 to +18) |
| OpenVLA-OFT | 70% (3 of 4 fail) | 0.025 | 0.025 (model realized 0.024) | progress | 15 of 91 | reference |
| OpenVLA-OFT | 70% (3 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys | 15 of 91 | +0 (-9 to +9) |
| OpenVLA-OFT | 70% (3 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys_frac | 29 of 91 | +14 (+5 to +23) |
| OpenVLA-OFT | 70% (3 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys_ttp | 26 of 91 | +11 (+2 to +20) |
| OpenVLA-OFT | 80% (4 of 4 fail) | 0.05 | 0.048 (model realized 0.047) | progress | 28 of 102 | reference |
| OpenVLA-OFT | 80% (4 of 4 fail) | 0.05 | 0.048 (model realized 0.048) | gru_phys | 24 of 102 | -4 (-13 to +5) |
| OpenVLA-OFT | 80% (4 of 4 fail) | 0.05 | 0.048 (model realized 0.048) | gru_phys_frac | 33 of 102 | +5 (-4 to +15) |
| OpenVLA-OFT | 80% (4 of 4 fail) | 0.05 | 0.048 (model realized 0.048) | gru_phys_ttp | 34 of 102 | +6 (-3 to +16) |
| OpenVLA-OFT | 80% (4 of 4 fail) | 0.025 | 0.025 (model realized 0.024) | progress | 18 of 102 | reference |
| OpenVLA-OFT | 80% (4 of 4 fail) | 0.025 | 0.025 (model realized 0.024) | gru_phys | 15 of 102 | -3 (-12 to +6) |
| OpenVLA-OFT | 80% (4 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys_frac | 29 of 102 | +11 (+2 to +21) |
| OpenVLA-OFT | 80% (4 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys_ttp | 29 of 102 | +11 (+2 to +21) |
| Pi0.5 | 50% (tau 0.5) | 0.05 | 0.050 (model realized 0.046) | progress | 5 of 27 | reference |
| Pi0.5 | 50% (tau 0.5) | 0.05 | 0.050 (model realized 0.050) | gru_phys | 10 of 27 | +5 (+0 to +10) |
| Pi0.5 | 50% (tau 0.5) | 0.05 | 0.050 (model realized 0.050) | gru_phys_frac | 7 of 27 | +2 (-2 to +6) |
| Pi0.5 | 50% (tau 0.5) | 0.05 | 0.050 (model realized 0.050) | gru_phys_ttp | 9 of 27 | +4 (+0 to +9) |
| Pi0.5 | 50% (tau 0.5) | 0.025 | 0.025 (model realized 0.023) | progress | 2 of 27 | reference |
| Pi0.5 | 50% (tau 0.5) | 0.025 | 0.025 (model realized 0.025) | gru_phys | 8 of 27 | +6 (+1 to +11) |
| Pi0.5 | 50% (tau 0.5) | 0.025 | 0.025 (model realized 0.025) | gru_phys_frac | 7 of 27 | +5 (+0 to +10) |
| Pi0.5 | 50% (tau 0.5) | 0.025 | 0.025 (model realized 0.025) | gru_phys_ttp | 8 of 27 | +6 (+1 to +11) |
| Pi0.5 | 70% (3 of 4 fail) | 0.05 | 0.050 (model realized 0.046) | progress | 8 of 31 | reference |
| Pi0.5 | 70% (3 of 4 fail) | 0.05 | 0.050 (model realized 0.050) | gru_phys | 12 of 31 | +4 (-2 to +10) |
| Pi0.5 | 70% (3 of 4 fail) | 0.05 | 0.050 (model realized 0.050) | gru_phys_frac | 11 of 31 | +3 (-3 to +9) |
| Pi0.5 | 70% (3 of 4 fail) | 0.05 | 0.050 (model realized 0.050) | gru_phys_ttp | 11 of 31 | +3 (-3 to +9) |
| Pi0.5 | 70% (3 of 4 fail) | 0.025 | 0.025 (model realized 0.023) | progress | 6 of 31 | reference |
| Pi0.5 | 70% (3 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys | 9 of 31 | +3 (-3 to +9) |
| Pi0.5 | 70% (3 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys_frac | 9 of 31 | +3 (-3 to +9) |
| Pi0.5 | 70% (3 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys_ttp | 9 of 31 | +3 (-3 to +9) |
| Pi0.5 | 80% (4 of 4 fail) | 0.05 | 0.050 (model realized 0.046) | progress | 17 of 33 | reference |
| Pi0.5 | 80% (4 of 4 fail) | 0.05 | 0.050 (model realized 0.050) | gru_phys | 11 of 33 | -6 (-11 to -1) |
| Pi0.5 | 80% (4 of 4 fail) | 0.05 | 0.050 (model realized 0.050) | gru_phys_frac | 11 of 33 | -6 (-12 to +0) |
| Pi0.5 | 80% (4 of 4 fail) | 0.05 | 0.050 (model realized 0.050) | gru_phys_ttp | 10 of 33 | -7 (-13 to -1) |
| Pi0.5 | 80% (4 of 4 fail) | 0.025 | 0.025 (model realized 0.023) | progress | 12 of 33 | reference |
| Pi0.5 | 80% (4 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys | 9 of 33 | -3 (-9 to +3) |
| Pi0.5 | 80% (4 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys_frac | 10 of 33 | -2 (-8 to +4) |
| Pi0.5 | 80% (4 of 4 fail) | 0.025 | 0.025 (model realized 0.025) | gru_phys_ttp | 9 of 33 | -3 (-9 to +3) |

## Curve (timely fraction at false-alarm rates 0 to 10%, every 1%); figure timely_vs_fa.png

| policy | rule | model | 0.0% | 1.0% | 2.0% | 3.0% | 4.0% | 5.0% | 6.0% | 7.0% | 8.0% | 9.0% | 10.0% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OpenVLA-OFT | 50% (tau 0.5) | progress | 0.00 | 0.11 | 0.14 | 0.15 | 0.19 | 0.22 | 0.25 | 0.26 | 0.26 | 0.26 | 0.27 |
| OpenVLA-OFT | 50% (tau 0.5) | gru_phys | 0.01 | 0.09 | 0.17 | 0.21 | 0.25 | 0.28 | 0.30 | 0.31 | 0.31 | 0.31 | 0.31 |
| OpenVLA-OFT | 50% (tau 0.5) | gru_phys_frac | 0.01 | 0.12 | 0.22 | 0.25 | 0.26 | 0.27 | 0.27 | 0.27 | 0.30 | 0.31 | 0.32 |
| OpenVLA-OFT | 50% (tau 0.5) | gru_phys_ttp | 0.02 | 0.10 | 0.20 | 0.23 | 0.25 | 0.25 | 0.25 | 0.25 | 0.26 | 0.30 | 0.32 |
| OpenVLA-OFT | 70% (3 of 4 fail) | progress | 0.01 | 0.14 | 0.14 | 0.19 | 0.21 | 0.26 | 0.31 | 0.32 | 0.32 | 0.32 | 0.37 |
| OpenVLA-OFT | 70% (3 of 4 fail) | gru_phys | 0.02 | 0.08 | 0.15 | 0.16 | 0.20 | 0.22 | 0.23 | 0.24 | 0.24 | 0.27 | 0.31 |
| OpenVLA-OFT | 70% (3 of 4 fail) | gru_phys_frac | 0.02 | 0.14 | 0.24 | 0.34 | 0.34 | 0.34 | 0.35 | 0.41 | 0.41 | 0.42 | 0.43 |
| OpenVLA-OFT | 70% (3 of 4 fail) | gru_phys_ttp | 0.02 | 0.15 | 0.26 | 0.31 | 0.34 | 0.36 | 0.40 | 0.41 | 0.41 | 0.42 | 0.45 |
| OpenVLA-OFT | 80% (4 of 4 fail) | progress | 0.03 | 0.16 | 0.17 | 0.21 | 0.23 | 0.27 | 0.33 | 0.35 | 0.35 | 0.35 | 0.39 |
| OpenVLA-OFT | 80% (4 of 4 fail) | gru_phys | 0.02 | 0.11 | 0.15 | 0.16 | 0.20 | 0.25 | 0.26 | 0.28 | 0.30 | 0.31 | 0.32 |
| OpenVLA-OFT | 80% (4 of 4 fail) | gru_phys_frac | 0.02 | 0.20 | 0.27 | 0.28 | 0.31 | 0.33 | 0.36 | 0.38 | 0.39 | 0.40 | 0.40 |
| OpenVLA-OFT | 80% (4 of 4 fail) | gru_phys_ttp | 0.00 | 0.18 | 0.25 | 0.31 | 0.33 | 0.34 | 0.35 | 0.37 | 0.39 | 0.39 | 0.39 |
| Pi0.5 | 50% (tau 0.5) | progress | 0.00 | 0.04 | 0.04 | 0.07 | 0.11 | 0.19 | 0.30 | 0.30 | 0.33 | 0.33 | 0.33 |
| Pi0.5 | 50% (tau 0.5) | gru_phys | 0.00 | 0.22 | 0.30 | 0.33 | 0.37 | 0.37 | 0.41 | 0.44 | 0.48 | 0.48 | 0.48 |
| Pi0.5 | 50% (tau 0.5) | gru_phys_frac | 0.11 | 0.22 | 0.26 | 0.26 | 0.26 | 0.26 | 0.30 | 0.30 | 0.30 | 0.30 | 0.30 |
| Pi0.5 | 50% (tau 0.5) | gru_phys_ttp | 0.15 | 0.26 | 0.30 | 0.30 | 0.30 | 0.33 | 0.33 | 0.33 | 0.33 | 0.33 | 0.33 |
| Pi0.5 | 70% (3 of 4 fail) | progress | 0.06 | 0.10 | 0.19 | 0.19 | 0.23 | 0.26 | 0.39 | 0.39 | 0.42 | 0.42 | 0.42 |
| Pi0.5 | 70% (3 of 4 fail) | gru_phys | 0.03 | 0.10 | 0.23 | 0.29 | 0.35 | 0.39 | 0.42 | 0.45 | 0.48 | 0.48 | 0.48 |
| Pi0.5 | 70% (3 of 4 fail) | gru_phys_frac | 0.16 | 0.29 | 0.29 | 0.32 | 0.32 | 0.35 | 0.35 | 0.35 | 0.35 | 0.35 | 0.39 |
| Pi0.5 | 70% (3 of 4 fail) | gru_phys_ttp | 0.13 | 0.29 | 0.29 | 0.29 | 0.32 | 0.35 | 0.35 | 0.39 | 0.39 | 0.39 | 0.39 |
| Pi0.5 | 80% (4 of 4 fail) | progress | 0.09 | 0.21 | 0.33 | 0.39 | 0.48 | 0.52 | 0.61 | 0.61 | 0.61 | 0.61 | 0.61 |
| Pi0.5 | 80% (4 of 4 fail) | gru_phys | 0.09 | 0.24 | 0.27 | 0.27 | 0.30 | 0.33 | 0.36 | 0.39 | 0.39 | 0.48 | 0.48 |
| Pi0.5 | 80% (4 of 4 fail) | gru_phys_frac | 0.15 | 0.27 | 0.30 | 0.30 | 0.30 | 0.33 | 0.36 | 0.36 | 0.39 | 0.39 | 0.42 |
| Pi0.5 | 80% (4 of 4 fail) | gru_phys_ttp | 0.15 | 0.27 | 0.27 | 0.27 | 0.27 | 0.30 | 0.30 | 0.33 | 0.36 | 0.36 | 0.39 |
