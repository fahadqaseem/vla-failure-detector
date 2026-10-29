#!/bin/bash
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=06:00:00
#SBATCH --output=pnr_probe/logs/%x-%A_%a.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Dense open-loop replay, one array task per line block of pnr_probe/dense/all_episodes.txt (CHUNK lines each).
source slurm/common.sh
export OMP_NUM_THREADS=2
CHUNK=${CHUNK:-50}
F=$(sed -n "$((SLURM_ARRAY_TASK_ID * CHUNK + 1)),$(((SLURM_ARRAY_TASK_ID + 1) * CHUNK))p" pnr_probe/dense/all_episodes.txt)
python pnr_probe/dense/${SCRIPT:-dense_replay.py} --episodes $F --out ${OUT:-pnr_probe/data/dense}
