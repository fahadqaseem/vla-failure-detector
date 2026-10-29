# pi0 diagnosis: success on tasks 0, 8 (initial states 0 to 9)

| setting | task 0 | task 8 | overall |
|---|---|---|---|
| lerobot-eval default (50 steps, 360 px), our env (LIBERO repo, robosuite 1.4.1, mujoco 3.3.0) | 0/10 | 3/10 | 3/20 = 15% |
| ours, 5 steps per query | 2/10 | 1/10 | 3/20 = 15% |
| ours, 8 steps per query | 1/10 | 2/10 | 3/20 = 15% |
| ours, 50 steps per query | 0/10 | 1/10 | 1/20 = 5% |
