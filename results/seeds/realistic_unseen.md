# Seeds 0 to 4, unseen tasks

Seed spread (Fahad, Nov 6, results/plan_nov06.md item 2): gru_phys, gru_phys_frac, gru_phys_ttp with seeds 0 to 4, both policies, three failure rules, unseen and seen tasks. Seed 0 = the runs of results/week3/regression and results/pi05/regression; seeds 1 to 4 = data/seeds/{policy}/thr{T}/{split}/s{S}/{model} (28_merge_groups.py already run). Per setting: mean and min to max over the 5 seeds of timely (alarm at or before t_pnr, failures with t_pnr > 0), false alarms on successes, unnecessary alarms on recoverable failures and median window t_alarm - t_pnr, and how many seeds beat progress (more timely alarms at the same budget; ties counted apart). Progress has no seed.

| policy | rule | budget | model | timely mean (min to max) | progress timely | seeds beating progress (ties) | false alarms | unnecessary | window |
|---|---|---|---|---|---|---|---|---|---|
| OpenVLA-OFT | 50% | 0.025 | gru_robotcontact_ttp | 5.2 (5.0 to 6.0) of 81 | 11 | 0 of 5 (0) | 0.007 (0.005 to 0.007) (progress 0.025) | 4.2 (2.0 to 6.0) of 31 (progress 22) | +183 (+172 to +192) (progress +200) |
| OpenVLA-OFT | 50% | 0.025 | gru_robot_ttp | 3.0 (1.0 to 6.0) of 81 | 11 | 0 of 5 (0) | 0.015 (0.003 to 0.033) (progress 0.025) | 1.2 (0.0 to 2.0) of 31 (progress 22) | +202 (+176 to +232) (progress +200) |
| OpenVLA-OFT | 50% | 0.05 | gru_robotcontact_ttp | 6.8 (6.0 to 7.0) of 81 | 17 | 0 of 5 (0) | 0.010 (0.007 to 0.011) (progress 0.048) | 5.6 (5.0 to 6.0) of 31 (progress 27) | +172 (+160 to +200) (progress +144) |
| OpenVLA-OFT | 50% | 0.05 | gru_robot_ttp | 4.4 (2.0 to 7.0) of 81 | 17 | 0 of 5 (0) | 0.027 (0.017 to 0.053) (progress 0.048) | 1.4 (0.0 to 2.0) of 31 (progress 27) | +181 (+136 to +208) (progress +144) |
| OpenVLA-OFT | 80% | 0.025 | gru_robotcontact_ttp | 17.0 (16.0 to 18.0) of 102 | 17 | 2 of 5 (1) | 0.007 (0.006 to 0.008) (progress 0.025) | 9.2 (9.0 to 10.0) of 39 (progress 28) | +80 (+64 to +96) (progress +144) |
| OpenVLA-OFT | 80% | 0.025 | gru_robot_ttp | 6.8 (5.0 to 10.0) of 102 | 17 | 0 of 5 (0) | 0.004 (0.002 to 0.007) (progress 0.025) | 3.0 (1.0 to 4.0) of 39 (progress 28) | +156 (+112 to +184) (progress +144) |
| OpenVLA-OFT | 80% | 0.05 | gru_robotcontact_ttp | 20.2 (19.0 to 21.0) of 102 | 29 | 0 of 5 (0) | 0.010 (0.007 to 0.014) (progress 0.048) | 9.6 (9.0 to 10.0) of 39 (progress 35) | +66 (+56 to +72) (progress +96) |
| OpenVLA-OFT | 80% | 0.05 | gru_robot_ttp | 10.2 (7.0 to 12.0) of 102 | 29 | 0 of 5 (0) | 0.010 (0.004 to 0.021) (progress 0.048) | 4.6 (3.0 to 7.0) of 39 (progress 35) | +123 (+100 to +152) (progress +96) |
| Pi0.5 | 50% | 0.025 | gru_robotcontact_ttp | 1.0 (1.0 to 1.0) of 27 | 2 | 0 of 5 (0) | 0.032 (0.008 to 0.051) (progress 0.025) | 0.6 (0.0 to 1.0) of 7 (progress 6) | +175 (+148 to +216) (progress +144) |
| Pi0.5 | 50% | 0.025 | gru_robot_ttp | 1.0 (1.0 to 1.0) of 27 | 2 | 0 of 5 (0) | 0.046 (0.019 to 0.057) (progress 0.025) | 0.2 (0.0 to 1.0) of 7 (progress 6) | +158 (+120 to +208) (progress +144) |
| Pi0.5 | 50% | 0.05 | gru_robotcontact_ttp | 1.4 (1.0 to 2.0) of 27 | 5 | 0 of 5 (0) | 0.050 (0.025 to 0.066) (progress 0.050) | 1.0 (1.0 to 1.0) of 7 (progress 6) | +120 (+96 to +160) (progress +104) |
| Pi0.5 | 50% | 0.05 | gru_robot_ttp | 1.4 (1.0 to 3.0) of 27 | 5 | 0 of 5 (0) | 0.057 (0.050 to 0.065) (progress 0.050) | 0.6 (0.0 to 1.0) of 7 (progress 6) | +159 (+120 to +208) (progress +104) |
| Pi0.5 | 80% | 0.025 | gru_robotcontact_ttp | 3.2 (2.0 to 5.0) of 33 | 12 | 0 of 5 (0) | 0.012 (0.006 to 0.018) (progress 0.025) | 0.2 (0.0 to 1.0) of 8 (progress 7) | +114 (+56 to +152) (progress +40) |
| Pi0.5 | 80% | 0.025 | gru_robot_ttp | 3.2 (2.0 to 4.0) of 33 | 12 | 0 of 5 (0) | 0.056 (0.044 to 0.066) (progress 0.025) | 0.2 (0.0 to 1.0) of 8 (progress 7) | +84 (+76 to +88) (progress +40) |
| Pi0.5 | 80% | 0.05 | gru_robotcontact_ttp | 3.4 (3.0 to 5.0) of 33 | 17 | 0 of 5 (0) | 0.033 (0.018 to 0.061) (progress 0.050) | 0.4 (0.0 to 1.0) of 8 (progress 7) | +99 (+68 to +136) (progress -28) |
| Pi0.5 | 80% | 0.05 | gru_robot_ttp | 4.2 (3.0 to 5.0) of 33 | 17 | 0 of 5 (0) | 0.068 (0.064 to 0.071) (progress 0.050) | 0.2 (0.0 to 1.0) of 8 (progress 7) | +77 (+64 to +88) (progress -28) |
