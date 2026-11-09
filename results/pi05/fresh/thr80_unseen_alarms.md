# Unnecessary and false alarms vs progress

Paired bootstrap vs progress for unnecessary alarms (recoverable failures) and false alarms (successes), as results/week3/regression/intervals.md (10000 draws, seed 0, same draws for both models). Reads DIR/per_episode.json of any run (Nov 6 plan: combo, realistic). Difference = model minus reference in alarmed runs; negative = fewer alarms.

| run | budget | model | unnecessary alarms | vs reference (95%) | false alarms | vs reference (95%) |
|---|---|---|---|---|---|---|
| data/pi05_fresh/thr80/unseen/merged | 0.05 | gru_phys_ttp_s0 | 1 vs 9 of 10 | -8 (-10 to -5) | 5 vs 25 of 633 | -20 (-30 to -10) |
| data/pi05_fresh/thr80/unseen/merged | 0.05 | gru_phys_ttp_s1 | 2 vs 9 of 10 | -7 (-10 to -4) | 12 vs 25 of 633 | -13 (-25 to -1) |
| data/pi05_fresh/thr80/unseen/merged | 0.05 | gru_phys_ttp_s2 | 1 vs 9 of 10 | -8 (-10 to -5) | 3 vs 25 of 633 | -22 (-33 to -12) |
| data/pi05_fresh/thr80/unseen/merged | 0.05 | gru_phys_ttp_s3 | 1 vs 9 of 10 | -8 (-10 to -5) | 2 vs 25 of 633 | -23 (-33 to -13) |
| data/pi05_fresh/thr80/unseen/merged | 0.05 | gru_phys_ttp_s4 | 1 vs 9 of 10 | -8 (-10 to -5) | 1 vs 25 of 633 | -24 (-34 to -14) |
| data/pi05_fresh/thr80/unseen/merged | 0.05 | gru_phys_ttp_ens | 1 vs 9 of 10 | -8 (-10 to -5) | 2 vs 25 of 633 | -23 (-33 to -14) |
| data/pi05_fresh/thr80/unseen/merged | 0.05 | or_progress_ens | 8 vs 9 of 10 | -1 (-3 to +0) | 12 vs 25 of 633 | -13 (-21 to -6) |
| data/pi05_fresh/thr80/unseen/merged | 0.025 | gru_phys_ttp_s0 | 1 vs 8 of 10 | -7 (-9 to -4) | 5 vs 10 of 633 | -5 (-12 to +1) |
| data/pi05_fresh/thr80/unseen/merged | 0.025 | gru_phys_ttp_s1 | 2 vs 8 of 10 | -6 (-9 to -3) | 5 vs 10 of 633 | -5 (-13 to +3) |
| data/pi05_fresh/thr80/unseen/merged | 0.025 | gru_phys_ttp_s2 | 1 vs 8 of 10 | -7 (-9 to -4) | 1 vs 10 of 633 | -9 (-16 to -3) |
| data/pi05_fresh/thr80/unseen/merged | 0.025 | gru_phys_ttp_s3 | 0 vs 8 of 10 | -8 (-10 to -5) | 1 vs 10 of 633 | -9 (-16 to -3) |
| data/pi05_fresh/thr80/unseen/merged | 0.025 | gru_phys_ttp_s4 | 1 vs 8 of 10 | -7 (-9 to -4) | 1 vs 10 of 633 | -9 (-16 to -3) |
| data/pi05_fresh/thr80/unseen/merged | 0.025 | gru_phys_ttp_ens | 1 vs 8 of 10 | -7 (-9 to -4) | 1 vs 10 of 633 | -9 (-16 to -3) |
| data/pi05_fresh/thr80/unseen/merged | 0.025 | or_progress_ens | 6 vs 8 of 10 | -2 (-5 to +0) | 5 vs 10 of 633 | -5 (-10 to +0) |
