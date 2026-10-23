#!/bin/bash
#SBATCH --job-name=t2-after-collect
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Track 2 for $P after the 500 natural episodes: full scans of every natural failure in gate-passed tasks plus 2
# successes per task. If fewer than 40 such failures (rule fixed Oct 23), perturbed starting scenes follow after the
# natural scans (50 per task, seed 0, gate, pre-check, scans), reported separately. Then training (t2_train_submit).
source slurm/common.sh
T=results/$P/natural_scans/targets.txt
python scripts/scan_targets.py --root data/$P/natural --n_success 2 --require_gate --out $T
NF=$(python -c "import csv,glob,os; print(sum(int(r['success'])==0 for f in glob.glob('data/$P/natural/task*/index.csv') if os.path.exists(os.path.join(os.path.dirname(f),'GATE_PASS')) for r in csv.DictReader(open(f))))")
N=$(grep -c . $T)
echo "$P: $NF natural failures in gate-passed tasks, $N scan targets"
F=$(bash slurm/gpu_free.sh)
S=$(sbatch --parsable -J t2-scan-$P --array=0-$((N - 1))%$F --export=ALL,PNR_POLICY=$P,TARGETS=$T,OUT=data/$P/full_scans slurm/t2_scan_array.sbatch)
C=$(git rev-parse --short HEAD)
echo "| $(date +%F) | Track 2 $P: 500 natural episodes collected; scan list $T ($N lines), scan array $S | $C | $NF natural failures in gate-passed tasks | gates: $(ls data/$P/natural/*/GATE_* 2>/dev/null | xargs -n1 basename | sort | uniq -c | tr '\n' ' ') job $SLURM_JOB_ID (auto) |" >> results/LOG.md
if [ "$NF" -lt 40 ]; then
    E=$(sbatch --parsable -J t2-collect-$P-pert --array=0-9%$F --dependency=afterany:$S --export=ALL,PNR_POLICY=$P,KIND=perturbed,START=0,N=50,GATE=1 slurm/t2_collect.sbatch)
    R=$(sbatch --parsable -J t2-precheck-$P --array=0-9%$F --dependency=afterany:$E --export=ALL,PNR_POLICY=$P slurm/t2_precheck.sbatch)
    sbatch --dependency=afterany:$R --export=ALL,P=$P slurm/t2_perturbed_scans.sbatch
else
    sbatch --dependency=afterany:$S --export=ALL,P=$P slurm/t2_train_submit.sbatch
fi
bash slurm/w2_push.sh "$P: scan list"
