#!/bin/bash
#SBATCH --job-name=t2-perturbed-scans
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2: full scans of the perturbed failures of $P whose pre-check says "scan", then training.
source slurm/common.sh
T=results/$P/perturbed_scans/targets.txt
python scripts/scan_targets.py --root data/$P/perturbed --n_success 0 --prechecks data/$P/perturbed/prechecks --require_gate --out $T
N=$(grep -c . $T)
DEP=""
if [ "$N" -gt 0 ]; then
    F=$(bash slurm/gpu_free.sh)
    S=$(sbatch --parsable -J t2-scan-$P-pert --array=0-$((N - 1))%$F --export=ALL,PNR_POLICY=$P,TARGETS=$T,OUT=data/$P/perturbed_scans slurm/t2_scan_array.sbatch)
    DEP="--dependency=afterany:$S"
fi
sbatch $DEP --export=ALL,P=$P slurm/t2_train_submit.sbatch
bash slurm/w2_push.sh "$P: perturbed scan list"
