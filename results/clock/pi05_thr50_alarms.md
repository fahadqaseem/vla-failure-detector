# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/clock/pi05_thr50 | 0.05 | gru_phys_ttp_s0 | 1 vs 3 of 4 | -2 (-4 to +2) | 8 vs 46 of 928 | -38 (-52 to -25) |
| data/clock/pi05_thr50 | 0.05 | gru_phys_ttp_s1 | 0 vs 3 of 4 | -3 (-4 to -1) | 17 vs 46 of 928 | -29 (-43 to -16) |
| data/clock/pi05_thr50 | 0.05 | gru_phys_ttp_s2 | 0 vs 3 of 4 | -3 (-4 to -1) | 6 vs 46 of 928 | -40 (-53 to -27) |
| data/clock/pi05_thr50 | 0.05 | gru_phys_ttp_s3 | 1 vs 3 of 4 | -2 (-4 to +2) | 8 vs 46 of 928 | -38 (-51 to -26) |
| data/clock/pi05_thr50 | 0.05 | gru_phys_ttp_s4 | 0 vs 3 of 4 | -3 (-4 to -1) | 5 vs 46 of 928 | -41 (-55 to -28) |
| data/clock/pi05_thr50 | 0.05 | gru_phys_ttp_ens | 1 vs 3 of 4 | -2 (-4 to +2) | 6 vs 46 of 928 | -40 (-54 to -27) |
| data/clock/pi05_thr50 | 0.05 | or_progress_ttp_s0 | 4 vs 3 of 4 | +1 (+0 to +3) | 27 vs 46 of 928 | -19 (-29 to -9) |
| data/clock/pi05_thr50 | 0.05 | or_progress_ttp_s1 | 3 vs 3 of 4 | +0 (+0 to +0) | 36 vs 46 of 928 | -10 (-20 to +0) |
| data/clock/pi05_thr50 | 0.05 | or_progress_ttp_s2 | 3 vs 3 of 4 | +0 (+0 to +0) | 26 vs 46 of 928 | -20 (-30 to -11) |
| data/clock/pi05_thr50 | 0.05 | or_progress_ttp_s3 | 4 vs 3 of 4 | +1 (+0 to +3) | 26 vs 46 of 928 | -20 (-30 to -11) |
| data/clock/pi05_thr50 | 0.05 | or_progress_ttp_s4 | 3 vs 3 of 4 | +0 (+0 to +0) | 24 vs 46 of 928 | -22 (-31 to -13) |
| data/clock/pi05_thr50 | 0.05 | or_progress_ens | 3 vs 3 of 4 | +0 (+0 to +0) | 25 vs 46 of 928 | -21 (-31 to -12) |
| data/clock/pi05_thr50 | 0.025 | gru_phys_ttp_s0 | 1 vs 3 of 4 | -2 (-4 to +2) | 5 vs 23 of 928 | -18 (-28 to -8) |
| data/clock/pi05_thr50 | 0.025 | gru_phys_ttp_s1 | 0 vs 3 of 4 | -3 (-4 to -1) | 14 vs 23 of 928 | -9 (-19 to +1) |
| data/clock/pi05_thr50 | 0.025 | gru_phys_ttp_s2 | 0 vs 3 of 4 | -3 (-4 to -1) | 4 vs 23 of 928 | -19 (-29 to -10) |
| data/clock/pi05_thr50 | 0.025 | gru_phys_ttp_s3 | 1 vs 3 of 4 | -2 (-4 to +2) | 4 vs 23 of 928 | -19 (-29 to -10) |
| data/clock/pi05_thr50 | 0.025 | gru_phys_ttp_s4 | 0 vs 3 of 4 | -3 (-4 to -1) | 0 vs 23 of 928 | -23 (-33 to -14) |
| data/clock/pi05_thr50 | 0.025 | gru_phys_ttp_ens | 0 vs 3 of 4 | -3 (-4 to -1) | 0 vs 23 of 928 | -23 (-33 to -14) |
| data/clock/pi05_thr50 | 0.025 | or_progress_ttp_s0 | 3 vs 3 of 4 | +0 (-3 to +3) | 16 vs 23 of 928 | -7 (-14 to +0) |
| data/clock/pi05_thr50 | 0.025 | or_progress_ttp_s1 | 2 vs 3 of 4 | -1 (-3 to +0) | 22 vs 23 of 928 | -1 (-9 to +6) |
| data/clock/pi05_thr50 | 0.025 | or_progress_ttp_s2 | 2 vs 3 of 4 | -1 (-3 to +0) | 14 vs 23 of 928 | -9 (-16 to -2) |
| data/clock/pi05_thr50 | 0.025 | or_progress_ttp_s3 | 3 vs 3 of 4 | +0 (-3 to +3) | 12 vs 23 of 928 | -11 (-18 to -5) |
| data/clock/pi05_thr50 | 0.025 | or_progress_ttp_s4 | 2 vs 3 of 4 | -1 (-3 to +0) | 12 vs 23 of 928 | -11 (-18 to -5) |
| data/clock/pi05_thr50 | 0.025 | or_progress_ens | 2 vs 3 of 4 | -1 (-3 to +0) | 13 vs 23 of 928 | -10 (-17 to -4) |
