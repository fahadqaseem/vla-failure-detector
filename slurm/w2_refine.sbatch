#!/bin/bash
#SBATCH --job-name=w2-refine
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=04:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# One line of results/week2/refine/targets.txt: "episode t_min t_max". 12 more replays (seed 1) at the two
# checkpoints around the tau 0.5 boundary, so they have 16 in total (CLAUDE.md decision 1).
source slurm/common.sh
read EP TMIN TMAX <<< "$(sed -n "$((SLURM_ARRAY_TASK_ID + 1))p" results/week2/refine/targets.txt)"
if [ -z "$EP" ]; then echo "no target"; exit 0; fi
python scripts/03_pnr_scan.py --episodes "$EP" --every 8 --K 12 --min_fail 2 --seed 1 --noise_std 0.05 \
    --extra_steps 200 --full_curve --t_min $TMIN --t_max $TMAX --out data/week2_refine
