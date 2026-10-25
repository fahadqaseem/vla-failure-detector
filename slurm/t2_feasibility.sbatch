#!/bin/bash
#SBATCH --job-name=t2-feasibility
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 verdict for $P (23_pi_feasibility.py), pushed. PASS: collect the other 30 episodes per task with the replay
# gate, then t2_after_collect; for pi0 also start pi05. FAIL: stop here (results/$P/feasibility.md says why).
source slurm/common.sh
python scripts/23_pi_feasibility.py --policy $P
C=$(git rev-parse --short HEAD)
echo "| $(date +%F) | Track 2 $P feasibility: 22_pi_checks.py, 20 episodes per task (t2_collect), 23_pi_feasibility.py | $C | $(cat results/$P/feasibility_status.txt) | results/$P/feasibility.md, checks.json; job $SLURM_JOB_ID (auto) |" >> results/LOG.md
git add results/$P 2>/dev/null
bash slurm/w2_push.sh "$P feasibility"
if grep -q PASS results/$P/feasibility_status.txt; then
    F=$(bash slurm/gpu_free.sh)
    [ "$P" = pi0 ] && [ $F -gt 1 ] && F=$((F - 1))  # keep one slot for pi05 (5 GPU job cap)
    E=$(sbatch --parsable -J t2-collect-$P --array=0-9%$F --export=ALL,PNR_POLICY=$P,KIND=natural,START=20,N=30,GATE=1 slurm/t2_collect.sbatch)
    sbatch --dependency=afterany:$E --export=ALL,P=$P slurm/t2_after_collect.sbatch
fi
# Pi0.5 starts right after the pi0 verdict passes, in parallel with pi0's scans and training (Fahad, Oct 25)
grep -q PASS results/$P/feasibility_status.txt && [ "$P" = pi0 ] && bash slurm/t2_start.sh pi05
true
