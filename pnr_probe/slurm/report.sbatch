#!/bin/bash
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=02:00:00
#SBATCH --output=pnr_probe/logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# Report (13_report.py style, 5% and 2.5%) + summary, then commit and push pnr_probe/results to pnr-probe only.
source slurm/common.sh
R=pnr_probe/results
SETS="surprise csd ttc micro bio bioplus t1"
for split in unseen seen; do
    P=""; for s in $SETS; do [ -f $R/${split}_$s/per_episode.json ] && P="$P $R/${split}_$s"; done
    for k in "fixed 0.05" "fixed 0.025"; do
        python pnr_probe/13_report.py --pred $P --key "$k" --headline "fixed 0.05" "fixed 0.025" --out "$R/${split}_report_${k// /_}.md"
    done
done
python pnr_probe/summary.py --results $R --sets $SETS --out $R/summary.md
C=$(git rev-parse --short HEAD)
echo "| $(date +%F) | bio precursor report: pnr_probe/slurm/submit.sh chain, 13_report.py + summary.py | $C | $R/summary.md, $R/*_report_*.md | job $SLURM_JOB_ID |" >> $R/LOG.md
[ "$(git branch --show-current)" = pnr-probe ] || { echo "not on pnr-probe, not pushing"; exit 1; }
find $R -type f -size +50M -printf "too big, not committed: %p\n"
git add $(find $R -type f -size -50M) pnr_probe/*.py pnr_probe/slurm pnr_probe/.gitignore
git -c user.name="Fahad Qaseem Khawar" commit -qm "pnr_probe: bio-inspired precursor features report

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" || echo "nothing to commit"
for try in 1 2; do git push -q -u origin pnr-probe && { echo pushed; exit 0; }; sleep 30; done
echo "PUSH FAILED" | tee -a $R/push_failures.txt
