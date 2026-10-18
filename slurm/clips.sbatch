#!/bin/bash
#SBATCH --job-name=pnr-clips
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Clips around automatic onset events (EGL rendering needs the GPU node; no policy is loaded).
source slurm/common.sh
python scripts/08_event_clips.py --ids ${IDS:-t02_e10_n0 t00_e14_n0 t08_e06_n0} --out results/clips
