#!/bin/bash
#SBATCH --job-name=t2-checks
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2: first checks for $PNR_POLICY (22_pi_checks.py: one episode, replay gate, do new flow seeds differ).
source slurm/common_pi.sh
source slurm/t2_fail.sh
python scripts/22_pi_checks.py
