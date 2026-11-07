# FailureSpot methods vs gru_phys on our data

Timely of failures with t_pnr > 0; false alarms natural / perturbed successes; unnecessary = alarms on recoverable failures; window = median t_alarm - t_pnr over alarmed failures (negative = before t_pnr). AUROC: FailureSpot's metrics, labels 1 from t_pnr on. Natural and perturbed pooled (7 of 10 tasks perturbed, perturbed_v2 tasks 0, 1, 4, 7). own = its split, seeds 0 to 2, unseen tasks, mean; loto = leave one task out, pooled. Evaluated on held-out episodes of tasks 0, 1, 4, 5, 6, 7 only (failures and successes).

| split | model | timestamp AUROC | trajectory AUROC | timely 0.05 | false alarms 0.05 | unnecessary 0.05 | window 0.05 | timely 0.025 | false alarms 0.025 | unnecessary 0.025 | window 0.025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| loto | failurespot_mlp | 0.406 | 0.647 | 0 of 27 | 0.000 / 0.004 | 0 of 7 | +nan | 0 of 27 | 0.000 / 0.002 | 0 of 7 | +nan |
| loto | failurespot_lstm | 0.579 | 0.635 | 0 of 27 | 0.024 / 0.013 | 2 of 7 | +144 | 0 of 27 | 0.017 / 0.011 | 1 of 7 | +112 |
| loto | safe_mlp | 0.754 | 0.866 | 7 of 27 | 0.058 / 0.088 | 4 of 7 | +104 | 5 of 27 | 0.034 / 0.071 | 1 of 7 | +144 |
| loto | safe_lstm | 0.555 | 0.610 | 1 of 27 | 0.027 / 0.042 | 1 of 7 | +272 | 1 of 27 | 0.021 / 0.018 | 1 of 7 | +376 |
| loto | supervised_random_mlp | 0.706 | 0.749 | 2 of 27 | 0.055 / 0.044 | 5 of 7 | +4 | 1 of 27 | 0.017 / 0.018 | 3 of 7 | +200 |
| loto | supervised_random_lstm | 0.516 | 0.546 | 1 of 27 | 0.000 / 0.002 | 0 of 7 | +208 | 1 of 27 | 0.000 / 0.002 | 0 of 7 | -24 |
| loto | actprobe_mlp | 0.830 | 0.949 | 8 of 27 | 0.034 / 0.075 | 7 of 7 | +40 | 5 of 27 | 0.017 / 0.038 | 6 of 7 | +136 |
| loto | actprobe_lstm | 0.815 | 0.993 | 8 of 27 | 0.045 / 0.055 | 7 of 7 | +24 | 5 of 27 | 0.021 / 0.024 | 7 of 7 | +96 |
| loto | logpzo | 0.458 | 0.439 | 2 of 27 | 0.186 / 0.159 | 0 of 7 | +0 | 0 of 27 | 0.052 / 0.035 | 0 of 7 | +nan |
| loto | gru_phys (ours) | 0.743 | 0.846 | 3 of 27 | 0.010 / 0.024 | 1 of 7 | +72 | 3 of 27 | 0.003 / 0.015 | 1 of 7 | +128 |
| loto | gru_phys_ttp (ours) | 0.763 | 0.813 | 9 of 27 | 0.010 / 0.011 | 1 of 7 | -96 | 8 of 27 | 0.007 / 0.007 | 1 of 7 | -64 |
| own | failurespot_mlp | 0.401 | 0.488 | 3 of 16.7 | 0.294 / 0.297 | 1.33 of 2.67 | -136 | 2.33 of 16.7 | 0.267 / 0.276 | 0.667 of 2.67 | -176 |
| own | failurespot_lstm | 0.487 | 0.653 | 2.33 of 16.7 | 0.236 / 0.224 | 2 of 2.67 | -28 | 2.33 of 16.7 | 0.214 / 0.203 | 2 of 2.67 | -56 |
| own | safe_mlp | 0.752 | 0.815 | 1.67 of 16.7 | 0.039 / 0.046 | 0 of 2.67 | +208 | 0.667 of 16.7 | 0.026 / 0.022 | 0 of 2.67 | +120 |
| own | safe_lstm | 0.442 | 0.599 | 1.67 of 16.7 | 0.089 / 0.113 | 1.33 of 2.67 | +20 | 0.333 of 16.7 | 0.050 / 0.048 | 1.33 of 2.67 | -24 |
| own | supervised_random_mlp | 0.594 | 0.530 | 2.33 of 16.7 | 0.208 / 0.177 | 0.333 of 2.67 | +24 | 0.333 of 16.7 | 0.106 / 0.067 | 0 of 2.67 | +130 |
| own | supervised_random_lstm | 0.447 | 0.640 | 6 of 16.7 | 0.273 / 0.247 | 0.667 of 2.67 | +16 | 0 of 16.7 | 0.000 / 0.000 | 0 of 2.67 | +80 |
| own | actprobe_mlp | 0.866 | 0.965 | 3.67 of 16.7 | 0.034 / 0.059 | 2.33 of 2.67 | +104 | 0.667 of 16.7 | 0.002 / 0.022 | 0.667 of 2.67 | +219 |
| own | actprobe_lstm | 0.857 | 0.974 | 3.67 of 16.7 | 0.019 / 0.056 | 1 of 2.67 | +76 | 0.667 of 16.7 | 0.007 / 0.018 | 0.333 of 2.67 | +189 |
| own | logpzo | 0.476 | 0.456 | 14.7 of 16.7 | 0.914 / 0.872 | 1.67 of 2.67 | -181 | 14 of 16.7 | 0.870 / 0.805 | 1.33 of 2.67 | -153 |
