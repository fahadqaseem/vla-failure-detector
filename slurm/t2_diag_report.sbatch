#!/bin/bash
#SBATCH --job-name=t2-diag-report
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:20:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 diagnosis table (26_pi_diag_table.py), logged and pushed.
source slurm/common.sh
python scripts/26_pi_diag_table.py --dir results/$P/diag --out results/$P/diag.md
echo "| $(date +%F) | Track 2 $P diagnosis: lerobot-eval (default settings) and 25_pi_diag.py with 5, 8, 50 steps per query, tasks 0 and 8, initial states 0 to 9; 26_pi_diag_table.py | $(git rev-parse --short HEAD) | results/$P/diag.md | job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "$P: diagnosis table"
