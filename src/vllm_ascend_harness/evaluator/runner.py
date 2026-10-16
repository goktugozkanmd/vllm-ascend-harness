"""Batch evaluation runner.

Drives batch execution of evaluation tasks across a dataset,
collecting per-task results and aggregate metrics.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from vllm_ascend_harness.adapters.base import BaseModelAdapter, GenerationRequest


@dataclass
class EvalTask:
    """A single evaluation task."""

    task_id: str
    prompt: str
    expected: str | None = None
    metadata: dict = field(default_factory=dict)


@dataclass
class EvalResult:
    """Result of a single evaluation task."""

    task_id: str
    output: str = ""
    score: float = 0.0
    metadata: dict = field(default_factory=dict)


@dataclass
class EvalReport:
    """Aggregate report across all evaluation tasks."""

    results: list[EvalResult] = field(default_factory=list)
    aggregate_score: float = 0.0

    # TODO: add per-category breakdown and regression diff


class EvalRunner:
    """Batch evaluation runner.

    Iterates tasks, invokes the model adapter, applies scorers,
    and aggregates results into an :class:`EvalReport`.
    """

    def __init__(
        self,
        adapter: BaseModelAdapter,
        scorer: Any | None = None,
    ) -> None:
        self.adapter = adapter
        self.scorer = scorer

    def run(self, tasks: list[EvalTask]) -> EvalReport:
        """Execute all *tasks* and return an aggregate report.

        TODO: add parallel execution, retry, and checkpointing.
        """
        results: list[EvalResult] = []
        for task in tasks:
            request = GenerationRequest(prompt=task.prompt)
            gen_result = self.adapter.generate(request)
            score = 0.0
            if self.scorer is not None:
                # TODO: call scorer.score(task, gen_result)
                pass
            results.append(
                EvalResult(
                    task_id=task.task_id,
                    output=gen_result.text,
                    score=score,
                )
            )
        # TODO: compute aggregate score
        return EvalReport(results=results)
