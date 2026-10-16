"""Scorer interfaces.

Defines the contract for evaluating model outputs.  This is the
primary extension point for custom scoring strategies (exact-match,
LLM-judge, AIS-Bench metrics, etc.).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseScorer(ABC):
    """Abstract base class for scorers.

    Extension point: subclass and implement :meth:`score` to provide
    a custom scoring strategy.
    """

    name: str = "base"

    @abstractmethod
    def score(self, task: Any, output: str) -> float:
        """Return a score in [0, 1] for *output* given *task*."""
        ...

    def batch_score(self, tasks: list[Any], outputs: list[str]) -> list[float]:
        """Score a batch of task/output pairs.

        TODO: add parallel scoring support.
        """
        if len(tasks) != len(outputs):
            raise ValueError("tasks and outputs must have equal length")
        return [self.score(t, o) for t, o in zip(tasks, outputs)]


class ExactMatchScorer(BaseScorer):
    """Simple exact-match scorer."""

    name = "exact-match"

    def score(self, task: Any, output: str) -> float:
        expected = getattr(task, "expected", None)
        if expected is None:
            return 0.0
        return 1.0 if output.strip() == expected.strip() else 0.0
