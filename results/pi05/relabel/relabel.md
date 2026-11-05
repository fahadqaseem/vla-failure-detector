# t_pnr at other failure thresholds

t_pnr recomputed from the existing scans at failure thresholds 50, 70, 80% (Prof. Zhu meeting, Oct 30). Replay data only, no new runs. Pi0.5: failures of results/pi05/all_* (natural + perturbed 2 to 3 cm, seeds 0 and 1, gate-passed tasks), no refinement. A checkpoint is not recoverable if the raw failure fraction is at least the threshold; t_pnr = first checkpoint from which every later one is not recoverable. With K = 4 that is 70% = 3 of 4 fail, 80% = 4 of 4 fail. 50% = the labels in use (Jeffreys tau 0.5), checked against --labels. Also shown: the Jeffreys rule at tau 0.3 and 0.2. Pre-check failures have no scan and stay recoverable at every threshold. Timed = t_pnr > 0, doomed = t_pnr 0.

| rule | timed | doomed | recoverable | natural timed / doomed / recov | perturbed timed / doomed / recov | timed in both | median shift (steps) | 25 to 75% | timed -> recoverable | doomed -> timed |
|---|---|---|---|---|---|---|---|---|---|---|
| 50% (labels in use) | 27 | 10 | 7 | 5 / 1 / 3 | 22 / 9 / 4 | 27 | +0 | +0 to +0 | 0 | 0 |
| 70% (3 of 4 fail) | 31 | 6 | 7 | 5 / 1 / 3 | 26 / 5 / 4 | 27 | +24 | +0 to +76 | 0 | 4 |
| 80% (4 of 4 fail) | 33 | 3 | 8 | 5 / 1 / 3 | 28 / 2 / 5 | 27 | +56 | +12 to +188 | 0 | 6 |
| Jeffreys tau 0.3 | 31 | 6 | 7 | 5 / 1 / 3 | 26 / 5 / 4 | 27 | +24 | +0 to +76 | 0 | 4 |
| Jeffreys tau 0.2 | 31 | 6 | 7 | 5 / 1 / 3 | 26 / 5 / 4 | 27 | +24 | +0 to +76 | 0 | 4 |
