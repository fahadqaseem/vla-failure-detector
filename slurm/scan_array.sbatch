#!/bin/bash
#SBATCH --job-name=pnr-fullscan
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=06:00:00
#SBATCH --array=0-2
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Full replay scans (every checkpoint) on 3 natural failures from different tasks, to test whether
# success probability only goes down over time. Picks come from scripts/pick_failures.py (fixed rule).
source slurm/common.sh
EP=$(python scripts/pick_failures.py --root data/natural --n 3 --index $SLURM_ARRAY_TASK_ID)
if [ -z "$EP" ]; then echo "no failure for pick $SLURM_ARRAY_TASK_ID"; exit 0; fi
echo "pick $SLURM_ARRAY_TASK_ID: $EP"
python scripts/03_pnr_scan.py --episodes "$EP" --every 8 --K 4 --min_fail 2 --noise_std 0.05 \
    --extra_steps 200 --full_curve --out data/full_scans
