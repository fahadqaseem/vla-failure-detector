#!/bin/bash
#SBATCH --job-name=pnr-after-rescan
#SBATCH --partition=mdtp
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=24:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# After the natural rescan with restore_query (Oct 19 2026): compare old and new t_pnr, then rerun onset,
# the leave-one-task-out predictor, and the two diagnostics (seen-task split, privileged sim-state model).
source slurm/common.sh
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
python scripts/compare_labels.py --old "data/full_scans_oct18_restore/*.json" --new "data/full_scans/*.json" \
    --out results/full_scans/rescan_compare.md
python scripts/07_auto_onset.py --episodes "data/natural/*/*.npz" --scans "data/full_scans/*.json" --out results/auto_onset.csv
python scripts/06_train_predictor.py --scans "data/full_scans/*.json" --episodes "data/natural/*/*.npz" \
    --privileged data/privileged --out results/predictor
python scripts/07_figures.py --scans "data/full_scans/*.json" --pred results/predictor --out results/predictor
python scripts/06_train_predictor.py --scans "data/full_scans/*.json" --episodes "data/natural/*/*.npz" \
    --privileged data/privileged --split episode --out results/predictor_seen_task
