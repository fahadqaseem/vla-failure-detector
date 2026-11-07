# Seeds 0 to 4, seen tasks

Seed spread (Fahad, Nov 6, results/plan_nov06.md item 2): gru_phys, gru_phys_frac, gru_phys_ttp with seeds 0 to 4, both policies, three failure rules, unseen and seen tasks. Seed 0 = the runs of results/week3/regression and results/pi05/regression; seeds 1 to 4 = data/seeds/{policy}/thr{T}/{split}/s{S}/{model} (28_merge_groups.py already run). Per setting: mean and min to max over the 5 seeds of timely (alarm at or before t_pnr, failures with t_pnr > 0), false alarms on successes, unnecessary alarms on recoverable failures and median window t_alarm - t_pnr, and how many seeds beat progress (more timely alarms at the same budget; ties counted apart). Progress has no seed.

| policy | rule | budget | model | timely mean (min to max) | progress timely | seeds beating progress (ties) | false alarms | unnecessary | window |
|---|---|---|---|---|---|---|---|---|---|
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp | 15.8 (15.0 to 17.0) of 81 | 11 | 5 of 5 (0) | 0.025 (0.023 to 0.025) (progress 0.026) | 9.8 (9.0 to 10.0) of 31 (progress 22) | +70 (+64 to +72) (progress +180) |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_frac | 16.4 (15.0 to 17.0) of 81 | 11 | 5 of 5 (0) | 0.025 (0.024 to 0.026) (progress 0.026) | 11.6 (10.0 to 14.0) of 31 (progress 22) | +70 (+64 to +80) (progress +180) |
| OpenVLA-OFT | 50% | 0.025 | gru_phys | 18.0 (17.0 to 19.0) of 81 | 11 | 5 of 5 (0) | 0.023 (0.021 to 0.025) (progress 0.026) | 9.8 (8.0 to 12.0) of 31 (progress 22) | +63 (+60 to +64) (progress +180) |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp | 19.4 (18.0 to 21.0) of 81 | 16 | 5 of 5 (0) | 0.048 (0.046 to 0.050) (progress 0.046) | 18.0 (17.0 to 19.0) of 31 (progress 26) | +54 (+48 to +56) (progress +144) |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_frac | 19.2 (19.0 to 20.0) of 81 | 16 | 5 of 5 (0) | 0.048 (0.046 to 0.051) (progress 0.046) | 23.4 (22.0 to 25.0) of 31 (progress 26) | +54 (+48 to +56) (progress +144) |
| OpenVLA-OFT | 50% | 0.05 | gru_phys | 21.6 (20.0 to 23.0) of 81 | 16 | 5 of 5 (0) | 0.050 (0.042 to 0.060) (progress 0.046) | 13.6 (11.0 to 15.0) of 31 (progress 26) | +53 (+48 to +56) (progress +144) |
| OpenVLA-OFT | 70% | 0.025 | gru_phys_ttp | 27.8 (26.0 to 29.0) of 91 | 15 | 5 of 5 (0) | 0.024 (0.021 to 0.028) (progress 0.026) | 13.4 (11.0 to 16.0) of 35 (progress 25) | +40 (+32 to +48) (progress +136) |
| OpenVLA-OFT | 70% | 0.025 | gru_phys_frac | 28.6 (28.0 to 30.0) of 91 | 15 | 5 of 5 (0) | 0.025 (0.022 to 0.026) (progress 0.026) | 16.2 (15.0 to 18.0) of 35 (progress 25) | +43 (+40 to +48) (progress +136) |
| OpenVLA-OFT | 70% | 0.025 | gru_phys | 27.6 (27.0 to 29.0) of 91 | 15 | 5 of 5 (0) | 0.018 (0.016 to 0.021) (progress 0.026) | 14.2 (13.0 to 16.0) of 35 (progress 25) | +34 (+32 to +40) (progress +136) |
| OpenVLA-OFT | 70% | 0.05 | gru_phys_ttp | 36.8 (34.0 to 39.0) of 91 | 22 | 5 of 5 (0) | 0.046 (0.043 to 0.049) (progress 0.046) | 20.2 (20.0 to 21.0) of 35 (progress 29) | +19 (+16 to +24) (progress +112) |
| OpenVLA-OFT | 70% | 0.05 | gru_phys_frac | 36.8 (35.0 to 39.0) of 91 | 22 | 5 of 5 (0) | 0.048 (0.044 to 0.052) (progress 0.046) | 25.4 (23.0 to 27.0) of 35 (progress 29) | +20 (+16 to +24) (progress +112) |
| OpenVLA-OFT | 70% | 0.05 | gru_phys | 36.8 (36.0 to 38.0) of 91 | 22 | 5 of 5 (0) | 0.050 (0.042 to 0.059) (progress 0.046) | 17.8 (16.0 to 20.0) of 35 (progress 29) | +16 (+16 to +16) (progress +112) |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp | 38.6 (37.0 to 40.0) of 102 | 18 | 5 of 5 (0) | 0.024 (0.021 to 0.027) (progress 0.026) | 14.8 (14.0 to 16.0) of 39 (progress 28) | +26 (+24 to +32) (progress +128) |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_frac | 36.8 (35.0 to 40.0) of 102 | 18 | 5 of 5 (0) | 0.022 (0.021 to 0.023) (progress 0.026) | 17.4 (15.0 to 19.0) of 39 (progress 28) | +30 (+24 to +32) (progress +128) |
| OpenVLA-OFT | 80% | 0.025 | gru_phys | 38.6 (35.0 to 40.0) of 102 | 18 | 5 of 5 (0) | 0.024 (0.021 to 0.026) (progress 0.026) | 14.6 (13.0 to 16.0) of 39 (progress 28) | +22 (+16 to +24) (progress +128) |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp | 51.2 (50.0 to 53.0) of 102 | 28 | 5 of 5 (0) | 0.049 (0.045 to 0.054) (progress 0.046) | 19.0 (17.0 to 21.0) of 39 (progress 33) | -5 (-8 to +0) (progress +104) |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_frac | 49.4 (48.0 to 52.0) of 102 | 28 | 5 of 5 (0) | 0.046 (0.044 to 0.049) (progress 0.046) | 27.6 (27.0 to 28.0) of 39 (progress 33) | -1 (-4 to +0) (progress +104) |
| OpenVLA-OFT | 80% | 0.05 | gru_phys | 50.0 (49.0 to 51.0) of 102 | 28 | 5 of 5 (0) | 0.047 (0.040 to 0.054) (progress 0.046) | 16.8 (16.0 to 18.0) of 39 (progress 33) | -6 (-12 to +0) (progress +104) |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp | 9.8 (9.0 to 10.0) of 27 | 1 | 5 of 5 (0) | 0.024 (0.023 to 0.025) (progress 0.020) | 1.4 (1.0 to 2.0) of 7 (progress 6) | -9 (-32 to +40) (progress +160) |
| Pi0.5 | 50% | 0.025 | gru_phys_frac | 9.2 (8.0 to 10.0) of 27 | 1 | 5 of 5 (0) | 0.024 (0.022 to 0.026) (progress 0.020) | 2.8 (2.0 to 4.0) of 7 (progress 6) | +36 (-16 to +56) (progress +160) |
| Pi0.5 | 50% | 0.025 | gru_phys | 8.8 (7.0 to 10.0) of 27 | 1 | 5 of 5 (0) | 0.020 (0.017 to 0.025) (progress 0.020) | 1.6 (1.0 to 2.0) of 7 (progress 6) | +64 (+56 to +72) (progress +160) |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp | 11.2 (10.0 to 12.0) of 27 | 6 | 5 of 5 (0) | 0.052 (0.050 to 0.055) (progress 0.047) | 3.2 (3.0 to 4.0) of 7 (progress 6) | +9 (-24 to +56) (progress +96) |
| Pi0.5 | 50% | 0.05 | gru_phys_frac | 11.0 (10.0 to 12.0) of 27 | 6 | 5 of 5 (0) | 0.056 (0.052 to 0.058) (progress 0.047) | 5.2 (5.0 to 6.0) of 7 (progress 6) | +15 (+8 to +32) (progress +96) |
| Pi0.5 | 50% | 0.05 | gru_phys | 10.4 (10.0 to 11.0) of 27 | 6 | 5 of 5 (0) | 0.052 (0.050 to 0.055) (progress 0.047) | 3.6 (3.0 to 5.0) of 7 (progress 6) | +42 (+16 to +56) (progress +96) |
| Pi0.5 | 70% | 0.025 | gru_phys_ttp | 12.8 (11.0 to 14.0) of 31 | 6 | 5 of 5 (0) | 0.026 (0.024 to 0.031) (progress 0.020) | 1.8 (1.0 to 2.0) of 7 (progress 6) | -7 (-16 to +16) (progress +152) |
| Pi0.5 | 70% | 0.025 | gru_phys_frac | 12.2 (11.0 to 13.0) of 31 | 6 | 5 of 5 (0) | 0.026 (0.023 to 0.029) (progress 0.020) | 3.0 (2.0 to 4.0) of 7 (progress 6) | +14 (-8 to +32) (progress +152) |
| Pi0.5 | 70% | 0.025 | gru_phys | 9.4 (9.0 to 11.0) of 31 | 6 | 5 of 5 (0) | 0.022 (0.017 to 0.026) (progress 0.020) | 1.8 (1.0 to 2.0) of 7 (progress 6) | +25 (-8 to +48) (progress +152) |
| Pi0.5 | 70% | 0.05 | gru_phys_ttp | 16.6 (16.0 to 18.0) of 31 | 9 | 5 of 5 (0) | 0.059 (0.055 to 0.064) (progress 0.047) | 2.8 (2.0 to 4.0) of 7 (progress 6) | -39 (-56 to -24) (progress +76) |
| Pi0.5 | 70% | 0.05 | gru_phys_frac | 16.6 (16.0 to 17.0) of 31 | 9 | 5 of 5 (0) | 0.057 (0.054 to 0.060) (progress 0.047) | 4.4 (4.0 to 5.0) of 7 (progress 6) | -33 (-48 to -20) (progress +76) |
| Pi0.5 | 70% | 0.05 | gru_phys | 14.4 (14.0 to 16.0) of 31 | 9 | 5 of 5 (0) | 0.051 (0.044 to 0.055) (progress 0.047) | 4.0 (3.0 to 5.0) of 7 (progress 6) | -16 (-20 to -8) (progress +76) |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp | 17.0 (16.0 to 18.0) of 33 | 12 | 5 of 5 (0) | 0.022 (0.019 to 0.024) (progress 0.020) | 3.0 (3.0 to 3.0) of 8 (progress 7) | -71 (-76 to -64) (progress +40) |
| Pi0.5 | 80% | 0.025 | gru_phys_frac | 17.2 (16.0 to 18.0) of 33 | 12 | 5 of 5 (0) | 0.022 (0.019 to 0.025) (progress 0.020) | 3.0 (3.0 to 3.0) of 8 (progress 7) | -67 (-76 to -48) (progress +40) |
| Pi0.5 | 80% | 0.025 | gru_phys | 14.0 (12.0 to 16.0) of 33 | 12 | 4 of 5 (1) | 0.023 (0.019 to 0.026) (progress 0.020) | 3.4 (3.0 to 4.0) of 8 (progress 7) | -58 (-76 to -32) (progress +40) |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp | 19.0 (18.0 to 20.0) of 33 | 18 | 3 of 5 (2) | 0.053 (0.051 to 0.055) (progress 0.047) | 4.2 (4.0 to 5.0) of 8 (progress 7) | -105 (-128 to -80) (progress -44) |
| Pi0.5 | 80% | 0.05 | gru_phys_frac | 20.0 (19.0 to 21.0) of 33 | 18 | 5 of 5 (0) | 0.053 (0.051 to 0.057) (progress 0.047) | 5.4 (5.0 to 6.0) of 8 (progress 7) | -114 (-128 to -80) (progress -44) |
| Pi0.5 | 80% | 0.05 | gru_phys | 18.0 (17.0 to 19.0) of 33 | 18 | 1 of 5 (3) | 0.055 (0.050 to 0.066) (progress 0.047) | 3.8 (3.0 to 4.0) of 8 (progress 7) | -96 (-100 to -88) (progress -44) |
