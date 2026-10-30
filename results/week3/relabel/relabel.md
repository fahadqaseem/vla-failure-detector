# t_pnr at other failure thresholds

t_pnr recomputed from the existing scans at failure thresholds 50, 70, 80% (Prof. Zhu meeting, Oct 30). Replay data only, no new runs. Same failures as T1all (natural + perturbed + perturbed_v2, refined counts). A checkpoint is not recoverable if the raw failure fraction is at least the threshold; t_pnr = first checkpoint from which every later one is not recoverable. With K = 4 that is 70% = 3 of 4 fail, 80% = 4 of 4 fail. 50% = the labels in use (Jeffreys tau 0.5), checked against T1all. Also shown: the Jeffreys rule at tau 0.3 and 0.2. Pre-check failures have no scan and stay recoverable at every threshold. Timed = t_pnr > 0, doomed = t_pnr 0.

| rule | timed | doomed | recoverable | natural timed / doomed / recov | perturbed timed / doomed / recov | timed in both | median shift (steps) | 25 to 75% | timed -> recoverable | doomed -> timed |
|---|---|---|---|---|---|---|---|---|---|---|
| 50% (labels in use) | 81 | 55 | 31 | 11 / 3 / 14 | 70 / 52 / 17 | 81 | +0 | +0 to +0 | 0 | 0 |
| 70% (3 of 4 fail) | 91 | 41 | 35 | 10 / 2 / 16 | 81 / 39 / 19 | 77 | +48 | +16 to +96 | 4 | 14 |
| 80% (4 of 4 fail) | 102 | 26 | 39 | 8 / 2 / 18 | 94 / 24 / 21 | 73 | +80 | +24 to +168 | 8 | 29 |
| Jeffreys tau 0.3 | 92 | 41 | 34 | 10 / 2 / 16 | 82 / 39 / 18 | 78 | +48 | +8 to +96 | 3 | 14 |
| Jeffreys tau 0.2 | 91 | 41 | 35 | 10 / 2 / 16 | 81 / 39 / 19 | 77 | +48 | +16 to +96 | 4 | 14 |
