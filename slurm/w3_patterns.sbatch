#!/bin/bash
#SBATCH --job-name=w3-patterns
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 3 patterns at t_pnr: table, plot, clip list; pushed. Then the clips (one short GPU job, after Pi0.5 collection, inside the cap).
source slurm/common.sh
python scripts/35_patterns.py || exit 1
echo "| $(date +%F) | Week 3 patterns: 07_auto_onset.py on all data -> results/week3/patterns/auto_onset.csv; 35_patterns.py | $(git rev-parse --short HEAD) | results/week3/patterns/patterns.md, signals_by_type.png, clip_ids.txt | written by job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "week3: patterns at t_pnr"
sbatch --dependency=afterany:40888023 slurm/w3_clips.sbatch || sbatch slurm/w3_clips.sbatch
