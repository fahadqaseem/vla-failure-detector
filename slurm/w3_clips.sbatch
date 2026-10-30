#!/bin/bash
#SBATCH --job-name=w3-clips
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# 10 clips around t_pnr (36_pnr_clips.py), pushed.
source slurm/common.sh
python scripts/36_pnr_clips.py || exit 1
echo "| $(date +%F) | Week 3 clips at t_pnr: 36_pnr_clips.py | $(git rev-parse --short HEAD) | results/week3/patterns/clips/ | written by job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "week3: clips at t_pnr"
