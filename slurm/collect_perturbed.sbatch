#!/bin/bash
#SBATCH --job-name=pnr-perturbed
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=04:00:00
#SBATCH --array=0-9
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Perturbed-natural episodes, one array task per LIBERO-10 task: initial states 0-49 with every movable
# object shifted 2-3 cm and rotated up to 15 deg (pnr/perturb.py), no action noise, features saved.
# Then the replay gate (02_replay_test.py, must pass before any scan) on the first episode at 2 queries.
# Pre-checks run separately after the natural rescan (slurm/precheck_perturbed.sbatch, Fahad Oct 19).
source slurm/common.sh
T=$(printf "%02d" $SLURM_ARRAY_TASK_ID)
D=data/perturbed/task$T
python scripts/01_collect.py --tasks $SLURM_ARRAY_TASK_ID --episodes 50 --perturb --out $D
FIRST=$(ls $D/*.npz | head -1)
for Q in 1 -1; do  # two checkpoints: query 1 and the middle one (one alone missed a failure, Oct 19)
    python scripts/02_replay_test.py --episode "$FIRST" --query $Q --steps 80 --full || { echo "replay test FAILED on $FIRST query $Q: no pre-check"; exit 1; }
done
