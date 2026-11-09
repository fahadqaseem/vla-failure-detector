# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/clock/oft_thr80 | 0.05 | gru_phys_ttp_s0 | 3 vs 18 of 19 | -15 (-18 to -11) | 27 vs 51 of 1071 | -24 (-40 to -8) |
| data/clock/oft_thr80 | 0.05 | gru_phys_ttp_s1 | 5 vs 18 of 19 | -13 (-17 to -9) | 23 vs 51 of 1071 | -28 (-43 to -13) |
| data/clock/oft_thr80 | 0.05 | gru_phys_ttp_s2 | 4 vs 18 of 19 | -14 (-17 to -10) | 24 vs 51 of 1071 | -27 (-43 to -12) |
| data/clock/oft_thr80 | 0.05 | gru_phys_ttp_s3 | 4 vs 18 of 19 | -14 (-17 to -10) | 64 vs 51 of 1071 | +13 (-7 to +33) |
| data/clock/oft_thr80 | 0.05 | gru_phys_ttp_s4 | 4 vs 18 of 19 | -14 (-17 to -10) | 33 vs 51 of 1071 | -18 (-34 to -1) |
| data/clock/oft_thr80 | 0.05 | gru_phys_ttp_ens | 5 vs 18 of 19 | -13 (-17 to -9) | 26 vs 51 of 1071 | -25 (-41 to -9) |
| data/clock/oft_thr80 | 0.05 | or_progress_ttp_s0 | 18 vs 18 of 19 | +0 (+0 to +0) | 41 vs 51 of 1071 | -10 (-22 to +1) |
| data/clock/oft_thr80 | 0.05 | or_progress_ttp_s1 | 18 vs 18 of 19 | +0 (+0 to +0) | 44 vs 51 of 1071 | -7 (-18 to +4) |
| data/clock/oft_thr80 | 0.05 | or_progress_ttp_s2 | 18 vs 18 of 19 | +0 (+0 to +0) | 38 vs 51 of 1071 | -13 (-24 to -2) |
| data/clock/oft_thr80 | 0.05 | or_progress_ttp_s3 | 18 vs 18 of 19 | +0 (+0 to +0) | 57 vs 51 of 1071 | +6 (-8 to +20) |
| data/clock/oft_thr80 | 0.05 | or_progress_ttp_s4 | 18 vs 18 of 19 | +0 (+0 to +0) | 53 vs 51 of 1071 | +2 (-11 to +15) |
| data/clock/oft_thr80 | 0.05 | or_progress_ens | 18 vs 18 of 19 | +0 (+0 to +0) | 48 vs 51 of 1071 | -3 (-15 to +8) |
| data/clock/oft_thr80 | 0.025 | gru_phys_ttp_s0 | 3 vs 15 of 19 | -12 (-17 to -6) | 13 vs 27 of 1071 | -14 (-25 to -3) |
| data/clock/oft_thr80 | 0.025 | gru_phys_ttp_s1 | 4 vs 15 of 19 | -11 (-16 to -5) | 15 vs 27 of 1071 | -12 (-23 to -1) |
| data/clock/oft_thr80 | 0.025 | gru_phys_ttp_s2 | 3 vs 15 of 19 | -12 (-17 to -6) | 15 vs 27 of 1071 | -12 (-23 to -1) |
| data/clock/oft_thr80 | 0.025 | gru_phys_ttp_s3 | 4 vs 15 of 19 | -11 (-16 to -5) | 33 vs 27 of 1071 | +6 (-8 to +20) |
| data/clock/oft_thr80 | 0.025 | gru_phys_ttp_s4 | 4 vs 15 of 19 | -11 (-16 to -5) | 26 vs 27 of 1071 | -1 (-14 to +12) |
| data/clock/oft_thr80 | 0.025 | gru_phys_ttp_ens | 4 vs 15 of 19 | -11 (-16 to -5) | 20 vs 27 of 1071 | -7 (-19 to +5) |
| data/clock/oft_thr80 | 0.025 | or_progress_ttp_s0 | 16 vs 15 of 19 | +1 (-2 to +4) | 20 vs 27 of 1071 | -7 (-15 to +0) |
| data/clock/oft_thr80 | 0.025 | or_progress_ttp_s1 | 16 vs 15 of 19 | +1 (-2 to +4) | 23 vs 27 of 1071 | -4 (-12 to +4) |
| data/clock/oft_thr80 | 0.025 | or_progress_ttp_s2 | 16 vs 15 of 19 | +1 (-2 to +4) | 26 vs 27 of 1071 | -1 (-8 to +6) |
| data/clock/oft_thr80 | 0.025 | or_progress_ttp_s3 | 16 vs 15 of 19 | +1 (-2 to +4) | 32 vs 27 of 1071 | +5 (-5 to +15) |
| data/clock/oft_thr80 | 0.025 | or_progress_ttp_s4 | 16 vs 15 of 19 | +1 (-2 to +4) | 23 vs 27 of 1071 | -4 (-12 to +4) |
| data/clock/oft_thr80 | 0.025 | or_progress_ens | 16 vs 15 of 19 | +1 (-2 to +4) | 24 vs 27 of 1071 | -3 (-11 to +5) |
