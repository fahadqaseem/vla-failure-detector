#!/bin/bash
#SBATCH --job-name=w2-lookahead
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 2 Phase B (UPPER BOUND, simulator at test time): look-ahead futures for 10 episodes per array task.
source slurm/common.sh
python scripts/15_lookahead.py --targets results/week2/lookahead/targets.txt --lines $((SLURM_ARRAY_TASK_ID * 10)) 10 \
    --out data/week2_lookahead
