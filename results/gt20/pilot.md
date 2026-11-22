# 20-replay ground truth, pilot (plan: results/plan_nov22_gt20.md, Step 3)

OpenVLA-OFT, checkpoints every 16 steps, K 20 (seed 0 scan replays and seed 1 refinement replays reused where present, new replays seed 20), noise 0.05, extra_steps 200. K 8 and K 4 = random subsets of the 20 (10 draws each, rng 22). Original K 4 = the 4 seed-0 replays of the existing scan. Failure fraction = 1 - successes / K.

## Change of the truth vs K 20 (mean absolute difference of the failure fraction over checkpoints and draws)

| run | checkpoints | K 4 subsets | K 8 subsets | original K 4 (seed 0) | t_pnr 50%: K 4 every 8 (scan) | K 20 every 16 |
|---|---|---|---|---|---|---|
| t00_e06_p0_s1 | 33 | 0.136 | 0.084 | 0.148 | 344 | 352 |
| t01_e07_p0_s1 | 33 | 0.042 | 0.019 | 0.038 | 120 | 128 |
| t04_e00_p0_s2 | 33 | 0.020 | 0.013 | 0.020 | 40 | 48 |
| all | 99 | 0.066 | 0.039 | 0.069 |  |  |

Runs with checkpoints still missing or not started: none; checkpoints done per run: t00_e06_p0_s1 33, t01_e07_p0_s1 33, t04_e00_p0_s2 33.

## Seed 0 model predictions (data/regression_v2, unseen task) vs the K 4 and K 20 truth, pilot checkpoints

MSE over the checkpoints every 16 steps of the pilot runs (pooled; per run in brackets: t00_e06_p0_s1, t01_e07_p0_s1, t04_e00_p0_s2). K 4 = original seed 0 scan replays. Noise floor = mean f(1 - f) / (K - 1) of that truth.

| model | MSE vs K 4 truth | MSE vs K 20 truth |
|---|---|---|
| gru_phys_frac | 0.3100 (0.201, 0.073, 0.656) | 0.2973 (0.192, 0.050, 0.650) |
| safe_lin | 0.1423 (0.203, 0.195, 0.029) | 0.1150 (0.158, 0.160, 0.027) |
| safe_mlp | 0.1191 (0.190, 0.044, 0.124) | 0.1035 (0.162, 0.030, 0.119) |
| safe_lstm | 0.2283 (0.491, 0.150, 0.043) | 0.2168 (0.493, 0.121, 0.036) |
| gru_physvla_frac | 0.2398 (0.278, 0.119, 0.323) | 0.2213 (0.256, 0.092, 0.317) |
| const | 0.6052 (0.447, 0.594, 0.774) | 0.6063 (0.447, 0.605, 0.767) |
| progress_iso | 0.3886 (0.433, 0.236, 0.497) | 0.3838 (0.435, 0.227, 0.490) |
| timer_iso | 0.3440 (0.230, 0.302, 0.501) | 0.3408 (0.212, 0.317, 0.493) |
| noise floor | 0.0204 | 0.0040 |

Slide redraw: plots/slide_t00_e06_p0_s1_K20.png. Per run truth curves: plots/truth_K_<run>.png.
