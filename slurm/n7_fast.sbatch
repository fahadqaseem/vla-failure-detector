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
# Nov 7 audit, fast items on what exists now: 52 rule vs events (after the Pi0.5 onset job), 51 task level, 57 breakdowns. The final audit job
# reruns 51 and 57 with the ensemble and all OR seeds.
python scripts/52_rule_events.py --out results/rule_events || exit 1
python scripts/51_tasklevel.py --out results/tasklevel || exit 1
python scripts/57_breakdowns.py --out results/breakdowns || exit 1
echo "| $(date +%F) | Nov 7 audit, first pass: 52_rule_events.py, 51_tasklevel.py, 57_breakdowns.py (ensemble and some OR seeds not ready yet, listed as missing) | $(git rev-parse --short HEAD) | results/rule_events/rule_events.md, results/tasklevel/tasklevel.md, results/breakdowns/ | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "audit: rule vs events, task level, breakdowns (first pass)"
