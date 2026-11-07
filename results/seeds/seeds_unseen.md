# Seeds 0 to 4, unseen tasks

Seed spread (Fahad, Nov 6, results/plan_nov06.md item 2): gru_phys, gru_phys_frac, gru_phys_ttp with seeds 0 to 4, both policies, three failure rules, unseen and seen tasks. Seed 0 = the runs of results/week3/regression and results/pi05/regression; seeds 1 to 4 = data/seeds/{policy}/thr{T}/{split}/s{S}/{model} (28_merge_groups.py already run). Per setting: mean and min to max over the 5 seeds of timely (alarm at or before t_pnr, failures with t_pnr > 0), false alarms on successes, unnecessary alarms on recoverable failures and median window t_alarm - t_pnr, and how many seeds beat progress (more timely alarms at the same budget; ties counted apart). Progress has no seed.

| policy | rule | budget | model | timely mean (min to max) | progress timely | seeds beating progress (ties) | false alarms | unnecessary | window |
|---|---|---|---|---|---|---|---|---|---|
| OpenVLA-OFT | 50% | 0.025 | gru_phys_ttp | 11.8 (10.0 to 14.0) of 81 | 11 | 3 of 5 (0) | 0.025 (0.007 to 0.046) (progress 0.025) | 1.8 (1.0 to 2.0) of 31 (progress 22) | +112 (+104 to +120) (progress +200) |
| OpenVLA-OFT | 50% | 0.025 | gru_phys_frac | 12.2 (10.0 to 14.0) of 81 | 11 | 4 of 5 (0) | 0.042 (0.011 to 0.054) (progress 0.025) | 1.6 (1.0 to 3.0) of 31 (progress 22) | +106 (+96 to +120) (progress +200) |
| OpenVLA-OFT | 50% | 0.025 | gru_phys | 11.0 (7.0 to 17.0) of 81 | 11 | 2 of 5 (0) | 0.063 (0.007 to 0.278) (progress 0.025) | 2.2 (1.0 to 4.0) of 31 (progress 22) | +114 (+64 to +136) (progress +200) |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_ttp | 14.6 (11.0 to 18.0) of 81 | 17 | 1 of 5 (0) | 0.057 (0.030 to 0.079) (progress 0.048) | 3.6 (2.0 to 5.0) of 31 (progress 27) | +104 (+92 to +120) (progress +144) |
| OpenVLA-OFT | 50% | 0.05 | gru_phys_frac | 14.8 (13.0 to 16.0) of 81 | 17 | 0 of 5 (0) | 0.059 (0.055 to 0.061) (progress 0.048) | 2.8 (1.0 to 4.0) of 31 (progress 27) | +89 (+84 to +104) (progress +144) |
| OpenVLA-OFT | 50% | 0.05 | gru_phys | 13.6 (8.0 to 19.0) of 81 | 17 | 1 of 5 (0) | 0.079 (0.014 to 0.304) (progress 0.048) | 3.0 (1.0 to 5.0) of 31 (progress 27) | +102 (+68 to +124) (progress +144) |
| OpenVLA-OFT | 70% | 0.025 | gru_phys_ttp | 19.0 (16.0 to 24.0) of 91 | 13 | 5 of 5 (0) | 0.016 (0.007 to 0.028) (progress 0.025) | 5.2 (4.0 to 7.0) of 35 (progress 25) | +91 (+80 to +96) (progress +156) |
| OpenVLA-OFT | 70% | 0.025 | gru_phys_frac | 20.0 (18.0 to 23.0) of 91 | 13 | 5 of 5 (0) | 0.015 (0.009 to 0.022) (progress 0.025) | 5.6 (4.0 to 8.0) of 35 (progress 25) | +83 (+80 to +88) (progress +156) |
| OpenVLA-OFT | 70% | 0.025 | gru_phys | 17.2 (15.0 to 21.0) of 91 | 13 | 5 of 5 (0) | 0.044 (0.035 to 0.065) (progress 0.025) | 5.8 (4.0 to 7.0) of 35 (progress 25) | +77 (+64 to +92) (progress +156) |
| OpenVLA-OFT | 70% | 0.05 | gru_phys_ttp | 23.8 (22.0 to 26.0) of 91 | 22 | 3 of 5 (2) | 0.030 (0.018 to 0.054) (progress 0.048) | 7.4 (6.0 to 9.0) of 35 (progress 31) | +78 (+72 to +88) (progress +108) |
| OpenVLA-OFT | 70% | 0.05 | gru_phys_frac | 23.8 (21.0 to 27.0) of 91 | 22 | 3 of 5 (1) | 0.036 (0.017 to 0.054) (progress 0.048) | 8.0 (6.0 to 9.0) of 35 (progress 31) | +66 (+56 to +76) (progress +108) |
| OpenVLA-OFT | 70% | 0.05 | gru_phys | 20.0 (18.0 to 22.0) of 91 | 22 | 0 of 5 (1) | 0.070 (0.052 to 0.097) (progress 0.048) | 6.0 (4.0 to 8.0) of 35 (progress 31) | +66 (+52 to +80) (progress +108) |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_ttp | 23.0 (20.0 to 25.0) of 102 | 17 | 5 of 5 (0) | 0.019 (0.012 to 0.031) (progress 0.025) | 8.4 (7.0 to 9.0) of 39 (progress 28) | +67 (+56 to +80) (progress +144) |
| OpenVLA-OFT | 80% | 0.025 | gru_phys_frac | 24.8 (22.0 to 31.0) of 102 | 17 | 5 of 5 (0) | 0.019 (0.015 to 0.028) (progress 0.025) | 8.6 (8.0 to 9.0) of 39 (progress 28) | +58 (+56 to +64) (progress +144) |
| OpenVLA-OFT | 80% | 0.025 | gru_phys | 12.8 (9.0 to 16.0) of 102 | 17 | 0 of 5 (0) | 0.024 (0.005 to 0.050) (progress 0.025) | 5.6 (4.0 to 7.0) of 39 (progress 28) | +90 (+56 to +112) (progress +144) |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_ttp | 27.0 (24.0 to 29.0) of 102 | 29 | 0 of 5 (1) | 0.032 (0.021 to 0.060) (progress 0.048) | 9.2 (8.0 to 10.0) of 39 (progress 35) | +54 (+48 to +68) (progress +96) |
| OpenVLA-OFT | 80% | 0.05 | gru_phys_frac | 29.2 (26.0 to 34.0) of 102 | 29 | 2 of 5 (1) | 0.038 (0.022 to 0.053) (progress 0.048) | 11.4 (11.0 to 12.0) of 39 (progress 35) | +46 (+40 to +48) (progress +96) |
| OpenVLA-OFT | 80% | 0.05 | gru_phys | 15.6 (11.0 to 20.0) of 102 | 29 | 0 of 5 (0) | 0.033 (0.008 to 0.068) (progress 0.048) | 6.0 (5.0 to 7.0) of 39 (progress 35) | +82 (+52 to +104) (progress +96) |
| Pi0.5 | 50% | 0.025 | gru_phys_ttp | 5.4 (2.0 to 8.0) of 27 | 2 | 4 of 5 (1) | 0.006 (0.000 to 0.015) (progress 0.025) | 0.4 (0.0 to 1.0) of 7 (progress 6) | -33 (-104 to +120) (progress +144) |
| Pi0.5 | 50% | 0.025 | gru_phys_frac | 2.6 (1.0 to 6.0) of 27 | 2 | 2 of 5 (0) | 0.001 (0.000 to 0.003) (progress 0.025) | 0.0 (0.0 to 0.0) of 7 (progress 6) | -88 (-120 to -28) (progress +144) |
| Pi0.5 | 50% | 0.025 | gru_phys | 2.2 (1.0 to 3.0) of 27 | 2 | 2 of 5 (2) | 0.013 (0.001 to 0.027) (progress 0.025) | 0.8 (0.0 to 2.0) of 7 (progress 6) | +121 (+40 to +184) (progress +144) |
| Pi0.5 | 50% | 0.05 | gru_phys_ttp | 6.2 (2.0 to 9.0) of 27 | 5 | 3 of 5 (1) | 0.009 (0.005 to 0.018) (progress 0.050) | 0.4 (0.0 to 1.0) of 7 (progress 6) | -52 (-112 to +76) (progress +104) |
| Pi0.5 | 50% | 0.05 | gru_phys_frac | 3.8 (2.0 to 8.0) of 27 | 5 | 1 of 5 (1) | 0.002 (0.000 to 0.005) (progress 0.050) | 0.0 (0.0 to 0.0) of 7 (progress 6) | -104 (-136 to -72) (progress +104) |
| Pi0.5 | 50% | 0.05 | gru_phys | 3.4 (3.0 to 4.0) of 27 | 5 | 0 of 5 (0) | 0.036 (0.006 to 0.073) (progress 0.050) | 1.6 (0.0 to 3.0) of 7 (progress 6) | +78 (+32 to +144) (progress +104) |
| Pi0.5 | 70% | 0.025 | gru_phys_ttp | 5.4 (1.0 to 10.0) of 31 | 6 | 2 of 5 (0) | 0.007 (0.003 to 0.013) (progress 0.025) | 0.4 (0.0 to 1.0) of 7 (progress 6) | -47 (-184 to +144) (progress +136) |
| Pi0.5 | 70% | 0.025 | gru_phys_frac | 3.4 (1.0 to 7.0) of 31 | 6 | 1 of 5 (1) | 0.005 (0.002 to 0.008) (progress 0.025) | 0.0 (0.0 to 0.0) of 7 (progress 6) | -91 (-132 to -32) (progress +136) |
| Pi0.5 | 70% | 0.025 | gru_phys | 2.0 (1.0 to 3.0) of 31 | 6 | 0 of 5 (0) | 0.003 (0.000 to 0.009) (progress 0.025) | 1.0 (1.0 to 1.0) of 7 (progress 6) | +84 (-16 to +184) (progress +136) |
| Pi0.5 | 70% | 0.05 | gru_phys_ttp | 6.2 (2.0 to 10.0) of 31 | 8 | 2 of 5 (0) | 0.010 (0.005 to 0.017) (progress 0.050) | 0.4 (0.0 to 1.0) of 7 (progress 6) | -63 (-208 to +84) (progress +84) |
| Pi0.5 | 70% | 0.05 | gru_phys_frac | 4.0 (2.0 to 7.0) of 31 | 8 | 0 of 5 (0) | 0.008 (0.004 to 0.012) (progress 0.050) | 0.0 (0.0 to 0.0) of 7 (progress 6) | -117 (-168 to -52) (progress +84) |
| Pi0.5 | 70% | 0.05 | gru_phys | 2.2 (1.0 to 3.0) of 31 | 8 | 0 of 5 (0) | 0.006 (0.001 to 0.018) (progress 0.050) | 1.0 (1.0 to 1.0) of 7 (progress 6) | +106 (+44 to +176) (progress +84) |
| Pi0.5 | 80% | 0.025 | gru_phys_ttp | 3.4 (1.0 to 6.0) of 33 | 12 | 0 of 5 (0) | 0.002 (0.000 to 0.005) (progress 0.025) | 0.2 (0.0 to 1.0) of 8 (progress 7) | -82 (-192 to +104) (progress +40) |
| Pi0.5 | 80% | 0.025 | gru_phys_frac | 1.8 (1.0 to 4.0) of 33 | 12 | 0 of 5 (0) | 0.003 (0.001 to 0.005) (progress 0.025) | 0.0 (0.0 to 0.0) of 8 (progress 7) | -77 (-240 to +104) (progress +40) |
| Pi0.5 | 80% | 0.025 | gru_phys | 2.8 (0.0 to 9.0) of 33 | 12 | 0 of 5 (0) | 0.004 (0.000 to 0.009) (progress 0.025) | 0.4 (0.0 to 1.0) of 8 (progress 7) | +5 (-208 to +156) (progress +40) |
| Pi0.5 | 80% | 0.05 | gru_phys_ttp | 3.8 (1.0 to 7.0) of 33 | 17 | 0 of 5 (0) | 0.006 (0.002 to 0.014) (progress 0.050) | 0.2 (0.0 to 1.0) of 8 (progress 7) | -99 (-192 to +64) (progress -28) |
| Pi0.5 | 80% | 0.05 | gru_phys_frac | 2.8 (1.0 to 5.0) of 33 | 17 | 0 of 5 (0) | 0.006 (0.002 to 0.015) (progress 0.050) | 0.0 (0.0 to 0.0) of 8 (progress 7) | -140 (-208 to +16) (progress -28) |
| Pi0.5 | 80% | 0.05 | gru_phys | 3.0 (0.0 to 9.0) of 33 | 17 | 0 of 5 (0) | 0.008 (0.001 to 0.018) (progress 0.050) | 0.6 (0.0 to 1.0) of 8 (progress 7) | +22 (-208 to +144) (progress -28) |
