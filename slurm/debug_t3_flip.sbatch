#!/bin/bash
#SBATCH --job-name=pnr-debug-t3
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Debug the t3 outcome flip (Oct 19 2026): t03_e00_p0 from query 1 drifts only 3.19 mm over 80 steps, but the
# full replay fails at 520 while the recording succeeded at 225. Where do actions first differ, and does the
# outcome also flip from later checkpoints? Low priority, submitted by perturbed_submit_scans.sbatch after the scans.
source slurm/common.sh
EP=data/perturbed/task03/t03_e00_p0.npz
python scripts/drift_debug.py $EP:1 --limit 240
for Q in 2 4 8 -1; do
    echo "=== query $Q"
    python scripts/02_replay_test.py --episode $EP --query $Q --steps 80 --full
done
exit 0
