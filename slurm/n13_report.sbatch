#!/bin/bash
#SBATCH --job-name=n13-report
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
source slurm/common.sh
fail() { rc=$?; [ $rc = 0 ] && return; echo "| $(date +%F) | $SLURM_JOB_NAME $SLURM_JOB_ID FAILED (exit $rc), see logs/$SLURM_JOB_NAME-$SLURM_JOB_ID.out | $(git rev-parse --short HEAD) | failed | not resubmitted |" >> results/LOG.md; bash slurm/w2_push.sh "log: $SLURM_JOB_NAME failed"; }
trap fail EXIT
# Nov 13 plan and amendment: main.md, seeds.md, backup.md, per_task.md, plots/ from data/regression_v2 (seeds 0 to 4, every learned model).
O=results/regression_v2; mkdir -p $O
python scripts/61_regression_report.py --root data/regression_v2 --out $O || exit 1
python scripts/62_regression_plots.py --root data/regression_v2 --out $O/plots || exit 1
echo "| $(date +%F) | Nov 13 regression (60_regression.py, n13_submit.sh; 61_regression_report.py, 62_regression_plots.py): seeds 0 to 4 for every learned model, seed 0 baselines, both policies, unseen | $(git rev-parse --short HEAD) | results/regression_v2/main.md, seeds.md, backup.md, per_task.md, plots/ | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "regression v2: report and plots"
