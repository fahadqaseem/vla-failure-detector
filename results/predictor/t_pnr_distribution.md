# t_pnr over scanned natural failures (full scans, K 4, tau 0.5)

| episode | task | t_pnr | t_pnr / 520 |
|---|---|---|---|
| t00_e08_n0 | 0 | 0 | 0.00 |
| t00_e14_n0 | 0 | 288 | 0.55 |
| t00_e27_n0 | 0 | 0 | 0.00 |
| t00_e42_n0 | 0 | 0 | 0.00 |
| t01_e41_n0 | 1 | 176 | 0.34 |
| t02_e10_n0 | 2 | 184 | 0.35 |
| t03_e37_n0 | 3 | None |  |
| t03_e43_n0 | 3 | None |  |
| t04_e11_n0 | 4 | 184 | 0.35 |
| t06_e20_n0 | 6 | None |  |
| t06_e23_n0 | 6 | 472 | 0.91 |
| t06_e25_n0 | 6 | 464 | 0.89 |
| t06_e26_n0 | 6 | 312 | 0.60 |
| t06_e27_n0 | 6 | 464 | 0.89 |
| t06_e28_n0 | 6 | None |  |
| t08_e04_n0 | 8 | 488 | 0.94 |
| t08_e06_n0 | 8 | None |  |
| t08_e08_n0 | 8 | None |  |
| t08_e11_n0 | 8 | None |  |
| t08_e12_n0 | 8 | None |  |
| t08_e20_n0 | 8 | None |  |
| t08_e27_n0 | 8 | None |  |
| t08_e30_n0 | 8 | None |  |
| t08_e38_n0 | 8 | 264 | 0.51 |
| t08_e45_n0 | 8 | None |  |
| t08_e47_n0 | 8 | None |  |
| t09_e25_n0 | 9 | 176 | 0.34 |
| t09_e34_n0 | 9 | None |  |

28 failures: 11 with t_pnr > 0, 3 doomed from start (t_pnr 0), 14 recoverable (no t_pnr).
t_pnr > 0: min 176, 25% 184, median 288, 75% 464, max 488 (steps).
Per task (t_pnr > 0 / doomed / recoverable): t0: 1/3/0, t1: 1/0/0, t2: 1/0/0, t3: 0/0/2, t4: 1/0/0, t6: 4/0/2, t8: 2/0/9, t9: 1/0/1
