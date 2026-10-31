# FailureSpot methods vs gru_phys on our data

Timely of failures with t_pnr > 0; false alarms natural / perturbed successes; unnecessary = alarms on recoverable failures; window = median t_alarm - t_pnr over alarmed failures (negative = before t_pnr). AUROC: FailureSpot's metrics, labels 1 from t_pnr on. Natural and perturbed pooled (7 of 10 tasks perturbed, perturbed_v2 tasks 0, 1, 4, 7). own = its split, seeds 0 to 2, unseen tasks, mean; loto = leave one task out, pooled.

| split | model | timestamp AUROC | trajectory AUROC | timely 0.05 | false alarms 0.05 | unnecessary 0.05 | window 0.05 | timely 0.025 | false alarms 0.025 | unnecessary 0.025 | window 0.025 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| loto | failurespot_mlp | 0.611 | 0.550 | 0 of 81 | 0.059 / 0.000 | 0 of 31 | +88 | 0 of 81 | 0.034 / 0.000 | 0 of 31 | +88 |
| loto | failurespot_lstm | 0.621 | 0.611 | 0 of 81 | 0.000 / 0.000 | 0 of 31 | +nan | 0 of 81 | 0.000 / 0.000 | 0 of 31 | +nan |
| loto | safe_mlp | 0.788 | 0.891 | 22 of 81 | 0.110 / 0.235 | 9 of 31 | +64 | 21 of 81 | 0.104 / 0.227 | 9 of 31 | +40 |
| loto | safe_lstm | 0.743 | 0.624 | 8 of 81 | 0.025 / 0.137 | 4 of 31 | +4 | 0 of 81 | 0.000 / 0.000 | 0 of 31 | +nan |
| loto | supervised_random_mlp | 0.757 | 0.841 | 25 of 81 | 0.112 / 0.244 | 8 of 31 | +48 | 22 of 81 | 0.106 / 0.239 | 5 of 31 | +48 |
| loto | supervised_random_lstm | 0.767 | 0.732 | 18 of 81 | 0.055 / 0.160 | 5 of 31 | +24 | 14 of 81 | 0.044 / 0.110 | 5 of 31 | +76 |
| loto | actprobe_mlp | 0.723 | 0.549 | 9 of 81 | 0.023 / 0.013 | 8 of 31 | +120 | 9 of 81 | 0.023 / 0.013 | 8 of 31 | +120 |
| loto | actprobe_lstm | 0.757 | 0.964 | 16 of 81 | 0.138 / 0.255 | 26 of 31 | +136 | 13 of 81 | 0.129 / 0.247 | 25 of 31 | +152 |
| loto | gru_phys (ours) | 0.879 | 0.860 | 12 of 81 | 0.000 / 0.025 | 2 of 31 | +112 | 10 of 81 | 0.000 / 0.025 | 2 of 31 | +136 |
| own | failurespot_mlp | 0.618 | 0.596 | 6.67 of 50 | 0.157 / 0.173 | 3 of 22.7 | +75 | 5 of 50 | 0.104 / 0.135 | 2 of 22.7 | +93 |
| own | failurespot_lstm | 0.277 | 0.482 | 2.33 of 50 | 0.099 / 0.098 | 2.67 of 22.7 | -153 | 1.67 of 50 | 0.050 / 0.037 | 0.667 of 22.7 | +nan |
| own | safe_mlp | 0.817 | 0.879 | 13 of 50 | 0.082 / 0.158 | 8 of 22.7 | +64 | 10.3 of 50 | 0.060 / 0.128 | 4.67 of 22.7 | +76 |
| own | safe_lstm | 0.703 | 0.739 | 2.33 of 50 | 0.071 / 0.047 | 4 of 22.7 | +252 | 1.33 of 50 | 0.031 / 0.020 | 3 of 22.7 | +272 |
| own | supervised_random_mlp | 0.844 | 0.883 | 16.3 of 50 | 0.173 / 0.242 | 11.3 of 22.7 | +35 | 5.67 of 50 | 0.016 / 0.047 | 6.33 of 22.7 | +76 |
| own | supervised_random_lstm | 0.763 | 0.734 | 2.33 of 50 | 0.052 / 0.033 | 4.67 of 22.7 | +107 | 1.67 of 50 | 0.004 / 0.009 | 3.33 of 22.7 | +109 |
| own | actprobe_mlp | 0.701 | 0.473 | 0.667 of 50 | 0.047 / 0.024 | 0 of 22.7 | -131 | 0.333 of 50 | 0.029 / 0.012 | 0 of 22.7 | +nan |
| own | actprobe_lstm | 0.772 | 0.983 | 10 of 50 | 0.159 / 0.094 | 22.3 of 22.7 | +129 | 9 of 50 | 0.125 / 0.070 | 22 of 22.7 | +143 |
