#!/bin/bash
#SBATCH --job-name=w2-refine-submit
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:20:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Week 2 Phase A: K 16 near the boundary for all timed failures (old and new scans), then Phase D after it.
source slurm/common.sh
T=results/week2/refine/targets.txt
python scripts/15_refine_targets.py --scans "data/full_scans/*.json" "data/perturbed_scans/*.json" \
    "data/perturbed_v2_scans/*.json" --out $T
N=$(grep -c . $T)
DEP=""
if [ "$N" -gt 0 ]; then
    REF=$(sbatch --parsable --array=0-$((N - 1))%3 slurm/w2_refine.sbatch)
    echo "refine array $REF ($N targets)"; DEP="--dependency=afterany:$REF"
fi
# Phase D also waits for the Phase C report (best variants) and the Phase B report, if their ids were passed.
for J in $C_REPORT $B_REPORT; do DEP="${DEP:---dependency=}${DEP:+,}afterany:$J"; done
DEP=${DEP/--dependency=,/--dependency=}
sbatch $DEP slurm/w2_phase_d.sbatch
bash slurm/w2_push.sh "week2: refinement list"
