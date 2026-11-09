# Fresh Pi0.5 test (plan_nov06.md, Nov 7 addition (c))

Models and thresholds come from the old Pi0.5 episodes only (natural + perturbed 2 to 3 cm seeds 0 and 1, gate-passed tasks); they are scored
only on the new perturbed episodes of seeds 2 to 4 (gate-passed folders). unseen = the new episodes of the held-out task (leave one task out);
seen = all new episodes, models trained on every old task. Models: progress, gru_phys_ttp seeds 0 to 4, the seed ensemble gru_phys_ttp_ens and
or_progress_ens (50_ensemble.py). Same recipe, rules (50 / 70 / 80%) and budgets (2.5%, 5%); no tuning. Not merged into any older table.

Left out: data/pi05/perturbed/task05_s3 (13 episodes; its index.csv lost the header after a reqp requeue and the folder has no replay gate),
and the gate-failed folders task04_s3, task05_s2, task05_s4. New failures with neither a scan nor a pre-check verdict of recoverable have no
label and are not scored (the scan chain stopped at 70 scanned failures, during seed 4).

Files: thr{T}_{unseen,seen}_report_fixed_{0.05,0.025}.md (13_report.py), thr{T}_{split}_alarms.md (46_paired_alarms.py), extra.md (task
bootstrap and rescue value, 58_fresh_extra.py).
