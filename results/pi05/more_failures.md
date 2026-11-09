| set | folder | gate | episodes | failures | scanned | timed t_pnr | doomed | recoverable (scanned) | recoverable by pre-check (not scanned) |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| natural | task00 | pass | 50 | 2 | 2 | 1 | 1 | 0 | 0 |
| natural | task01 | pass | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| natural | task02 | FAIL | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| natural | task03 | FAIL | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| natural | task04 | pass | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| natural | task05 | pass | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| natural | task06 | pass | 50 | 4 | 4 | 4 | 0 | 0 | 0 |
| natural | task07 | pass | 50 | 3 | 3 | 0 | 0 | 3 | 0 |
| natural | task08 | FAIL | 50 | 13 | 0 | 0 | 0 | 0 | 0 |
| natural | task09 | FAIL | 50 | 3 | 0 | 0 | 0 | 0 | 0 |
| **natural** | all | | 500 | 25 | 9 | 5 | 1 | 3 | 0 |
| perturbed | task00 | pass | 47 | 2 | 1 | 0 | 1 | 0 | 1 |
| perturbed | task00_s1 | pass | 47 | 6 | 6 | 1 | 5 | 0 | 0 |
| perturbed | task00_s2 | pass | 47 | 5 | 5 | 3 | 2 | 0 | 0 |
| perturbed | task00_s3 | pass | 47 | 4 | 4 | 2 | 2 | 0 | 0 |
| perturbed | task00_s4 | pass | 47 | 6 | 2 | 1 | 1 | 0 | 0 |
| perturbed | task01 | pass | 50 | 3 | 3 | 3 | 0 | 0 | 0 |
| perturbed | task01_s1 | pass | 50 | 2 | 2 | 1 | 1 | 0 | 0 |
| perturbed | task01_s2 | pass | 50 | 1 | 1 | 1 | 0 | 0 | 0 |
| perturbed | task01_s3 | pass | 50 | 2 | 1 | 1 | 0 | 0 | 1 |
| perturbed | task01_s4 | pass | 50 | 2 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task02 | FAIL | 50 | 4 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task03 | FAIL | 50 | 2 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task04 | pass | 50 | 4 | 3 | 3 | 0 | 0 | 1 |
| perturbed | task04_s1 | pass | 50 | 1 | 1 | 1 | 0 | 0 | 0 |
| perturbed | task04_s2 | pass | 50 | 1 | 0 | 0 | 0 | 0 | 1 |
| perturbed | task04_s3 | FAIL | 50 | 1 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task04_s4 | pass | 50 | 1 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task05 | FAIL | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task05_s1 | pass | 50 | 0 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task05_s2 | FAIL | 50 | 2 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task05_s3 | none | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task05_s4 | FAIL | 50 | 6 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task06 | pass | 47 | 4 | 4 | 4 | 0 | 0 | 0 |
| perturbed | task06_s1 | pass | 47 | 7 | 7 | 5 | 2 | 0 | 0 |
| perturbed | task06_s2 | pass | 47 | 2 | 2 | 0 | 2 | 0 | 0 |
| perturbed | task06_s3 | pass | 47 | 8 | 8 | 8 | 0 | 0 | 0 |
| perturbed | task06_s4 | pass | 48 | 6 | 0 | 0 | 0 | 0 | 2 |
| perturbed | task07 | FAIL | 50 | 3 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task07_s1 | pass | 50 | 6 | 4 | 4 | 0 | 0 | 2 |
| perturbed | task07_s2 | pass | 50 | 5 | 5 | 5 | 0 | 0 | 0 |
| perturbed | task07_s3 | pass | 49 | 2 | 2 | 2 | 0 | 0 | 0 |
| perturbed | task07_s4 | pass | 50 | 4 | 0 | 0 | 0 | 0 | 1 |
| perturbed | task08 | FAIL | 50 | 18 | 0 | 0 | 0 | 0 | 0 |
| perturbed | task09 | FAIL | 50 | 3 | 0 | 0 | 0 | 0 | 0 |
| **perturbed** | all | | 1620 | 123 | 61 | 45 | 16 | 0 | 9 |
| **perturbed_l2** | all | | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Counting (Nov 9): "scanned" (the 40 and 70 targets) counts failures with a full replay scan only. A failure whose pre-check says
recoverable (3 or more of 4 retries succeed near the end) gets no scan: it is labelled recoverable (0 at every step) but is not in the
scanned count, so it appears in the last column, not under "recoverable (scanned)". The old Pi0.5 total of 44 failures
(results/pi05/relabel) = 40 scanned + 4 recoverable by pre-check (seeds 0 and 1), and its 7 recoverable = 3 scanned natural failures
with no t_pnr + those 4. Same rule (tau 0.5), different counting; nothing was relabelled. Seed 4 failures past the 70th were
pre-checked but not scanned (the chain stops at 70), so they have no label and are left out of training and evaluation.
data/pi05/perturbed/task05_s3 (13 episodes, index.csv without header after a reqp requeue, no gate) is left out everywhere.
