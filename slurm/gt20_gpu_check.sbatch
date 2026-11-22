#!/bin/bash
#SBATCH --job-name=gt20-gpucheck
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=03:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# GPU type check (plan_nov22_gt20.md amendment): partition / qos / gres given at submit time.
# 1) replay gate (02_replay_test.py --full, query 1 and middle) on t01_e07_p0_s1; 2) rerun two finished pilot checkpoints (all 20 replays,
# same seeds) and compare with the L40S outcomes (66_gpu_check.py).
source slurm/common.sh
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
for q in 1 -1; do python scripts/02_replay_test.py --episode data/perturbed_v2/task01/t01_e07_p0_s1.npz --query $q --steps 80 --full; done
python scripts/66_gpu_check.py --checkpoints data/gt20_pilot/t01_e07_p0_s1/c000.json data/gt20_pilot/t00_e06_p0_s1/c016.json --out results/gt20/gpu_check
