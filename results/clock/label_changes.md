# Clock-aware labels: label changes

Clock-aware labels (Fahad, Nov 7, item 8): t_pnr recomputed from the existing scans counting a retry as a success only if it succeeds by step 520 (the episode's own limit), with the same three rules as 32_relabel.py (Jeffreys tau 0.5, raw failure fraction >= 0.7, >= 0.8). Existing alarms are rescored without retraining: OUT/{pol}_thr{T}/per_episode.json for 13_report.py, and a count of how labels move (recoverable -> timed, timed -> doomed, ...). Unscanned failures (pre-check recoverable) keep their label.

| policy | rule | failures | old -> new label (count) |
|---|---|---|---|
| OpenVLA-OFT | 50% | 151 | doomed -> doomed (55); recoverable -> recoverable (1); recoverable -> timed (14); timed -> doomed (4); timed -> timed (77) |
| OpenVLA-OFT | 70% (main) | 151 | doomed -> doomed (41); recoverable -> recoverable (3); recoverable -> timed (16); timed -> doomed (2); timed -> timed (89) |
| OpenVLA-OFT | 80% | 151 | doomed -> doomed (26); recoverable -> recoverable (3); recoverable -> timed (20); timed -> doomed (2); timed -> timed (100) |
| Pi0.5 | 50% | 40 | doomed -> doomed (10); recoverable -> doomed (1); recoverable -> timed (2); timed -> timed (27) |
| Pi0.5 | 70% (main) | 40 | doomed -> doomed (6); recoverable -> timed (3); timed -> doomed (2); timed -> timed (29) |
| Pi0.5 | 80% | 40 | doomed -> doomed (3); recoverable -> timed (4); timed -> doomed (3); timed -> timed (30) |
