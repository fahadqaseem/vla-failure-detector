# FailureSpot methods vs gru_phys on our data

Timely of failures with t_pnr > 0; false alarms natural / perturbed successes; unnecessary = alarms on recoverable failures; window = median t_alarm - t_pnr over alarmed failures (negative = before t_pnr). AUROC: FailureSpot's metrics, labels 1 from t_pnr on. Natural and perturbed pooled (7 of 10 tasks perturbed, perturbed_v2 tasks 0, 1, 4, 7). own = its split, seeds 0 to 2, unseen tasks, mean; loto = leave one task out, pooled.

| split | model | timestamp AUROC | trajectory AUROC | timely 0.05 | false alarms 0.05 | unnecessary 0.05 | window 0.05 | timely 0.025 | false alarms 0.025 | unnecessary 0.025 | window 0.025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| loto | failurespot_mlp | 0.384 | 0.584 | 0 of 27 | 0.088 / 0.004 | 0 of 7 | n/a | 0 of 27 | 0.051 / 0.002 | 0 of 7 | n/a |
| loto | failurespot_lstm | 0.539 | 0.619 | 0 of 27 | 0.029 / 0.013 | 2 of 7 | +144 | 0 of 27 | 0.013 / 0.011 | 1 of 7 | +112 |
| loto | safe_mlp | 0.765 | 0.873 | 7 of 27 | 0.040 / 0.088 | 4 of 7 | +104 | 5 of 27 | 0.021 / 0.071 | 1 of 7 | +144 |
| loto | safe_lstm | 0.570 | 0.629 | 1 of 27 | 0.109 / 0.042 | 1 of 7 | +272 | 1 of 27 | 0.021 / 0.018 | 1 of 7 | +376 |
| loto | supervised_random_mlp | 0.717 | 0.766 | 2 of 27 | 0.036 / 0.044 | 5 of 7 | +4 | 1 of 27 | 0.011 / 0.018 | 3 of 7 | +200 |
| loto | supervised_random_lstm | 0.496 | 0.573 | 1 of 27 | 0.000 / 0.002 | 0 of 7 | +208 | 1 of 27 | 0.000 / 0.002 | 0 of 7 | -24 |
| loto | actprobe_mlp | 0.820 | 0.948 | 8 of 27 | 0.036 / 0.075 | 7 of 7 | +40 | 5 of 27 | 0.015 / 0.038 | 6 of 7 | +136 |
| loto | actprobe_lstm | 0.815 | 0.993 | 8 of 27 | 0.032 / 0.055 | 7 of 7 | +24 | 5 of 27 | 0.015 / 0.024 | 7 of 7 | +96 |
| loto | logpzo | 0.513 | 0.472 | 2 of 27 | 0.213 / 0.159 | 0 of 7 | +0 | 0 of 27 | 0.131 / 0.035 | 0 of 7 | n/a |
| loto | gru_phys (ours) | 0.773 | 0.873 | 3 of 27 | 0.006 / 0.024 | 1 of 7 | +72 | 3 of 27 | 0.002 / 0.015 | 1 of 7 | +128 |
| loto | gru_phys_ttp (ours) | 0.795 | 0.844 | 9 of 27 | 0.006 / 0.011 | 1 of 7 | -96 | 8 of 27 | 0.004 / 0.007 | 1 of 7 | -64 |
| own | failurespot_mlp | 0.418 | 0.442 | 3 of 16.7 | 0.344 / 0.297 | 1.33 of 2.67 | -136 | 2.33 of 16.7 | 0.321 / 0.276 | 0.667 of 2.67 | -176 |
| own | failurespot_lstm | 0.501 | 0.639 | 2.33 of 16.7 | 0.324 / 0.224 | 2 of 2.67 | -28 | 2.33 of 16.7 | 0.311 / 0.203 | 2 of 2.67 | -56 |
| own | safe_mlp | 0.755 | 0.808 | 1.67 of 16.7 | 0.046 / 0.046 | 0 of 2.67 | +208 | 0.667 of 16.7 | 0.021 / 0.022 | 0 of 2.67 | +120 |
| own | safe_lstm | 0.441 | 0.555 | 1.67 of 16.7 | 0.132 / 0.113 | 1.33 of 2.67 | +20 | 0.333 of 16.7 | 0.086 / 0.048 | 1.33 of 2.67 | -24 |
| own | supervised_random_mlp | 0.589 | 0.514 | 2.33 of 16.7 | 0.152 / 0.177 | 0.333 of 2.67 | +24 | 0.333 of 16.7 | 0.063 / 0.067 | 0 of 2.67 | +130 |
| own | supervised_random_lstm | 0.448 | 0.588 | 6 of 16.7 | 0.327 / 0.247 | 0.667 of 2.67 | +16 | 0 of 16.7 | 0.006 / 0.000 | 0 of 2.67 | +80 |
| own | actprobe_mlp | 0.863 | 0.965 | 3.67 of 16.7 | 0.036 / 0.059 | 2.33 of 2.67 | +104 | 0.667 of 16.7 | 0.004 / 0.022 | 0.667 of 2.67 | +219 |
| own | actprobe_lstm | 0.851 | 0.965 | 3.67 of 16.7 | 0.058 / 0.056 | 1 of 2.67 | +76 | 0.667 of 16.7 | 0.029 / 0.018 | 0.333 of 2.67 | +189 |
| own | logpzo | 0.488 | 0.405 | 14.7 of 16.7 | 0.942 / 0.872 | 1.67 of 2.67 | -181 | 14 of 16.7 | 0.911 / 0.805 | 1.33 of 2.67 | -153 |

## Per task: replay gate and the 50-step chunk check

41_pi_chunks.py replays the recorded actions and asks the policy again with each query's flow seed; difference = max |recovered first 8 actions - recorded actions| per query (0 = chunk reproduced). Tasks whose natural gate failed (2, 3, 8, 9) may not reproduce.

| task | natural gate | held-out episodes (progress rows) | failures with t_pnr > 0 | chunk queries | median difference | max difference |
|---|---|---|---|---|---|---|
| 0 | pass | 144 | 2 | 5230 | 0.0000 | 2.0057 |
| 1 | pass | 150 | 4 | 447 | 0.0017 | 2.0018 |
| 2 | FAIL | 50 | 0 | 3213 | 0.0834 | 2.0147 |
| 3 | FAIL | 50 | 0 | 3008 | 0.0463 | 2.0137 |
| 4 | pass | 150 | 4 | 4606 | 0.0000 | 0.0053 |
| 5 | pass | 100 | 0 | 3546 | 0.0138 | 1.9993 |
| 6 | pass | 144 | 13 | 4934 | 0.0000 | 0.0000 |
| 7 | pass | 100 | 4 | 3299 | 0.0000 | 2.0126 |
| 8 | FAIL | 37 | 0 | 5484 | 0.0225 | 2.0121 |
| 9 | FAIL | 47 | 0 | 3525 | 0.0367 | 2.0347 |
