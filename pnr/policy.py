"""Policy backend for the pipeline scripts (Track 2, Oct 23 2026): PNR_POLICY=oft (default, OpenVLA-OFT, pnr/sim.py)
or pi0 / pi05 (LeRobot Pi0 / Pi0.5, pnr/sim_pi.py, env ~/envs/pi). Both give the same names."""

import os

if os.environ.get("PNR_POLICY", "oft") == "oft":
    from pnr.sim import (CHUNK, DETERMINISTIC, REPLAY_START, Policy, make_task, max_steps,  # noqa: F401
                         restore_query, rollout, save_episode)
else:
    from pnr.sim_pi import (CHUNK, DETERMINISTIC, REPLAY_START, Policy, make_task, max_steps,  # noqa: F401
                            restore_query, rollout, save_episode)
