#!/bin/bash
#SBATCH --partition=mdtp
#SBATCH --qos=primary
#SBATCH --cpus-per-task=2
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=pnr_probe/logs/%x-%j.out
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=hr4625@wayne.edu
# micro_phys report: 13_report.py at 2.5% and 5% (unseen = headline, seen), the micro-event figure, then commit and push
# pnr_probe/results/micro_phys to pnr-probe only (fold files left out: they hold per-step scores).
source slurm/common.sh
R=pnr_probe/results/micro_phys
for split in unseen seen; do
    [ -f $R/$split/per_episode.json ] || continue
    for k in "fixed 0.025" "fixed 0.05"; do
        python pnr_probe/13_report.py --pred $R/$split --key "$k" --headline "fixed 0.025" "fixed 0.05" --out "$R/${split}_report_${k// /_}.md"
    done
done
python pnr_probe/micro_phys/plot_micro.py --phys pnr_probe/data/unseen/micro --pred pnr_probe/results/unseen_t1 --out $R/figure
C=$(git rev-parse --short HEAD)
echo "| $(date +%F) | micro_phys report: pnr_probe/micro_phys/submit.sh chain | $C | $R/unseen_report_fixed_0.025.md, $R/figure/summary.md | job $SLURM_JOB_ID |" >> pnr_probe/results/LOG.md
[ "$(git branch --show-current)" = pnr-probe ] || { echo "not on pnr-probe, not pushing"; exit 1; }
git add $(find $R -type f -size -50M -not -path "*/folds/*") pnr_probe/results/LOG.md pnr_probe/results/jobs.txt pnr_probe/micro_phys
git -c user.name="Fahad Qaseem Khawar" commit -qm "pnr_probe: micro_phys report (gru on Track 1 + 3 micro-events) and micro-event figure

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" || echo "nothing to commit"
for try in 1 2; do git push -q -u origin pnr-probe && { echo pushed; exit 0; }; sleep 30; done
echo "PUSH FAILED" | tee -a $R/push_failures.txt
