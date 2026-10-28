# pi0 feasibility: 20 natural episodes per LIBERO-10 task (initial states 0-19)

| task | episodes | successes | rate |
|---|---|---|---|
| 0 | 20 | 4 | 20% |
| 1 | 20 | 9 | 45% |
| 2 | 20 | 15 | 75% |
| 3 | 20 | 14 | 70% |
| 4 | 20 | 4 | 20% |
| 5 | 20 | 13 | 65% |
| 6 | 20 | 6 | 30% |
| 7 | 20 | 6 | 30% |
| 8 | 20 | 2 | 10% |
| 9 | 20 | 11 | 55% |

Overall: 84 of 200 = 42.0% (Wilson 95% 35.4 to 48.9); reference 85.2 (openpi README, pi0 @ 30k finetuned). Rule: within 10 points and at least 190 episodes. Verdict: FAIL.
Checks (22_pi_checks.py): {"policy": "pi0", "checkpoint": "lerobot/pi0_libero_finetuned_v044", "episode_success": false, "episode_steps": 520, "queries": 65, "features_shape": [65, 10, 1024], "model_load_s": 85.7, "episode_s": 33.0, "s_per_query": 0.508, "replay_same_seed_max_eef_dev_m": 0.00015598598999999602, "replay_gate_pass_10mm": true, "two_new_seeds_max_eef_diff_m": 0.1988453257767911, "new_seeds_differ_1mm": true}
