#!/bin/bash
#SBATCH --job-name=pnr-replay
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
source slurm/common.sh
python scripts/02_replay_test.py --episode $EP --steps 80 --full
