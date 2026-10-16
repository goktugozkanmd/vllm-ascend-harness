"""Agent execution main loop.

The AgentLoop is the central execution driver. It orchestrates the
plan-act-observe cycle, dispatches skills, and integrates with the
event bus and telemetry subsystems.

Design inherits from OpenHarness's agent loop abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentStep:
    """A single step in the agent execution trajectory."""

    skill: str
    input: Any
    output: Any = None
    metadata: dict = field(default_factory=dict)


@dataclass
class AgentContext:
    """Shared context carried across agent execution steps."""

    task_id: str
    prompt: str
    steps: list[AgentStep] = field(default_factory=list)
    max_steps: int = 20
    metadata: dict = field(default_factory=dict)


class AgentLoop(ABC):
    """Abstract agent execution main loop.

    Concrete implementations drive the plan-act-observe cycle for a
    given backend (e.g. vllm-ascend).  Subclass and implement
    :meth:`step` to provide backend-specific reasoning/action logic.
    """

    def __init__(self, context: AgentContext, event_bus: Any | None = None) -> None:
        self.context = context
        self.event_bus = event_bus

    @abstractmethod
    def step(self) -> AgentStep:
        """Execute a single agent step (plan -> act -> observe).

        Returns:
            The completed :class:`AgentStep`.
        """
        ...

    def run(self) -> list[AgentStep]:
        """Run the agent loop to completion.

        Iterates :meth:`step` until the agent signals completion or
        ``max_steps`` is reached.
        """
        # TODO: implement completion-detection logic
        while len(self.context.steps) < self.context.max_steps:
            step = self.step()
            self.context.steps.append(step)
            if self._is_done(step):
                break
        return self.context.steps

    def _is_done(self, step: AgentStep) -> bool:
        """Determine whether the agent should stop after *step*.

        TODO: implement stop-condition logic (e.g. sentinel skill
        output, tool-finish signal).
        """
        return False
