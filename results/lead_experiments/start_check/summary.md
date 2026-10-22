# Start-of-run check: doomed from step 0, from the first query only, leave-one-task-out (results/predictor_with_perturbed)

Natural and perturbed-natural (7 of 10 tasks) pooled. Threshold: conformal 5% on cross-fitted training-task successes.

| model | AUROC doomed vs rest | AUROC doomed vs successes | doomed caught | natural / perturbed caught | false alarms on successes | alarms on other failures |
|---|---|---|---|---|---|---|
| logreg | 0.537 | 0.539 | 1 of 28 | 0 of 3 / 1 of 25 | 25 of 743 (0.034) | 2 of 73 |
| mlp | 0.640 | 0.641 | 1 of 28 | 0 of 3 / 1 of 25 | 36 of 743 (0.048) | 6 of 73 |
