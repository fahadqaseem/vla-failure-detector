# Pi0.5 episodes: fresh seeds 2 to 4 and the whole set

Pi0.5 episode counts (Fahad, Nov 9): per task and seed for the fresh perturbed seeds 2 to 4 (collected, gate, successes, failures, scanned failures with timed / doomed / recoverable at 50%, 70%, 80%), totals for the whole Pi0.5 set, and per held-out task of the fresh unseen test (catchable failures = t_pnr > 0, and successes, from results of the fresh report). Rules as 32_relabel.py: 50% = Jeffreys tau 0.5, 70% / 80% = raw failure fraction of the K 4 retries.

## Fresh perturbed seeds 2 to 4, per task and seed

| folder | collected | gate | successes | failures | scanned failures | timed / doomed / recoverable 50% | 70% | 80% | status |
|---|---|---|---|---|---|---|---|---|---|
| task00_s2 | 47 | pass | 42 | 5 | 5 | 3 / 2 / 0 | 4 / 1 / 0 | 4 / 0 / 1 | used |
| task00_s3 | 47 | pass | 43 | 4 | 4 | 2 / 2 / 0 | 4 / 0 / 0 | 3 / 0 / 1 | used |
| task00_s4 | 47 | pass | 41 | 6 | 2 | 1 / 1 / 0 | 1 / 1 / 0 | 0 / 1 / 1 | used |
| task01_s2 | 50 | pass | 49 | 1 | 1 | 1 / 0 / 0 | 1 / 0 / 0 | 1 / 0 / 0 | used |
| task01_s3 | 50 | pass | 48 | 2 | 1 | 1 / 0 / 0 | 1 / 0 / 0 | 1 / 0 / 0 | used |
| task01_s4 | 50 | pass | 48 | 2 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | used |
| task04_s2 | 50 | pass | 49 | 1 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | used |
| task04_s3 | 50 | FAIL | 49 | 1 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | EXCLUDED: replay gate failed |
| task04_s4 | 50 | pass | 49 | 1 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | used |
| task05_s2 | 50 | FAIL | 48 | 2 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | EXCLUDED: replay gate failed |
| task05_s3 | 13 | none | 13 | 0 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | EXCLUDED: index.csv lost its header after a reqp requeue (13 episodes), no replay gate run |
| task05_s4 | 50 | FAIL | 44 | 6 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | EXCLUDED: replay gate failed |
| task06_s2 | 47 | pass | 45 | 2 | 2 | 0 / 2 / 0 | 2 / 0 / 0 | 2 / 0 / 0 | used |
| task06_s3 | 47 | pass | 39 | 8 | 8 | 8 / 0 / 0 | 8 / 0 / 0 | 6 / 0 / 2 | used |
| task06_s4 | 48 | pass | 42 | 6 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | used |
| task07_s2 | 50 | pass | 45 | 5 | 5 | 5 / 0 / 0 | 5 / 0 / 0 | 5 / 0 / 0 | used |
| task07_s3 | 49 | pass | 47 | 2 | 2 | 2 / 0 / 0 | 2 / 0 / 0 | 2 / 0 / 0 | used |
| task07_s4 | 50 | pass | 46 | 4 | 0 | 0 / 0 / 0 | 0 / 0 / 0 | 0 / 0 / 0 | used |

Failures of used folders that are not scanned: either recoverable by pre-check (no scan, label 0) or seed 4 failures past the
70th scanned failure (pre-checked, never scanned, no label, not scored).

## Whole Pi0.5 set

| set | episodes | successes | failures | scanned failures | catchable at 50% (t_pnr > 0) |
|---|---|---|---|---|---|
| natural (used) | 500 | 475 | 25 | 9 | 5 |
| perturbed seed 0 (not used) | 300 | 270 | 30 | 0 | 0 |
| perturbed seed 0 (used) | 194 | 181 | 13 | 11 | 10 |
| perturbed seed 1 (used) | 294 | 272 | 22 | 20 | 12 |
| perturbed seed 2 (not used) | 50 | 48 | 2 | 0 | 0 |
| perturbed seed 2 (used) | 244 | 230 | 14 | 13 | 9 |
| perturbed seed 3 (not used) | 63 | 62 | 1 | 0 | 0 |
| perturbed seed 3 (used) | 193 | 177 | 16 | 15 | 13 |
| perturbed seed 4 (not used) | 50 | 44 | 6 | 0 | 0 |
| perturbed seed 4 (used) | 245 | 226 | 19 | 2 | 1 |
| all collected | 2133 | 1985 | 148 | 70 | 50 |
| analysis set (used) | 1670 | 1561 | 109 | 70 | 50 |

The natural set keeps all 10 tasks (successes of tasks 2, 3, 8, 9 are used; their failures are not scanned because the natural
gate failed). Old = natural + perturbed seeds 0 and 1 (training); fresh = perturbed seeds 2 to 4 (test).

## Fresh unseen test, per held-out task (scored episodes, from the fresh report)

| held-out task | successes | catchable 50% | catchable 70% | catchable 80% | recoverable failures 50% |
|---|---|---|---|---|---|
| 0 | 126 | 6 | 9 | 7 | 0 |
| 1 | 145 | 2 | 2 | 2 | 1 |
| 4 | 98 | 0 | 0 | 0 | 1 |
| 6 | 126 | 8 | 10 | 8 | 2 |
| 7 | 138 | 7 | 7 | 7 | 1 |
| all | 633 | 23 | 28 | 24 | 5 |
