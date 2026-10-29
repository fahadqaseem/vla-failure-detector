#!/bin/bash
# Per-chunk dense replay (Oct 28 2026), CPU only, jobs probe-*: replay array (dense_chunk_replay.py) -> gate
# (pass rates by class, pushed; continues to features / training / report only if timed failures pass >= 90%).
set -e
cd ~/vla-probe; mkdir -p pnr_probe/logs pnr_probe/results/dense_chunk
N=$(wc -l < pnr_probe/dense/all_episodes.txt); CHUNK=25
sub() { sbatch --parsable "$@"; }
A=$(sub --array=0-$(((N + CHUNK - 1) / CHUNK - 1)) -J probe-chunk-replay -t 12:00:00 --export=ALL,CHUNK=$CHUNK,SCRIPT=dense_chunk_replay.py,OUT=pnr_probe/data/dense_chunk pnr_probe/dense/replay_array.sbatch)
G=$(sub --dependency=afterany:$A -J probe-chunk-gate pnr_probe/dense/chunk_gate.sbatch)
echo "$(date +%F) dense_chunk: $N episodes, replay $A gate $G" | tee -a pnr_probe/results/jobs.txt
