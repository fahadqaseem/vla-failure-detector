#!/bin/bash
#SBATCH --job-name=pnr-fullscan-rq
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=06:00:00
#SBATCH --requeue
#SBATCH --array=0-47%4
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --open-mode=append
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Extra L40S capacity for the label scans on the preemptible partition (same GPU type as galhp).
# Walks results/full_scans/targets.txt from the END, so it meets the galhp array (which walks from the
# start) as late as possible. 03_pnr_scan.py takes a lock per episode, so no episode is scanned twice;
# a preempted job is requeued with the same job id, takes its own lock back and restarts the scan.
source slurm/common.sh
EP=$(sed -n "$((48 - SLURM_ARRAY_TASK_ID))p" results/full_scans/targets.txt)
if [ -z "$EP" ]; then echo "no target for task $SLURM_ARRAY_TASK_ID"; exit 0; fi
if [ -f "data/full_scans/$(basename "$EP" .npz).json" ]; then echo "already scanned: $EP"; exit 0; fi
echo "target (from end) $SLURM_ARRAY_TASK_ID: $EP"
python scripts/03_pnr_scan.py --episodes "$EP" --include_success 1 --every 8 --K 4 --min_fail 2 \
    --noise_std 0.05 --extra_steps 200 --full_curve --out data/full_scans
