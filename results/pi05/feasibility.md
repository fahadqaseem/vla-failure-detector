# pi05 feasibility: 20 natural episodes per LIBERO-10 task (initial states 0-19)

| task | episodes | successes | rate |
|---|---|---|---|
| 0 | 20 | 19 | 95% |
| 1 | 20 | 20 | 100% |
| 2 | 20 | 20 | 100% |
| 3 | 20 | 20 | 100% |
| 4 | 20 | 20 | 100% |
| 5 | 20 | 20 | 100% |
| 6 | 20 | 20 | 100% |
| 7 | 20 | 18 | 90% |
| 8 | 20 | 12 | 60% |
| 9 | 20 | 19 | 95% |

Overall: 188 of 200 = 94.0% (Wilson 95% 89.8 to 96.5); reference 92.4 (openpi pi05_libero; LeRobot reports 96.0 for its port). Rule: within 10 points and at least 190 episodes. Verdict: PASS.
Checks (22_pi_checks.py): {"policy": "pi05", "checkpoint": "lerobot/pi05_libero_finetuned_v044", "episode_success": true, "episode_steps": 292, "queries": 37, "features_shape": [37, 10, 1024], "model_load_s": 90.3, "episode_s": 24.6, "s_per_query": 0.665, "replay_same_seed_max_eef_dev_m": 8.881784197001252e-16, "replay_gate_pass_10mm": true, "two_new_seeds_max_eef_diff_m": 0.03239889704998275, "new_seeds_differ_1mm": true}
