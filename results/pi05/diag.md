# pi05 diagnosis: success on tasks 0, 8 (initial states 0 to 9)

| setting | task 0 | task 8 | overall |
|---|---|---|---|
| lerobot-eval default (50 steps, 360 px), our env (LIBERO repo, robosuite 1.4.1, mujoco 3.3.0) | 8/10 | 9/10 | 17/20 = 85% |
| lerobot-eval default (50 steps, 360 px), LeRobot docs env (hf-libero 0.1.4, robosuite 1.4.0, mujoco 3.3.0) | 8/10 | 9/10 | 17/20 = 85% |
| lerobot-eval default (50 steps, 360 px), LeRobot docs env with mujoco 2.3.7 | 8/10 | 8/10 | 16/20 = 80% |
