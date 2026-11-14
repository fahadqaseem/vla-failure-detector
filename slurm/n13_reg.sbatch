#!/bin/bash
#SBATCH --job-name=n13-reg
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Nov 13 plan (results/plan_nov13.md): pure regression, one held-out task per array task (0 to 9), CPU only.
# POL=oft|pi05, MODEL (60_regression.py --model), SEED, EXTRA (e.g. --smoke). Output data/regression_v2/$POL/$MODEL/s$SEED/g$G.json.
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
python scripts/60_regression.py --policy $POL --model $MODEL --held_out $SLURM_ARRAY_TASK_ID --seed ${SEED:-0} ${EXTRA:-} \
    --out ${OUT:-data/regression_v2}/$POL
