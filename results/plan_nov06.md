# Pre-registered plan, Nov 6, 2026 (written and pushed before any job of this plan started)

Goal: solid, repeatable results. Every setting below is reported, whether the main model wins or loses.

## Fixed before the runs

- Main model: `gru_phys_ttp` (GRU on physical signals, target 1 - min(steps until t_pnr, 200) / 200; alarm on the output).
- Main comparison: `gru_phys_ttp` vs `progress` (steps since progress), unseen tasks (leave one task out), false-alarm budgets 2.5% and 5%,
  all three failure rules (50% = Jeffreys tau 0.5, 70% = 3 of 4 replays fail, 80% = 4 of 4 fail), both policies (OpenVLA-OFT, Pi0.5).
- Data: OpenVLA-OFT = natural + perturbed (7 of 10 tasks) + perturbed_v2 (tasks 0, 1, 4, 7), refined labels, as results/week3/regression.
  Pi0.5 = natural + perturbed 2 to 3 cm seeds 0 and 1, gate-passed tasks, as results/pi05/regression.
- Thresholds: fixed conformal on cross-fitted training-task successes (unchanged). Metrics as 13_report.py: timely (alarm at or before t_pnr,
  failures with t_pnr > 0), false alarms on successes, unnecessary alarms on recoverable failures, median window t_alarm - t_pnr.
- Intervals: paired bootstrap vs progress, 10000 draws, seed 0.
- Seen tasks (5 episode folds) are reported as a diagnostic, never the headline.

## Items

1. FailureSpot on Pi0.5 rerun (GPU): chunks for every task, a check that all 10 tasks' chunk files exist before convert, then the methods and
   the report -> results/pi05/failurespot/.
2. Seeds (CPU): gru_phys, gru_phys_frac, gru_phys_ttp with seeds 0 to 4, both policies, all three rules, unseen and seen. Per setting: mean and
   min to max over seeds of timely, false alarms, unnecessary alarms, window, and how many of the 5 seeds beat progress on timely at the same
   budget (beat = more timely alarms; progress has no seed) -> results/seeds/.
3. Matched false alarms (CPU, existing seed 0 scores, no retraining): timely of each model at progress's realized false-alarm rate on the
   held-out successes, and timely vs false alarms from 0 to 10%, with paired bootstrap intervals. The matched threshold is set on the held-out
   successes (pooled over folds), so this is a descriptive comparison, not a deployable rule -> results/matched_fa/ (PNG + md).
4. OR combination (CPU): alarm = progress OR gru_phys_ttp. Inside each leave-one-task-out fold both thresholds come from the training-task
   successes only (cross-fitted scores, saved by 06 --save_calib): one common conformal level for both parts, the largest one at which the
   union false-alarm rate on those training successes stays within the budget. Both policies, all rules, unseen tasks -> results/combo/.
5. Real-robot inputs (CPU): gru_phys_ttp target with (a) robot state only (eef position, eef rotation, gripper width) and (b) the same plus
   contact, no object poses. Both policies, 50% and 80%, unseen and seen -> results/realistic/. The contact signal is the one logged by
   20_physical_signals.py (robosuite check_contact between the gripper and a task object; we use the max over the goal objects and the
   articulated object, i.e. "gripper touches a task object"). A real robot would get this from a force or tactile sensor.
6. Only if GPUs are free after 1: another Pi0.5 shifted-start batch (2 to 3 cm, new seeds, gate-passed tasks) plus pre-checks and scans,
   target +30 scanned failures. Its numbers are reported separately and do not change items 2 to 5.

Nothing here changes the PNR definition or its defaults.

## Nov 7 additions (written and pushed before any job of this section started)

(a) Seed ensemble: `gru_phys_ttp_ens` = mean over seeds 0 to 4 of the per-step scores of gru_phys_ttp. Thresholds as usual: fixed conformal on
    the cross-fitted training-task successes of each fold, here the seed mean of their per-step scores (06 --save_calib now also keeps the
    per-step calibration scores; gru_phys_ttp seeds 0 to 4 are rerun for that, unseen, both policies, three rules). The OR rule with the ensemble
    (`or_progress_ens`) uses the same common-level rule as item 4.
(b) Main rule from now on: 70% (3 of 4 retries fail). 50% and 80% are sensitivity checks. Everything is still reported for all three.
(c) Fresh Pi0.5 test: once item 6 reaches 70 scanned failures, models are trained on the old Pi0.5 episodes only (natural + perturbed seeds 0 and 1)
    and scored only on the new ones (perturbed seeds 2 to 4), unseen (leave one task out, new episodes of the held-out task) and seen (all old
    tasks in training). Same recipe, rules and budgets, thresholds from old training successes, no tuning. Reported in results/pi05/fresh/ only.

Further analyses on existing scores (no tuning, descriptive where marked): task-level robustness (bootstrap over held-out tasks), rule vs first
visible failure event, one timely-vs-false-alarm curve per policy for every method (thresholds swept on held-out successes, descriptive),
rescue value from the replay retries, signal ablation (seed 0), few-shot calibration on the held-out task, clock-aware labels (retries count only
if they succeed by step 520), and breakdowns (natural only, lead time, alarm steps).
