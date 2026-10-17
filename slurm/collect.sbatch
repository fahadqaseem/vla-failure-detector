#!/bin/bash
#SBATCH --job-name=pnr-collect
#SBATCH --partition=gmsap
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_h200:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
source slurm/common.sh
# Override with: ARGS="--tasks 0 --episodes 1" sbatch slurm/collect.sbatch
python scripts/01_collect.py ${ARGS:---tasks 0 1 2 3 4 5 6 7 8 9 --episodes 3}
