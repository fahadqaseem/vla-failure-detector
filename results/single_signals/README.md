# Add-one-signal analysis (Fahad, Nov 12, 2026)

gru_phys_ttp trained on ONE physical signal group alone (06 `--phys_keep`), and each of these OR the progress rule (47_combo.py: one common
conformal level for both parts, set on the training-task successes so the union stays within the budget). 70% rule, unseen tasks
(leave-one-task-out), seed 0, OpenVLA-OFT (`oft_*`) and Pi0.5 (`pi05_*`), budgets 5% and 2.5%.

Groups (columns of data/physical, every goal slot):
- goal: goal_dist, in_goal
- pose (object pose): pos_x, pos_y, pos_z, dz, lifted, tilt
- contact: contact (obj1, obj2, articulated object)
- gripper: dist, ddist (gripper to object), grip_open

"Alone" means only these columns: the slot `used` flags, `art_true` and eef position are left out too.
Progress and gru_phys_ttp with all groups are rerun in the same jobs, so every row has the same episodes and calibration successes.

Models in the reports: progress, gru_phys_ttp (all groups), or_progress_ttp (all groups OR progress), ttp_{group}_only, or_progress_{group}_only.
Files: `{pol}_thr70_report_fixed_{0.05,0.025}.md` (timely, false alarms, vs progress), `{pol}_thr70_alarms.md`, `{pol}_thr70_levels_{group}.txt`.
Made by slurm/n12_single_submit.sh and slurm/n12_single_report.sbatch (logged in results/LOG.md).
