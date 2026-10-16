"""Policy + LIBERO environment + one rollout function used for recording, replay tests and PNR scans.

Everything model- or env-specific comes from the official openvla-oft repo (set OFT_ROOT to your clone),
so preprocessing exactly matches the published LIBERO evaluation.
"""

from __future__ import annotations

import os
import sys
from collections import deque
from dataclasses import dataclass, field
from typing import List, Optional

import numpy as np

OFT_ROOT = os.environ.get("OFT_ROOT", os.path.expanduser("~/openvla-oft"))
if OFT_ROOT not in sys.path:
    sys.path.insert(0, OFT_ROOT)

# These imports come from the openvla-oft repo (they also pull in LIBERO, torch, etc.).
from experiments.robot.libero.libero_utils import get_libero_dummy_action, get_libero_env  # noqa: E402
from experiments.robot.libero.run_libero_eval import (  # noqa: E402
    TASK_MAX_STEPS,
    GenerateConfig,
    initialize_model,
    prepare_observation,
    process_action,
)
from experiments.robot.robot_utils import get_action, get_image_resize_size, set_seed_everywhere  # noqa: E402
from libero.libero import benchmark  # noqa: E402

# Apple Silicon: openvla-oft picks cuda:0 or falls back to CPU (very slow). Use the Mac GPU (MPS) instead.
# Both modules read their module-level DEVICE at call time, so patching it here is enough. Set PNR_DEVICE=cpu
# to disable. On Grid (CUDA) nothing changes.
import torch  # noqa: E402
import experiments.robot.openvla_utils as _oft_utils  # noqa: E402
import experiments.robot.robot_utils as _oft_robot_utils  # noqa: E402

if (not torch.cuda.is_available() and getattr(torch.backends, "mps", None) is not None
        and torch.backends.mps.is_available() and os.environ.get("PNR_DEVICE", "mps") == "mps"):
    _oft_utils.DEVICE = _oft_robot_utils.DEVICE = torch.device("mps")
DEVICE = _oft_utils.DEVICE

# The action head and proprio projector files were saved on a CUDA GPU. Without CUDA, torch.load must map them
# to the CPU first; openvla-oft then moves them to DEVICE itself. On Grid (CUDA) nothing changes.
if not torch.cuda.is_available():
    _torch_load = torch.load

    def _load_to_cpu(*args, **kwargs):
        kwargs.setdefault("map_location", "cpu")
        return _torch_load(*args, **kwargs)

    torch.load = _load_to_cpu

SUITE = "libero_10"
CHUNK = 8
WAIT_STEPS = 10

# openvla-oft guesses the robot platform from the command line text; make sure it picked LIBERO's chunk of 8.
from prismatic.vla.constants import NUM_ACTIONS_CHUNK  # noqa: E402

assert NUM_ACTIONS_CHUNK == CHUNK, f"openvla-oft chose chunk {NUM_ACTIONS_CHUNK}, expected {CHUNK} (LIBERO)"
MODEL_FAMILY = "openvla"


class Policy:
    """Loads OpenVLA-OFT once and returns an action chunk (list of 8 raw actions) per query."""

    def __init__(self, checkpoint: str = "moojink/openvla-7b-oft-finetuned-libero-10", seed: int = 7):
        self.cfg = GenerateConfig(pretrained_checkpoint=checkpoint, task_suite_name=SUITE, seed=seed)
        set_seed_everywhere(seed)
        (self.model, self.action_head, self.proprio_projector,
         self.noisy_action_projector, self.processor) = initialize_model(self.cfg)
        self.resize_size = get_image_resize_size(self.cfg)

    def act(self, obs, task_description: str) -> list:
        observation, _ = prepare_observation(obs, self.resize_size)
        return get_action(
            self.cfg, self.model, observation, task_description,
            processor=self.processor, action_head=self.action_head,
            proprio_projector=self.proprio_projector,
            noisy_action_projector=self.noisy_action_projector,
            use_film=self.cfg.use_film,
        )


