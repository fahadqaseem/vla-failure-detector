# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/clock/pi05_thr80 | 0.05 | gru_phys_ttp_s0 | 0 vs 3 of 4 | -3 (-4 to -1) | 5 vs 46 of 928 | -41 (-55 to -28) |
| data/clock/pi05_thr80 | 0.05 | gru_phys_ttp_s1 | 0 vs 3 of 4 | -3 (-4 to -1) | 13 vs 46 of 928 | -33 (-46 to -20) |
| data/clock/pi05_thr80 | 0.05 | gru_phys_ttp_s2 | 0 vs 3 of 4 | -3 (-4 to -1) | 4 vs 46 of 928 | -42 (-56 to -29) |
| data/clock/pi05_thr80 | 0.05 | gru_phys_ttp_s3 | 0 vs 3 of 4 | -3 (-4 to -1) | 6 vs 46 of 928 | -40 (-54 to -27) |
| data/clock/pi05_thr80 | 0.05 | gru_phys_ttp_s4 | 0 vs 3 of 4 | -3 (-4 to -1) | 2 vs 46 of 928 | -44 (-58 to -31) |
| data/clock/pi05_thr80 | 0.05 | gru_phys_ttp_ens | 0 vs 3 of 4 | -3 (-4 to -1) | 3 vs 46 of 928 | -43 (-57 to -30) |
| data/clock/pi05_thr80 | 0.05 | or_progress_ttp_s0 | 3 vs 3 of 4 | +0 (+0 to +0) | 25 vs 46 of 928 | -21 (-31 to -12) |
| data/clock/pi05_thr80 | 0.05 | or_progress_ttp_s1 | 3 vs 3 of 4 | +0 (+0 to +0) | 27 vs 46 of 928 | -19 (-29 to -10) |
| data/clock/pi05_thr80 | 0.05 | or_progress_ttp_s2 | 3 vs 3 of 4 | +0 (+0 to +0) | 24 vs 46 of 928 | -22 (-32 to -13) |
| data/clock/pi05_thr80 | 0.05 | or_progress_ttp_s3 | 3 vs 3 of 4 | +0 (+0 to +0) | 25 vs 46 of 928 | -21 (-31 to -12) |
| data/clock/pi05_thr80 | 0.05 | or_progress_ttp_s4 | 3 vs 3 of 4 | +0 (+0 to +0) | 23 vs 46 of 928 | -23 (-33 to -14) |
| data/clock/pi05_thr80 | 0.05 | or_progress_ens | 3 vs 3 of 4 | +0 (+0 to +0) | 24 vs 46 of 928 | -22 (-32 to -13) |
| data/clock/pi05_thr80 | 0.025 | gru_phys_ttp_s0 | 0 vs 3 of 4 | -3 (-4 to -1) | 2 vs 23 of 928 | -21 (-31 to -12) |
| data/clock/pi05_thr80 | 0.025 | gru_phys_ttp_s1 | 0 vs 3 of 4 | -3 (-4 to -1) | 5 vs 23 of 928 | -18 (-28 to -8) |
| data/clock/pi05_thr80 | 0.025 | gru_phys_ttp_s2 | 0 vs 3 of 4 | -3 (-4 to -1) | 2 vs 23 of 928 | -21 (-31 to -12) |
| data/clock/pi05_thr80 | 0.025 | gru_phys_ttp_s3 | 0 vs 3 of 4 | -3 (-4 to -1) | 2 vs 23 of 928 | -21 (-31 to -12) |
| data/clock/pi05_thr80 | 0.025 | gru_phys_ttp_s4 | 0 vs 3 of 4 | -3 (-4 to -1) | 0 vs 23 of 928 | -23 (-33 to -14) |
| data/clock/pi05_thr80 | 0.025 | gru_phys_ttp_ens | 0 vs 3 of 4 | -3 (-4 to -1) | 2 vs 23 of 928 | -21 (-31 to -12) |
| data/clock/pi05_thr80 | 0.025 | or_progress_ttp_s0 | 2 vs 3 of 4 | -1 (-3 to +0) | 13 vs 23 of 928 | -10 (-17 to -4) |
| data/clock/pi05_thr80 | 0.025 | or_progress_ttp_s1 | 2 vs 3 of 4 | -1 (-3 to +0) | 13 vs 23 of 928 | -10 (-17 to -4) |
| data/clock/pi05_thr80 | 0.025 | or_progress_ttp_s2 | 2 vs 3 of 4 | -1 (-3 to +0) | 14 vs 23 of 928 | -9 (-16 to -3) |
| data/clock/pi05_thr80 | 0.025 | or_progress_ttp_s3 | 2 vs 3 of 4 | -1 (-3 to +0) | 13 vs 23 of 928 | -10 (-17 to -4) |
| data/clock/pi05_thr80 | 0.025 | or_progress_ttp_s4 | 2 vs 3 of 4 | -1 (-3 to +0) | 12 vs 23 of 928 | -11 (-18 to -5) |
| data/clock/pi05_thr80 | 0.025 | or_progress_ens | 2 vs 3 of 4 | -1 (-3 to +0) | 13 vs 23 of 928 | -10 (-17 to -4) |
