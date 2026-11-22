#!/bin/bash
#SBATCH --job-name=gt20-report
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Nov 22 amendment: regression v2 on the OpenVLA-OFT 20-replay truth (data/gt20/regression), same format as results/regression_v2.
source slurm/common.sh
fail() { rc=$?; [ $rc = 0 ] && return; echo "| $(date +%F) | $SLURM_JOB_NAME $SLURM_JOB_ID FAILED (exit $rc), see logs/$SLURM_JOB_NAME-$SLURM_JOB_ID.out | $(git rev-parse --short HEAD) | failed | not resubmitted |" >> results/LOG.md; bash slurm/w2_push.sh "log: $SLURM_JOB_NAME failed"; }
trap fail EXIT
NOTE="20-REPLAY TRUTH (results/plan_nov22_gt20.md, amendment Nov 22): failed runs use the failure fraction from 20 replays at every checkpoint (every 8 steps; 67_gt20_worker.py, data/gt20/oft), t_pnr (backup alarms) from the same 20 replays. Same episodes, exclusions and models as results/regression_v2 (exclusions decided on the K 4 scans). Successes unchanged (target 0, or the K 4 scan for the 20 scanned OFT successes). OpenVLA-OFT only; Pi0.5 follows."
O=results/gt20; mkdir -p $O
python scripts/61_regression_report.py --root data/gt20/regression --policies oft --out $O --note "$NOTE" || exit 1
python scripts/62_regression_plots.py --root data/gt20/regression --policies oft --out $O/plots_reg || exit 1
echo "| $(date +%F) | Nov 22 amendment: regression v2 on the OFT 20-replay truth (60_regression.py --target gt20, gt20_full_submit.sh; 61_regression_report.py, 62_regression_plots.py), every model, seeds 0 to 4 | $(git rev-parse --short HEAD) | results/gt20/main.md, seeds.md, backup.md, per_task.md, plots_reg/ | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "gt20: regression on the OFT 20-replay truth"
