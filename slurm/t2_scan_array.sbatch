#!/bin/bash
#SBATCH --job-name=t2-scan
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=10:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 full scans for $PNR_POLICY (one line of $TARGETS per array task): K 4, every 8 steps, tau 0.5, 200 extra
# steps, the policy's own randomness (new flow seed per replay), no action noise (Oct 23). Output $OUT.
source slurm/common_pi.sh
EP=$(sed -n "$((SLURM_ARRAY_TASK_ID + 1))p" "$TARGETS")
[ -z "$EP" ] && { echo "no target"; exit 0; }
[ -f "$OUT/$(basename "$EP" .npz).json" ] && { echo "already scanned: $EP"; exit 0; }
python scripts/03_pnr_scan.py --episodes "$EP" --include_success 1 --every 8 --K 4 --min_fail 2     --noise_std 0 --extra_steps 200 --full_curve --out "$OUT"
