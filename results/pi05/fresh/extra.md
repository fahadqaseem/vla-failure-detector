# Fresh Pi0.5 test: task bootstrap and rescue value

Fresh Pi0.5 test extras (Fahad, Nov 9): on data/pi05_fresh/thr{T}/{split}/merged/per_episode.json (models trained on the old episodes, scored on the new perturbed seeds 2 to 4 only): (1) task bootstrap as results/tasklevel (per-task timely and false alarms vs progress, 10000 draws over the held-out tasks, seed 0, tasks better / worse / equal); (2) rescue value as results/rescue (retry success fraction at the last scanned checkpoint at or before each alarm on a scanned failure, per 100 runs; as scanned and by step 520), next to false alarms per 100 runs.

## Task bootstrap

| split | rule | budget | model | timely (vs progress) | bootstrap over tasks (95%) | tasks better / worse / equal | false alarms (vs progress) |
|---|---|---|---|---|---|---|---|
| unseen | 50% | 0.025 | gru_phys_ttp_s0 | 1 (-3) | -5 to -1 | 0 / 3 / 2 | 5 (-5) |
| unseen | 50% | 0.025 | gru_phys_ttp_s1 | 2 (-2) | -4 to +0 | 0 / 2 / 3 | 14 (+4) |
| unseen | 50% | 0.025 | gru_phys_ttp_s2 | 1 (-3) | -5 to -1 | 0 / 3 / 2 | 3 (-7) |
| unseen | 50% | 0.025 | gru_phys_ttp_s3 | 1 (-3) | -5 to -1 | 0 / 3 / 2 | 3 (-7) |
| unseen | 50% | 0.025 | gru_phys_ttp_s4 | 1 (-3) | -5 to -1 | 0 / 3 / 2 | 1 (-9) |
| unseen | 50% | 0.025 | gru_phys_ttp_ens | 1 (-3) | -5 to -1 | 0 / 3 / 2 | 1 (-9) |
| unseen | 50% | 0.025 | or_progress_ens | 3 (-1) | -4 to +2 | 1 / 2 / 2 | 6 (-4) |
| unseen | 50% | 0.05 | gru_phys_ttp_s0 | 1 (-3) | -5 to -1 | 0 / 3 / 2 | 7 (-18) |
| unseen | 50% | 0.05 | gru_phys_ttp_s1 | 2 (-2) | -4 to +0 | 0 / 2 / 3 | 24 (-1) |
| unseen | 50% | 0.05 | gru_phys_ttp_s2 | 1 (-3) | -5 to -1 | 0 / 3 / 2 | 5 (-20) |
| unseen | 50% | 0.05 | gru_phys_ttp_s3 | 2 (-2) | -4 to +0 | 0 / 2 / 3 | 5 (-20) |
| unseen | 50% | 0.05 | gru_phys_ttp_s4 | 1 (-3) | -5 to -1 | 0 / 3 / 2 | 5 (-20) |
| unseen | 50% | 0.05 | gru_phys_ttp_ens | 1 (-3) | -5 to -1 | 0 / 3 / 2 | 4 (-21) |
| unseen | 50% | 0.05 | or_progress_ens | 5 (+1) | +0 to +3 | 1 / 0 / 4 | 13 (-12) |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_s0 | 4 (-3) | -8 to +2 | 1 / 2 / 2 | 10 (+0) |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_s1 | 4 (-3) | -7 to +0 | 0 / 2 / 3 | 11 (+1) |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_s2 | 3 (-4) | -9 to +1 | 1 / 3 / 1 | 4 (-6) |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_s3 | 2 (-5) | -10 to +1 | 1 / 3 / 1 | 3 (-7) |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_s4 | 3 (-4) | -9 to +1 | 1 / 3 / 1 | 5 (-5) |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_ens | 3 (-4) | -9 to +1 | 1 / 3 / 1 | 4 (-6) |
| unseen | 70% (main) | 0.025 | or_progress_ens | 8 (+1) | -2 to +4 | 2 / 1 / 2 | 7 (-3) |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_s0 | 4 (-3) | -8 to +2 | 1 / 2 / 2 | 16 (-9) |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_s1 | 5 (-2) | -7 to +2 | 1 / 2 / 2 | 19 (-6) |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_s2 | 3 (-4) | -9 to +1 | 1 / 3 / 1 | 9 (-16) |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_s3 | 2 (-5) | -10 to +1 | 1 / 3 / 1 | 5 (-20) |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_s4 | 3 (-4) | -9 to +1 | 1 / 3 / 1 | 10 (-15) |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_ens | 3 (-4) | -9 to +1 | 1 / 3 / 1 | 8 (-17) |
| unseen | 70% (main) | 0.05 | or_progress_ens | 10 (+3) | +1 to +5 | 3 / 0 / 2 | 15 (-10) |
| unseen | 80% | 0.025 | gru_phys_ttp_s0 | 2 (-6) | -14 to +0 | 0 / 2 / 3 | 5 (-5) |
| unseen | 80% | 0.025 | gru_phys_ttp_s1 | 2 (-6) | -10 to -2 | 0 / 3 / 2 | 5 (-5) |
| unseen | 80% | 0.025 | gru_phys_ttp_s2 | 3 (-5) | -11 to +0 | 0 / 2 / 3 | 1 (-9) |
| unseen | 80% | 0.025 | gru_phys_ttp_s3 | 1 (-7) | -12 to -2 | 0 / 3 / 2 | 1 (-9) |
| unseen | 80% | 0.025 | gru_phys_ttp_s4 | 2 (-6) | -14 to +0 | 0 / 2 / 3 | 1 (-9) |
| unseen | 80% | 0.025 | gru_phys_ttp_ens | 3 (-5) | -11 to +0 | 0 / 2 / 3 | 1 (-9) |
| unseen | 80% | 0.025 | or_progress_ens | 7 (-1) | -6 to +3 | 1 / 1 / 3 | 5 (-5) |
| unseen | 80% | 0.05 | gru_phys_ttp_s0 | 3 (-5) | -11 to +0 | 0 / 2 / 3 | 5 (-20) |
| unseen | 80% | 0.05 | gru_phys_ttp_s1 | 2 (-6) | -10 to -2 | 0 / 3 / 2 | 12 (-13) |
| unseen | 80% | 0.05 | gru_phys_ttp_s2 | 3 (-5) | -11 to +0 | 0 / 2 / 3 | 3 (-22) |
| unseen | 80% | 0.05 | gru_phys_ttp_s3 | 1 (-7) | -12 to -2 | 0 / 3 / 2 | 2 (-23) |
| unseen | 80% | 0.05 | gru_phys_ttp_s4 | 3 (-5) | -11 to +0 | 0 / 2 / 3 | 1 (-24) |
| unseen | 80% | 0.05 | gru_phys_ttp_ens | 3 (-5) | -11 to +0 | 0 / 2 / 3 | 2 (-23) |
| unseen | 80% | 0.05 | or_progress_ens | 11 (+3) | +0 to +7 | 2 / 0 / 3 | 12 (-13) |
| seen | 50% | 0.025 | gru_phys_ttp_s0 | 0 (-3) | -7 to +0 | 0 / 2 / 3 | 2 (-7) |
| seen | 50% | 0.025 | gru_phys_ttp_s1 | 0 (-3) | -7 to +0 | 0 / 2 / 3 | 6 (-3) |
| seen | 50% | 0.025 | gru_phys_ttp_s2 | 0 (-3) | -7 to +0 | 0 / 2 / 3 | 5 (-4) |
| seen | 50% | 0.025 | gru_phys_ttp_s3 | 0 (-3) | -7 to +0 | 0 / 2 / 3 | 5 (-4) |
| seen | 50% | 0.025 | gru_phys_ttp_s4 | 0 (-3) | -7 to +0 | 0 / 2 / 3 | 5 (-4) |
| seen | 50% | 0.025 | gru_phys_ttp_ens | 0 (-3) | -7 to +0 | 0 / 2 / 3 | 5 (-4) |
| seen | 50% | 0.025 | or_progress_ens | 3 (+0) | +0 to +0 | 0 / 0 / 5 | 7 (-2) |
| seen | 50% | 0.05 | gru_phys_ttp_s0 | 0 (-4) | -7 to -1 | 0 / 3 / 2 | 3 (-18) |
| seen | 50% | 0.05 | gru_phys_ttp_s1 | 0 (-4) | -7 to -1 | 0 / 3 / 2 | 6 (-15) |
| seen | 50% | 0.05 | gru_phys_ttp_s2 | 0 (-4) | -7 to -1 | 0 / 3 / 2 | 6 (-15) |
| seen | 50% | 0.05 | gru_phys_ttp_s3 | 0 (-4) | -7 to -1 | 0 / 3 / 2 | 6 (-15) |
| seen | 50% | 0.05 | gru_phys_ttp_s4 | 0 (-4) | -7 to -1 | 0 / 3 / 2 | 8 (-13) |
| seen | 50% | 0.05 | gru_phys_ttp_ens | 0 (-4) | -7 to -1 | 0 / 3 / 2 | 6 (-15) |
| seen | 50% | 0.05 | or_progress_ens | 3 (-1) | -3 to +0 | 0 / 1 / 4 | 13 (-8) |
| seen | 70% (main) | 0.025 | gru_phys_ttp_s0 | 1 (-6) | -11 to -1 | 0 / 3 / 2 | 1 (-8) |
| seen | 70% (main) | 0.025 | gru_phys_ttp_s1 | 1 (-6) | -11 to -1 | 0 / 3 / 2 | 3 (-6) |
| seen | 70% (main) | 0.025 | gru_phys_ttp_s2 | 1 (-6) | -11 to -1 | 0 / 3 / 2 | 4 (-5) |
| seen | 70% (main) | 0.025 | gru_phys_ttp_s3 | 0 (-7) | -12 to -2 | 0 / 3 / 2 | 1 (-8) |
| seen | 70% (main) | 0.025 | gru_phys_ttp_s4 | 1 (-6) | -11 to -1 | 0 / 3 / 2 | 3 (-6) |
| seen | 70% (main) | 0.025 | gru_phys_ttp_ens | 1 (-6) | -11 to -1 | 0 / 3 / 2 | 3 (-6) |
| seen | 70% (main) | 0.025 | or_progress_ens | 6 (-1) | -3 to +0 | 0 / 1 / 4 | 7 (-2) |
| seen | 70% (main) | 0.05 | gru_phys_ttp_s0 | 1 (-6) | -11 to -1 | 0 / 3 / 2 | 1 (-20) |
| seen | 70% (main) | 0.05 | gru_phys_ttp_s1 | 2 (-5) | -9 to -1 | 0 / 3 / 2 | 4 (-17) |
| seen | 70% (main) | 0.05 | gru_phys_ttp_s2 | 1 (-6) | -11 to -1 | 0 / 3 / 2 | 4 (-17) |
| seen | 70% (main) | 0.05 | gru_phys_ttp_s3 | 1 (-6) | -11 to -1 | 0 / 3 / 2 | 3 (-18) |
| seen | 70% (main) | 0.05 | gru_phys_ttp_s4 | 1 (-6) | -11 to -1 | 0 / 3 / 2 | 4 (-17) |
| seen | 70% (main) | 0.05 | gru_phys_ttp_ens | 1 (-6) | -11 to -1 | 0 / 3 / 2 | 3 (-18) |
| seen | 70% (main) | 0.05 | or_progress_ens | 8 (+1) | +0 to +3 | 1 / 0 / 4 | 12 (-9) |
| seen | 80% | 0.025 | gru_phys_ttp_s0 | 1 (-7) | -14 to -1 | 0 / 3 / 2 | 1 (-8) |
| seen | 80% | 0.025 | gru_phys_ttp_s1 | 1 (-7) | -14 to -1 | 0 / 3 / 2 | 3 (-6) |
| seen | 80% | 0.025 | gru_phys_ttp_s2 | 2 (-6) | -14 to +0 | 0 / 2 / 3 | 1 (-8) |
| seen | 80% | 0.025 | gru_phys_ttp_s3 | 1 (-7) | -14 to -1 | 0 / 3 / 2 | 1 (-8) |
| seen | 80% | 0.025 | gru_phys_ttp_s4 | 1 (-7) | -14 to -1 | 0 / 3 / 2 | 1 (-8) |
| seen | 80% | 0.025 | gru_phys_ttp_ens | 1 (-7) | -14 to -1 | 0 / 3 / 2 | 1 (-8) |
| seen | 80% | 0.025 | or_progress_ens | 8 (+0) | -3 to +3 | 1 / 1 / 3 | 5 (-4) |
| seen | 80% | 0.05 | gru_phys_ttp_s0 | 1 (-7) | -14 to -1 | 0 / 3 / 2 | 1 (-20) |
| seen | 80% | 0.05 | gru_phys_ttp_s1 | 3 (-5) | -13 to +0 | 0 / 2 / 3 | 3 (-18) |
| seen | 80% | 0.05 | gru_phys_ttp_s2 | 2 (-6) | -14 to +0 | 0 / 2 / 3 | 1 (-20) |
| seen | 80% | 0.05 | gru_phys_ttp_s3 | 2 (-6) | -13 to -1 | 0 / 3 / 2 | 1 (-20) |
| seen | 80% | 0.05 | gru_phys_ttp_s4 | 1 (-7) | -14 to -1 | 0 / 3 / 2 | 1 (-20) |
| seen | 80% | 0.05 | gru_phys_ttp_ens | 3 (-5) | -13 to +0 | 0 / 2 / 3 | 1 (-20) |
| seen | 80% | 0.05 | or_progress_ens | 9 (+1) | +0 to +3 | 1 / 0 / 4 | 10 (-11) |

