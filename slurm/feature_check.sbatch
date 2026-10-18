#!/bin/bash
#SBATCH --job-name=pnr-featcheck
#SBATCH --partition=galhp
#SBATCH --qos=gpu
#SBATCH --gres=gpu:nvidia_l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=00:45:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Gate before big collections: re-record t00_e00_n0 with the new code; it must match the old
# recording exactly and still pass the replay test. Any failure stops the job (exit code != 0).
source slurm/common.sh
set -e
python scripts/01_collect.py --tasks 0 --episodes 1 --out data/feature_check
python scripts/compare_episodes.py data/rollouts/t00_e00_n0.npz data/feature_check/t00_e00_n0.npz
python scripts/02_replay_test.py --episode data/feature_check/t00_e00_n0.npz --steps 80 --full
