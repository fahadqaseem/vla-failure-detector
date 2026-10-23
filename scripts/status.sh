#!/bin/bash
# Week 2 status in under 15 lines: jobs running / pending / failed, and which results exist. bash scripts/status.sh
cd "$(dirname "$0")/.."
echo "== $(date '+%F %H:%M') on $(hostname)"
squeue -u $USER -h -o "%T %j" | grep -v VSCode | awk '{n[$1]++; j[$1]=j[$1]" "$2} END{for(s in n) printf "%s %d:%s\n", s, n[s], substr(j[s],1,110)}'
F=$(sacct -S now-3days -X -n -o JobName%30,State | grep -E "w2-|pnr-" | grep -vE "COMPLETED|RUNNING|PENDING|CANCELLED" | awk '{print $1"("$2")"}' | sort | uniq -c | tr '\n' ' ')
echo "failed (3 days): ${F:-none}"
n() { ls $1 2>/dev/null | wc -l; }
echo "A: episodes $(n 'data/perturbed_v2/task*/*.npz') of 700, gate pass $(n 'data/perturbed_v2/task*/GATE_PASS') fail $(n 'data/perturbed_v2/task*/GATE_FAIL'), prechecks $(n 'data/perturbed_v2/prechecks/*.json'), scans $(n 'data/perturbed_v2_scans/*.json') of $(grep -c . results/week2/scans/targets.txt 2>/dev/null || echo '?'), refined $(n 'data/week2_refine/*.json') of $(grep -c . results/week2/refine/targets.txt 2>/dev/null || echo '?')"
echo "B: lookahead $(n 'data/week2_lookahead/*.npz') of $(grep -c . results/week2/lookahead/targets.txt 2>/dev/null || echo '?'), mlp-scored $(n 'data/week2_lookahead_mlp/*.npz')"
echo "results/week2: $(ls results/week2 2>/dev/null | grep -E 'report|best|changes' | tr '\n' ' ' | cut -c1-200)"
[ -f results/week2/push_failures.txt ] && echo "PUSH FAILURES: $(wc -l < results/week2/push_failures.txt)"
echo "git: $(git log --oneline -1 | cut -c1-60), unpushed $(git rev-list --count origin/main..HEAD 2>/dev/null)"
