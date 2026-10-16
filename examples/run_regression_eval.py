#!/usr/bin/env python
"""Example: run a nightly regression evaluation.

Demonstrates the EvalRunner with a stub adapter and exact-match scorer.
Replace the adapter with VllmAscendAdapter for real Ascend NPU evaluation.

Usage:
    python examples/run_regression_eval.py
"""

from __future__ import annotations

import argparse
import sys

from vllm_ascend_harness.adapters.base import (
    BaseModelAdapter,
    GenerationRequest,
    GenerationResult,
)
from vllm_ascend_harness.evaluator.runner import EvalRunner, EvalTask
from vllm_ascend_harness.evaluator.scorer import ExactMatchScorer


class StubAdapter(BaseModelAdapter):
    """Minimal stub adapter for demonstration."""

    name = "stub"

    def generate(self, request: GenerationRequest) -> GenerationResult:
        return GenerationResult(
            text=request.prompt,
            prompt_tokens=len(request.prompt.split()),
            completion_tokens=len(request.prompt.split()),
        )


def build_tasks() -> list[EvalTask]:
    """Build a small set of regression tasks.

    TODO: load from YAML/JSON config in real usage.
    """
    return [
        EvalTask(task_id="reg-001", prompt="hello", expected="hello"),
        EvalTask(task_id="reg-002", prompt="world", expected="world"),
        EvalTask(task_id="reg-003", prompt="vllm", expected="ascend"),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Run nightly regression evaluation")
    parser.add_argument("--config", default=None, help="Path to regression config (YAML)")
    args = parser.parse_args()

    adapter = StubAdapter()
    scorer = ExactMatchScorer()
    runner = EvalRunner(adapter=adapter, scorer=scorer)

    # TODO: load tasks from config when provided
    tasks = build_tasks()
    report = runner.run(tasks)

    print(f"Tasks evaluated: {len(report.results)}")
    for r in report.results:
        print(f"  {r.task_id}: score={r.score:.2f}  output={r.output!r}")
    print("\nRegression evaluation complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
