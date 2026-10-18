#!/bin/bash
#SBATCH --job-name=pnr-natural
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=03:00:00
#SBATCH --array=0-9
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# One array task per LIBERO-10 task: all 50 initial states, no noise (natural), features saved.
# Each task writes its own folder, so no two jobs append to the same index.csv.
source slurm/common.sh
T=$(printf "%02d" $SLURM_ARRAY_TASK_ID)
python scripts/01_collect.py --tasks $SLURM_ARRAY_TASK_ID --episodes 50 --out data/natural/task$T
