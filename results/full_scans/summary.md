# Full replay scans: does binary search find the same t_pnr?

Natural failures, every checkpoint (8 steps), K = 4 at every checkpoint (no K = 16 expansion), noise 0.05 on 6 arm dims, extra_steps 200. Rule per checkpoint: Jeffreys lower 0.25 quantile >= tau, or 'fails every replay'.

Jeffreys lower 0.25 quantile for k of 4 successes: k=0: 0.012, k=1: 0.150, k=2: 0.345, k=3: 0.576, k=4: 0.856

| episode | rule | t_pnr full scan | t_pnr binary search | same | rebounds after first non-recoverable |
|---|---|---|---|---|---|
| t00_e08_n0 | tau 0.3 | 0 | 0 | True | 0 |
| t00_e08_n0 | tau 0.5 | 0 | 0 | True | 0 |
| t00_e08_n0 | tau 0.7 | 0 | 0 | True | 0 |
| t00_e08_n0 | fails every replay | 0 | 0 | True | 0 |
| t00_e08_n0 | successes of 4 per checkpoint | 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | | | |
| t01_e41_n0 | tau 0.3 | 192 | 176 | False | 15 |
| t01_e41_n0 | tau 0.5 | 152 | 40 | False | 6 |
| t01_e41_n0 | tau 0.7 | 152 | 0 | False | 1 |
| t01_e41_n0 | fails every replay | 232 | 232 | True | 2 |
| t01_e41_n0 | successes of 4 per checkpoint | 3 1 3 1 3 2 1 1 2 1 3 3 1 2 2 2 2 3 4 1 2 2 1 2 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | | | |
| t02_e10_n0 | tau 0.3 | 184 | 184 | True | 0 |
| t02_e10_n0 | tau 0.5 | 184 | 184 | True | 4 |
| t02_e10_n0 | tau 0.7 | 168 | 168 | True | 7 |
| t02_e10_n0 | fails every replay | 192 | 192 | True | 0 |
| t02_e10_n0 | successes of 4 per checkpoint | 4 4 4 4 3 4 4 4 4 4 3 3 3 3 3 3 4 2 3 2 4 3 3 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 | | | |
