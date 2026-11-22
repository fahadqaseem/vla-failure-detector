#!/bin/bash
#SBATCH --job-name=gt20-pooled-report
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Nov 22 plan, Step 4: report of the interim pooled target (data/gt20/pooled), same format as results/regression_v2/main.md.
source slurm/common.sh
fail() { rc=$?; [ $rc = 0 ] && return; echo "| $(date +%F) | $SLURM_JOB_NAME $SLURM_JOB_ID FAILED (exit $rc), see logs/$SLURM_JOB_NAME-$SLURM_JOB_ID.out | $(git rev-parse --short HEAD) | failed | not resubmitted |" >> results/LOG.md; bash slurm/w2_push.sh "log: $SLURM_JOB_NAME failed"; }
trap fail EXIT
NOTE="INTERIM SMOOTHING, NOT THE 20-REPLAY GROUND TRUTH (results/plan_nov22_gt20.md, Step 4): target and floor here use the pooled failure fraction = failed / all replays over the scan checkpoints k-1, k, k+1 (about 12 replays, or more where refined), on the same episodes, exclusions, t_pnr values and models as results/regression_v2. The floor treats the pooled count as binomial, so it is approximate. Compare with results/regression_v2/main.md (raw K 4 target)."
O=results/gt20/pooled; mkdir -p $O
python scripts/61_regression_report.py --root data/gt20/pooled --out $O --note "$NOTE" || exit 1
cp $O/main.md results/gt20/pooled_main.md
echo "| $(date +%F) | Nov 22 Step 4: interim pooled target (60_regression.py --target pooled, gt20_pooled_submit.sh; 61_regression_report.py), every model, seeds 0 to 4, both policies, unseen | $(git rev-parse --short HEAD) | results/gt20/pooled_main.md, results/gt20/pooled/ | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "gt20: pooled interim report"
