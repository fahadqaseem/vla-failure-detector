#!/bin/bash
#SBATCH --job-name=fs-run
#SBATCH --partition=reqp
#SBATCH --qos=requeue
#SBATCH --requeue
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --time=1-00:00:00
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# FailureSpot methods, one array task per held-out task (MODE=loto, array 0-9) or seed (MODE=own, array 0-2).
# METHODS, DEVICE (cpu default). Finished methods are skipped after a preemption.
source slurm/common.sh
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-4}
G=$SLURM_ARRAY_TASK_ID
python scripts/30_fs_run.py --mode $MODE --group $G --methods $METHODS --device ${DEVICE:-cpu} --out results/week3/failurespot/$MODE/g$G
