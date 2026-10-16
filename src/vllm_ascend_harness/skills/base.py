"""Base skill interface.

Defines the contract for all agent skills.  This is the primary
extension point for adding new capabilities to the agent.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class SkillResult:
    """Result of a skill execution."""

    output: str = ""
    success: bool = True
    metadata: dict | None = None


class BaseSkill(ABC):
    """Abstract base class for agent skills.

    Extension point: subclass and implement :meth:`execute` to
    provide a new agent capability.
    """

    name: str = "base"
    description: str = ""

    @abstractmethod
    def execute(self, **kwargs: Any) -> SkillResult:
        """Execute the skill and return a :class:`SkillResult`."""
        ...

    def __call__(self, **kwargs: Any) -> SkillResult:
        return self.execute(**kwargs)
