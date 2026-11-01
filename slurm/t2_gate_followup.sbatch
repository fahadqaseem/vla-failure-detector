#!/bin/bash
#SBATCH --job-name=t2-gate-followup
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 after t2_gate_retest: failures of tasks that now pass go to a separate scan list (the running arrays index
# targets.txt by line, so it stays as it is), the pending training chain ($WAIT_JOB) waits for those scans, and it is logged.
source slurm/common.sh
source slurm/t2_fail.sh
L=results/$P/natural_scans
python scripts/scan_targets.py --root data/$P/natural --n_success 0 --require_gate --out $L/targets_failures.tmp || exit 1
grep -vxFf $L/targets.txt $L/targets_failures.tmp > $L/targets_retest.txt
rm $L/targets_failures.tmp
N=$(grep -c . $L/targets_retest.txt)
S=none
if [ "$N" -gt 0 ]; then
    F=$(bash slurm/gpu_free.sh)
    source slurm/t2_split.sh
    S=$(split_scan "t2-scan-$P-retest" "$N" "ALL,PNR_POLICY=$P,TARGETS=$L/targets_retest.txt,OUT=data/$P/full_scans" "" "$F") || exit 1
    scontrol update JobId=$WAIT_JOB Dependency=$(squeue -h -j $WAIT_JOB -o %E | sed 's/(unfulfilled)//g'),afterany:${S//:/,afterany:} || exit 1
fi
scontrol update JobId=$NICE_JOB Nice=0
PASSED=$(ls data/$P/natural/*/GATE_FAIL_e00 2>/dev/null | cut -d/ -f4 | tr '\n' ' ')
DRIFT=$(grep -H "^replayed" results/$P/gate_retest/task*.txt | sed -E 's/.*(task[0-9]+)\.txt:replayed 80 steps: eef deviation max ([0-9.]+) mm.*/\1 \2 mm;/' | tr '\n' ' ')
echo "| $(date +%F) | Track 2 $P gate retest on e01 (job $GATE_JOB, 10 mm limit): passed ${PASSED:-none}; $N failures added in $L/targets_retest.txt, scan array $S, $WAIT_JOB waits for it | $(git rev-parse --short HEAD) | $DRIFT | results/$P/gate_retest; a task that failed again stays out. job $SLURM_JOB_ID (auto) |" >> results/LOG.md
bash slurm/w2_push.sh "$P: gate retest on e01"