def make_task(task_id: int):
    """Returns (env, task_description, initial_states[50]) for a LIBERO-10 task."""
    suite = benchmark.get_benchmark_dict()[SUITE]()
    task = suite.get_task(task_id)
    env, description = get_libero_env(task, MODEL_FAMILY, resolution=256)
    return env, description, suite.get_task_init_states(task_id)


def max_steps() -> int:
    return int(TASK_MAX_STEPS[SUITE])


@dataclass
class Rollout:
    success: bool
    t_end: int                                            # policy steps executed (excludes the 10 wait steps)
    query_steps: List[int] = field(default_factory=list)  # policy step at each model query (chunk boundary)
    query_states: List[np.ndarray] = field(default_factory=list)  # flattened MuJoCo state at each query
    actions: List[np.ndarray] = field(default_factory=list)       # executed env actions, one per step
    eef: List[np.ndarray] = field(default_factory=list)           # end-effector position after each step
    frames: List[np.ndarray] = field(default_factory=list)        # agentview frames (only if save_frames)


def rollout(env, policy: Policy, description: str, *, init_state=None, start_state=None, t0: int = 0,
            noise_std: float = 0.0, rng: Optional[np.random.Generator] = None,
            record_states: bool = True, save_frames: bool = False, limit: Optional[int] = None,
            horizon: Optional[int] = None) -> Rollout:
    """Run one episode.

    Fresh episode:  pass init_state (one of the 50 LIBERO initial states). Does the 10 wait steps first.
    Replay:         pass start_state (a saved query state) and t0 (its policy step). No wait steps.
    noise_std:      Gaussian noise added to the 6 arm action dims after processing (gripper untouched).
    limit:          stop after this many policy steps (used by the replay test).
    horizon:        last allowed policy step (default 520). PNR replays get extra time so late
                    checkpoints do not fail just because the clock ran out.
    """
    assert (init_state is None) != (start_state is None), "pass exactly one of init_state / start_state"
    rng = rng or np.random.default_rng()
    env.reset()
    if start_state is not None:
        obs = env.set_init_state(start_state)
        t = t0
    else:
        obs = env.set_init_state(init_state)
        for _ in range(WAIT_STEPS):
            obs, _, _, _ = env.step(get_libero_dummy_action(MODEL_FAMILY))
        t = 0

    out = Rollout(success=False, t_end=t)
    queue: deque = deque()
    end = max_steps() if horizon is None else horizon
    stop_at = end if limit is None else min(end, t + limit)
    while t < stop_at:
        if not queue:
            if record_states:
                out.query_steps.append(t)
                out.query_states.append(env.get_sim_state().copy())
            queue.extend(policy.act(obs, description))
        action = process_action(np.array(queue.popleft(), dtype=np.float64, copy=True), MODEL_FAMILY)
        if noise_std > 0:
            action[:6] = np.clip(action[:6] + rng.normal(0.0, noise_std, size=6), -1.0, 1.0)
        obs, _, done, _ = env.step(action.tolist())
        t += 1
        out.actions.append(action.copy())
        out.eef.append(np.array(obs["robot0_eef_pos"], dtype=np.float64))
        if save_frames:
            out.frames.append(obs["agentview_image"][::-1, ::-1].copy())
        if done:
            out.success = True
            break
    out.t_end = t
    return out


def save_episode(path: str, r: Rollout, *, task_id: int, episode_idx: int, description: str,
                 init_state, noise_std: float, seed: int) -> None:
    np.savez_compressed(
        path,
        task_id=task_id, episode_idx=episode_idx, description=description,
        success=r.success, t_end=r.t_end, noise_std=noise_std, seed=seed,
        induced=bool(noise_std > 0),
        init_state=np.asarray(init_state),
        query_steps=np.asarray(r.query_steps, dtype=np.int64),
        query_states=np.stack(r.query_states) if r.query_states else np.zeros((0,)),
        actions=np.stack(r.actions) if r.actions else np.zeros((0, 7)),
        eef=np.stack(r.eef) if r.eef else np.zeros((0, 3)),
    )
