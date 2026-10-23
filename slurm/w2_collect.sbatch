#!/bin/bash
#SBATCH --job-name=w2-collect
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=08:00:00
#SBATCH --array=0-6%3
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 2 Phase A (docs/PLAN_week2.md): 100 new perturbed-natural episodes for one task (initial states 0-49 with
# seeds 1 and 2; the old ones used seed 0), then the replay gate on the first one at query 1 and the middle query.
# Gate pass -> GATE_PASS, fail -> GATE_FAIL and exit 0, so the chain goes on with the other tasks.
source slurm/common.sh
TASKS=(0 1 4 5 6 7 8)
TID=${TASKS[$SLURM_ARRAY_TASK_ID]}
D=data/perturbed_v2/task$(printf "%02d" $TID)
for SEED in 1 2; do
    python scripts/01_collect.py --tasks $TID --episodes 50 --perturb --seed $SEED --out $D || exit 1
done
FIRST=$(ls $D/*.npz | head -1)
for Q in 1 -1; do
    if ! python scripts/02_replay_test.py --episode "$FIRST" --query $Q --steps 80 --full; then
        echo "query $Q of $FIRST" > $D/GATE_FAIL; echo "replay gate FAILED for task $TID"; exit 0
    fi
done
touch $D/GATE_PASS
