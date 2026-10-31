#!/bin/bash
#SBATCH --job-name=pifs-chunks
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# 50-step chunks of one task's Pi0.5 episodes (41_pi_chunks.py), one array task per LIBERO-10 task.
source slurm/common_pi.sh
source slurm/t2_fail.sh
python scripts/41_pi_chunks.py --task $SLURM_ARRAY_TASK_ID ${ARGS:-} || exit 1
