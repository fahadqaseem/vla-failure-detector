#!/bin/bash
#SBATCH --job-name=t2-collect
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --array=0-9
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 collection for $PNR_POLICY, one LIBERO-10 task per array task: initial states START .. START+N-1, the
# policy's own randomness (no action noise). KIND=natural (LIBERO init states) or perturbed (moved objects, seed 0).
# GATE=1: replay gate on the task's first episode (query 1 and the middle query) -> GATE_PASS / GATE_FAIL.
source slurm/common_pi.sh
source slurm/t2_fail.sh
T=$SLURM_ARRAY_TASK_ID
D=data/$PNR_POLICY/${KIND:-natural}/task$(printf "%02d" $T)
python scripts/01_collect.py --tasks $T --start_idx ${START:-0} --episodes ${N:-50} --noise_std 0     $( [ "$KIND" = perturbed ] && echo --perturb ) --out $D || exit 1
if [ "${GATE:-0}" = 1 ]; then
    FIRST=$(ls $D/*.npz | head -1)
    for Q in 1 -1; do
        if ! python scripts/02_replay_test.py --episode "$FIRST" --query $Q --steps 80 --full; then
            echo "query $Q of $FIRST" > $D/GATE_FAIL; echo "replay gate FAILED for task $T"; exit 0
        fi
    done
    touch $D/GATE_PASS
fi
