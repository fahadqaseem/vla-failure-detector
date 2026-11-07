#!/bin/bash
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=2
#SBATCH --mem=48G
#SBATCH --time=04:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
source slurm/common.sh
fail() { rc=$?; [ $rc = 0 ] && return; echo "| $(date +%F) | $SLURM_JOB_NAME $SLURM_JOB_ID FAILED (exit $rc), see logs/$SLURM_JOB_NAME-$SLURM_JOB_ID.out | $(git rev-parse --short HEAD) | failed | not resubmitted |" >> results/LOG.md; bash slurm/w2_push.sh "log: $SLURM_JOB_NAME failed"; }
trap fail EXIT
# Nov 7 audit, main pass after the ensemble reruns, the SAFE / Hide-and-Seek runs at 70% and the Pi0.5 OR seeds: build the ensemble, then
# items 1, 9, 5, 7, 8, 4, each pushed as it lands.
for P in oft pi05; do
  for M in safe hideseek; do python scripts/28_merge_groups.py --dir data/base70/$P/$M --groups 10 || exit 1; done
  for T in 50 70 80; do
    for S in 0 1 2 3 4; do python scripts/28_merge_groups.py --dir data/ens/$P/thr$T/s$S --groups 10 > /dev/null || exit 1; done
    python scripts/50_ensemble.py --root data/ens/$P/thr$T --combo data/combo/$P/thr$T --out data/ens/$P/thr$T/merged || exit 1
  done
done
C=$(git rev-parse --short HEAD)
step() { echo "| $(date +%F) | Nov 7 audit: $1 | $C | $2 | job $SLURM_JOB_ID (auto) |" >> results/LOG.md; bash slurm/w2_push.sh "audit: $3"; }
python scripts/51_tasklevel.py --out results/tasklevel || exit 1; step "51_tasklevel.py (with ensemble and OR seeds)" "results/tasklevel/tasklevel.md" "task level"
python scripts/57_breakdowns.py --out results/breakdowns || exit 1; step "57_breakdowns.py" "results/breakdowns/" "breakdowns"
python scripts/54_rescue.py --out results/rescue || exit 1; step "54_rescue.py" "results/rescue/rescue.md" "rescue value"
python scripts/55_fewshot.py --out results/fewshot || exit 1; step "55_fewshot.py" "results/fewshot/fewshot.md" "few-shot calibration"
python scripts/56_clock.py --out data/clock || exit 1
for P in oft pi05; do for T in 50 70 80; do for k in "fixed 0.05" "fixed 0.025"; do
  python scripts/13_report.py --pred data/clock/${P}_thr$T --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "results/clock/${P}_thr${T}_report_${k// /_}.md" || exit 1
done; python scripts/46_paired_alarms.py --pred data/clock/${P}_thr$T --out results/clock/${P}_thr${T}_alarms.md > /dev/null || exit 1; done; done
step "56_clock.py, 13_report.py, 46_paired_alarms.py on clock-aware labels" "results/clock/label_changes.md, *_report_*, *_alarms.md" "clock-aware labels"
python scripts/53_curves.py --out results/curves || exit 1; step "53_curves.py (SAFE, Hide-and-Seek from data/base70, 06 at 70%)" "results/curves/curves.md, curves.png" "one curve every method"
