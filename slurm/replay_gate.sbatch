#!/bin/bash
#SBATCH --job-name=pnr-gate
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=02:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Replay gate at several checkpoints (Oct 19 2026: one checkpoint passing is not enough, query 24 of
# t00_e00_n0 passed while query 1 failed). Arguments: episode:query pairs. Exit 1 if any fails.
source slurm/common.sh
fail=0
for pair in "$@"; do
    echo "=== ${pair}"
    python scripts/02_replay_test.py --episode "${pair%%:*}" --query "${pair##*:}" --steps 80 --full || fail=1
done
exit $fail
