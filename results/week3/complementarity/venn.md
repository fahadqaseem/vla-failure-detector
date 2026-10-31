# Which timed failures does each detector catch in time?

Unseen tasks, failure threshold 50%, 81 timed failures, natural + perturbed pooled. Each row counts the failures caught in time by exactly that set of detectors. A detector's false alarm rate is its own.

## fixed 0.05

Detector totals: progress 17 (false alarms 0.048), gru_phys 12 (false alarms 0.014), safe 18 (false alarms 0.147), hideseek 13 (false alarms 0.037); caught by at least one: 35 of 81.

| caught by exactly | all | missed_grasp | stuck | drop | none |
|---|---|---|---|---|---|
| progress + gru_phys + safe + hideseek | 1 | 1 | 0 | 0 | 0 |
| progress + gru_phys + safe | 1 | 1 | 0 | 0 | 0 |
| progress + gru_phys + hideseek | 2 | 0 | 0 | 0 | 2 |
| progress + safe + hideseek | 1 | 0 | 0 | 0 | 1 |
| gru_phys + safe + hideseek | 0 | 0 | 0 | 0 | 0 |
| progress + gru_phys | 0 | 0 | 0 | 0 | 0 |
| progress + safe | 0 | 0 | 0 | 0 | 0 |
| progress + hideseek | 5 | 2 | 0 | 0 | 3 |
| gru_phys + safe | 5 | 3 | 2 | 0 | 0 |
| gru_phys + hideseek | 1 | 0 | 1 | 0 | 0 |
| safe + hideseek | 3 | 2 | 0 | 0 | 1 |
| progress | 7 | 5 | 0 | 0 | 2 |
| gru_phys | 2 | 1 | 1 | 0 | 0 |
| safe | 7 | 5 | 1 | 0 | 1 |
| hideseek | 0 | 0 | 0 | 0 | 0 |
| none | 46 | 30 | 12 | 2 | 2 |

## fixed 0.025

Detector totals: progress 11 (false alarms 0.025), gru_phys 10 (false alarms 0.014), safe 13 (false alarms 0.077), hideseek 11 (false alarms 0.025); caught by at least one: 28 of 81.

| caught by exactly | all | missed_grasp | stuck | drop | none |
|---|---|---|---|---|---|
| progress + gru_phys + safe + hideseek | 1 | 1 | 0 | 0 | 0 |
| progress + gru_phys + safe | 0 | 0 | 0 | 0 | 0 |
| progress + gru_phys + hideseek | 2 | 0 | 0 | 0 | 2 |
| progress + safe + hideseek | 0 | 0 | 0 | 0 | 0 |
| gru_phys + safe + hideseek | 0 | 0 | 0 | 0 | 0 |
| progress + gru_phys | 0 | 0 | 0 | 0 | 0 |
| progress + safe | 0 | 0 | 0 | 0 | 0 |
| progress + hideseek | 3 | 1 | 0 | 0 | 2 |
| gru_phys + safe | 4 | 2 | 2 | 0 | 0 |
| gru_phys + hideseek | 0 | 0 | 0 | 0 | 0 |
| safe + hideseek | 3 | 1 | 0 | 0 | 2 |
| progress | 5 | 3 | 0 | 0 | 2 |
| gru_phys | 3 | 2 | 1 | 0 | 0 |
| safe | 5 | 4 | 1 | 0 | 0 |
| hideseek | 2 | 1 | 1 | 0 | 0 |
| none | 53 | 35 | 12 | 2 | 4 |

