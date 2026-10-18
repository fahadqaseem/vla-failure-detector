#!/bin/bash
#SBATCH --job-name=pnr-fullscan
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=06:00:00
#SBATCH --array=0-47%4
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Full replay scans (every checkpoint) used as t_pnr labels: one array task per line of
# results/full_scans/targets.txt (all natural failures, then 2 successes per task; scripts/scan_targets.py).
# %4 = at most 4 at once. Episodes already scanned (output JSON exists) are skipped.
source slurm/common.sh
EP=$(sed -n "$((SLURM_ARRAY_TASK_ID + 1))p" results/full_scans/targets.txt)
if [ -z "$EP" ]; then echo "no target for line $SLURM_ARRAY_TASK_ID"; exit 0; fi
if [ -f "data/full_scans/$(basename "$EP" .npz).json" ]; then echo "already scanned: $EP"; exit 0; fi
echo "target $SLURM_ARRAY_TASK_ID: $EP"
python scripts/03_pnr_scan.py --episodes "$EP" --include_success 1 --every 8 --K 4 --min_fail 2 \
    --noise_std 0.05 --extra_steps 200 --full_curve --out data/full_scans
