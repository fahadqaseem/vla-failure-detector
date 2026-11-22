#!/bin/bash
#SBATCH --job-name=gt20-analysis
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Nov 22 plan (results/plan_nov22_gt20.md), Steps 2 and 3: cost.md and the pilot analysis from whatever pilot checkpoints exist now.
# STAGE=interim (2 h after the pilot starts) or final (after the pilot ends). Pushes results/gt20.
source slurm/common.sh
STAGE=${STAGE:-final}
python scripts/65_gt20_cost.py --pilot data/gt20_pilot --out results/gt20/cost.md || exit 1
python scripts/64_gt20_analysis.py --pilot data/gt20_pilot --out results/gt20 || exit 1
echo "| $(date +%F) | Nov 22 Steps 2-3 ($STAGE): 65_gt20_cost.py, 64_gt20_analysis.py on data/gt20_pilot ($(ls data/gt20_pilot/*/c*.json | wc -l) of 99 checkpoints) | $(git rev-parse --short HEAD) | results/gt20/cost.md, pilot.md, plots/ | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "gt20: cost and pilot analysis ($STAGE)"