## Rescue value

| split | rule | budget | model | runs | alarms on scanned failures | expected rescues / 100 runs (as scanned) | (by step 520) | false alarms / 100 runs |
|---|---|---|---|---|---|---|---|---|
| unseen | 50% | 0.025 | progress | 668 | 26 | 0.37 | 0.07 | 1.50 |
| unseen | 50% | 0.025 | gru_phys_ttp_s0 | 668 | 4 | 0.19 | 0.19 | 0.75 |
| unseen | 50% | 0.025 | gru_phys_ttp_s1 | 668 | 6 | 0.30 | 0.30 | 2.10 |
| unseen | 50% | 0.025 | gru_phys_ttp_s2 | 668 | 3 | 0.11 | 0.07 | 0.45 |
| unseen | 50% | 0.025 | gru_phys_ttp_s3 | 668 | 1 | 0.00 | 0.00 | 0.45 |
| unseen | 50% | 0.025 | gru_phys_ttp_s4 | 668 | 5 | 0.04 | 0.04 | 0.15 |
| unseen | 50% | 0.025 | gru_phys_ttp_ens | 668 | 4 | 0.19 | 0.15 | 0.15 |
| unseen | 50% | 0.025 | or_progress_ens | 668 | 23 | 0.41 | 0.04 | 0.90 |
| unseen | 50% | 0.05 | progress | 668 | 28 | 0.30 | 0.04 | 3.74 |
| unseen | 50% | 0.05 | gru_phys_ttp_s0 | 668 | 6 | 0.04 | 0.04 | 1.05 |
| unseen | 50% | 0.05 | gru_phys_ttp_s1 | 668 | 6 | 0.34 | 0.30 | 3.59 |
| unseen | 50% | 0.05 | gru_phys_ttp_s2 | 668 | 3 | 0.11 | 0.07 | 0.75 |
| unseen | 50% | 0.05 | gru_phys_ttp_s3 | 668 | 2 | 0.22 | 0.22 | 0.75 |
| unseen | 50% | 0.05 | gru_phys_ttp_s4 | 668 | 7 | 0.00 | 0.00 | 0.75 |
| unseen | 50% | 0.05 | gru_phys_ttp_ens | 668 | 4 | 0.11 | 0.07 | 0.60 |
| unseen | 50% | 0.05 | or_progress_ens | 668 | 26 | 0.49 | 0.11 | 1.95 |
| unseen | 70% (main) | 0.025 | progress | 668 | 26 | 0.37 | 0.07 | 1.50 |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_s0 | 668 | 6 | 0.34 | 0.26 | 1.50 |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_s1 | 668 | 6 | 0.37 | 0.34 | 1.65 |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_s2 | 668 | 3 | 0.19 | 0.15 | 0.60 |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_s3 | 668 | 2 | 0.07 | 0.07 | 0.45 |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_s4 | 668 | 5 | 0.19 | 0.19 | 0.75 |
| unseen | 70% (main) | 0.025 | gru_phys_ttp_ens | 668 | 5 | 0.15 | 0.07 | 0.60 |
| unseen | 70% (main) | 0.025 | or_progress_ens | 668 | 23 | 0.60 | 0.19 | 1.05 |
| unseen | 70% (main) | 0.05 | progress | 668 | 28 | 0.30 | 0.04 | 3.74 |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_s0 | 668 | 6 | 0.15 | 0.11 | 2.40 |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_s1 | 668 | 7 | 0.30 | 0.26 | 2.84 |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_s2 | 668 | 3 | 0.26 | 0.22 | 1.35 |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_s3 | 668 | 2 | 0.19 | 0.15 | 0.75 |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_s4 | 668 | 5 | 0.19 | 0.19 | 1.50 |
| unseen | 70% (main) | 0.05 | gru_phys_ttp_ens | 668 | 5 | 0.22 | 0.15 | 1.20 |
| unseen | 70% (main) | 0.05 | or_progress_ens | 668 | 26 | 0.56 | 0.15 | 2.25 |
| unseen | 80% | 0.025 | progress | 668 | 26 | 0.37 | 0.07 | 1.50 |
| unseen | 80% | 0.025 | gru_phys_ttp_s0 | 668 | 3 | 0.04 | 0.04 | 0.75 |
| unseen | 80% | 0.025 | gru_phys_ttp_s1 | 668 | 3 | 0.22 | 0.19 | 0.75 |
| unseen | 80% | 0.025 | gru_phys_ttp_s2 | 668 | 4 | 0.11 | 0.07 | 0.15 |
| unseen | 80% | 0.025 | gru_phys_ttp_s3 | 668 | 1 | 0.00 | 0.00 | 0.15 |
| unseen | 80% | 0.025 | gru_phys_ttp_s4 | 668 | 3 | 0.04 | 0.04 | 0.15 |
| unseen | 80% | 0.025 | gru_phys_ttp_ens | 668 | 4 | 0.11 | 0.04 | 0.15 |
| unseen | 80% | 0.025 | or_progress_ens | 668 | 22 | 0.41 | 0.15 | 0.75 |
| unseen | 80% | 0.05 | progress | 668 | 28 | 0.30 | 0.04 | 3.74 |
| unseen | 80% | 0.05 | gru_phys_ttp_s0 | 668 | 4 | 0.19 | 0.19 | 0.75 |
| unseen | 80% | 0.05 | gru_phys_ttp_s1 | 668 | 3 | 0.22 | 0.19 | 1.80 |
| unseen | 80% | 0.05 | gru_phys_ttp_s2 | 668 | 4 | 0.15 | 0.11 | 0.45 |
| unseen | 80% | 0.05 | gru_phys_ttp_s3 | 668 | 1 | 0.07 | 0.07 | 0.30 |
| unseen | 80% | 0.05 | gru_phys_ttp_s4 | 668 | 4 | 0.15 | 0.15 | 0.15 |
| unseen | 80% | 0.05 | gru_phys_ttp_ens | 668 | 4 | 0.15 | 0.11 | 0.30 |
| unseen | 80% | 0.05 | or_progress_ens | 668 | 26 | 0.34 | 0.15 | 1.80 |
| seen | 50% | 0.025 | progress | 668 | 26 | 0.45 | 0.07 | 1.35 |
| seen | 50% | 0.025 | gru_phys_ttp_s0 | 668 | 4 | 0.07 | 0.04 | 0.30 |
| seen | 50% | 0.025 | gru_phys_ttp_s1 | 668 | 6 | 0.04 | 0.00 | 0.90 |
| seen | 50% | 0.025 | gru_phys_ttp_s2 | 668 | 5 | 0.07 | 0.04 | 0.75 |
| seen | 50% | 0.025 | gru_phys_ttp_s3 | 668 | 6 | 0.11 | 0.04 | 0.75 |
| seen | 50% | 0.025 | gru_phys_ttp_s4 | 668 | 6 | 0.19 | 0.07 | 0.75 |
| seen | 50% | 0.025 | gru_phys_ttp_ens | 668 | 7 | 0.07 | 0.00 | 0.75 |
| seen | 50% | 0.025 | or_progress_ens | 668 | 25 | 0.45 | 0.04 | 1.05 |
| seen | 50% | 0.05 | progress | 668 | 28 | 0.37 | 0.04 | 3.14 |
| seen | 50% | 0.05 | gru_phys_ttp_s0 | 668 | 4 | 0.07 | 0.04 | 0.45 |
| seen | 50% | 0.05 | gru_phys_ttp_s1 | 668 | 7 | 0.04 | 0.00 | 0.90 |
| seen | 50% | 0.05 | gru_phys_ttp_s2 | 668 | 7 | 0.15 | 0.04 | 0.90 |
| seen | 50% | 0.05 | gru_phys_ttp_s3 | 668 | 6 | 0.07 | 0.00 | 0.90 |
| seen | 50% | 0.05 | gru_phys_ttp_s4 | 668 | 10 | 0.19 | 0.11 | 1.20 |
| seen | 50% | 0.05 | gru_phys_ttp_ens | 668 | 7 | 0.07 | 0.00 | 0.90 |
| seen | 50% | 0.05 | or_progress_ens | 668 | 26 | 0.49 | 0.07 | 1.95 |
| seen | 70% (main) | 0.025 | progress | 668 | 26 | 0.45 | 0.07 | 1.35 |
| seen | 70% (main) | 0.025 | gru_phys_ttp_s0 | 668 | 1 | 0.07 | 0.07 | 0.15 |
| seen | 70% (main) | 0.025 | gru_phys_ttp_s1 | 668 | 6 | 0.15 | 0.07 | 0.45 |
| seen | 70% (main) | 0.025 | gru_phys_ttp_s2 | 668 | 3 | 0.04 | 0.04 | 0.60 |
| seen | 70% (main) | 0.025 | gru_phys_ttp_s3 | 668 | 2 | 0.04 | 0.04 | 0.15 |
| seen | 70% (main) | 0.025 | gru_phys_ttp_s4 | 668 | 5 | 0.11 | 0.04 | 0.45 |
| seen | 70% (main) | 0.025 | gru_phys_ttp_ens | 668 | 3 | 0.11 | 0.04 | 0.45 |
| seen | 70% (main) | 0.025 | or_progress_ens | 668 | 23 | 0.41 | 0.07 | 1.05 |
| seen | 70% (main) | 0.05 | progress | 668 | 28 | 0.37 | 0.04 | 3.14 |
| seen | 70% (main) | 0.05 | gru_phys_ttp_s0 | 668 | 1 | 0.04 | 0.04 | 0.15 |
| seen | 70% (main) | 0.05 | gru_phys_ttp_s1 | 668 | 7 | 0.11 | 0.04 | 0.60 |
| seen | 70% (main) | 0.05 | gru_phys_ttp_s2 | 668 | 4 | 0.07 | 0.04 | 0.60 |
| seen | 70% (main) | 0.05 | gru_phys_ttp_s3 | 668 | 4 | 0.11 | 0.04 | 0.45 |
| seen | 70% (main) | 0.05 | gru_phys_ttp_s4 | 668 | 5 | 0.15 | 0.04 | 0.60 |
| seen | 70% (main) | 0.05 | gru_phys_ttp_ens | 668 | 3 | 0.11 | 0.04 | 0.45 |
| seen | 70% (main) | 0.05 | or_progress_ens | 668 | 26 | 0.56 | 0.11 | 1.80 |
| seen | 80% | 0.025 | progress | 668 | 26 | 0.45 | 0.07 | 1.35 |
| seen | 80% | 0.025 | gru_phys_ttp_s0 | 668 | 1 | 0.07 | 0.07 | 0.15 |
| seen | 80% | 0.025 | gru_phys_ttp_s1 | 668 | 1 | 0.04 | 0.04 | 0.45 |
| seen | 80% | 0.025 | gru_phys_ttp_s2 | 668 | 2 | 0.07 | 0.04 | 0.15 |
| seen | 80% | 0.025 | gru_phys_ttp_s3 | 668 | 1 | 0.04 | 0.04 | 0.15 |
| seen | 80% | 0.025 | gru_phys_ttp_s4 | 668 | 1 | 0.07 | 0.07 | 0.15 |
| seen | 80% | 0.025 | gru_phys_ttp_ens | 668 | 1 | 0.00 | 0.00 | 0.15 |
| seen | 80% | 0.025 | or_progress_ens | 668 | 23 | 0.45 | 0.11 | 0.75 |
| seen | 80% | 0.05 | progress | 668 | 28 | 0.37 | 0.04 | 3.14 |
| seen | 80% | 0.05 | gru_phys_ttp_s0 | 668 | 1 | 0.04 | 0.00 | 0.15 |
| seen | 80% | 0.05 | gru_phys_ttp_s1 | 668 | 4 | 0.11 | 0.04 | 0.45 |
| seen | 80% | 0.05 | gru_phys_ttp_s2 | 668 | 3 | 0.04 | 0.04 | 0.15 |
| seen | 80% | 0.05 | gru_phys_ttp_s3 | 668 | 4 | 0.15 | 0.04 | 0.15 |
| seen | 80% | 0.05 | gru_phys_ttp_s4 | 668 | 2 | 0.07 | 0.04 | 0.15 |
| seen | 80% | 0.05 | gru_phys_ttp_ens | 668 | 3 | 0.15 | 0.04 | 0.15 |
| seen | 80% | 0.05 | or_progress_ens | 668 | 26 | 0.49 | 0.11 | 1.50 |
