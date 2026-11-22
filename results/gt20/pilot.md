# 20-replay ground truth, pilot (plan: results/plan_nov22_gt20.md, Step 3)

OpenVLA-OFT, checkpoints every 16 steps, K 20 (seed 0 scan replays and seed 1 refinement replays reused where present, new replays seed 20), noise 0.05, extra_steps 200. K 8 and K 4 = random subsets of the 20 (10 draws each, rng 22). Original K 4 = the 4 seed-0 replays of the existing scan. Failure fraction = 1 - successes / K.

## Change of the truth vs K 20 (mean absolute difference of the failure fraction over checkpoints and draws)

| run | checkpoints | K 4 subsets | K 8 subsets | original K 4 (seed 0) | t_pnr 50%: K 4 every 8 (scan) | K 20 every 16 |
|---|---|---|---|---|---|---|
| t00_e06_p0_s1 | 33 | 0.136 | 0.084 | 0.148 | 344 | 352 |
| t01_e07_p0_s1 | 33 | 0.042 | 0.019 | 0.038 | 120 | 128 |
| t04_e00_p0_s2 | 31 | 0.022 | 0.013 | 0.021 | 40 | 48 |
| all | 97 | 0.068 | 0.040 | 0.070 |  |  |

Runs with checkpoints still missing or not started: none; checkpoints done per run: t00_e06_p0_s1 33, t01_e07_p0_s1 33, t04_e00_p0_s2 31.

## Seed 0 model predictions (data/regression_v2, unseen task) vs the K 4 and K 20 truth, pilot checkpoints

MSE over the checkpoints every 16 steps of the pilot runs (pooled; per run in brackets: t00_e06_p0_s1, t01_e07_p0_s1, t04_e00_p0_s2). K 4 = original seed 0 scan replays. Noise floor = mean f(1 - f) / (K - 1) of that truth.

| model | MSE vs K 4 truth | MSE vs K 20 truth |
|---|---|---|
| gru_phys_frac | 0.3113 (0.201, 0.073, 0.683) | 0.2983 (0.192, 0.050, 0.676) |
| safe_lin | 0.1452 (0.203, 0.195, 0.030) | 0.1174 (0.158, 0.160, 0.028) |
| safe_mlp | 0.1215 (0.190, 0.044, 0.132) | 0.1057 (0.162, 0.030, 0.127) |
| safe_lstm | 0.2329 (0.491, 0.150, 0.045) | 0.2212 (0.493, 0.121, 0.038) |
| gru_physvla_frac | 0.2397 (0.278, 0.119, 0.328) | 0.2208 (0.256, 0.092, 0.321) |
| const | 0.6005 (0.447, 0.594, 0.771) | 0.6016 (0.447, 0.605, 0.763) |
| progress_iso | 0.3958 (0.433, 0.236, 0.526) | 0.3909 (0.435, 0.227, 0.519) |
| timer_iso | 0.3511 (0.230, 0.302, 0.533) | 0.3478 (0.212, 0.317, 0.525) |
| noise floor | 0.0208 | 0.0041 |

Slide redraw: plots/slide_t00_e06_p0_s1_K20.png. Per run truth curves: plots/truth_K_<run>.png.
