#!/bin/bash
#SBATCH --job-name=pnr-pnr
#SBATCH --partition=gmsap
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_h200:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=04:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
source slurm/common.sh
python scripts/03_pnr_scan.py --episodes "${EPS:-data/rollouts/*.npz}"
