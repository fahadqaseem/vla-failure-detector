#!/bin/bash
#SBATCH --job-name=pnr-check
#SBATCH --partition=gmsap
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_h200:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
source slurm/common.sh
nvidia-smi
python scripts/00_check_env.py
