"""AIS-Bench integration layer.

Provides integration with the AIS-Bench evaluation framework for
collecting standardised regression metrics on Ascend NPU.

TODO: implement AIS-Bench task adapter and metric exporter.
"""

from __future__ import annotations

from typing import Any

from vllm_ascend_harness.evaluator.scorer import BaseScorer


class AISBenchScorer(BaseScorer):
    """Scorer that delegates to the AIS-Bench evaluation framework.

    TODO: implement AIS-Bench metric computation and export.
    """

    name = "ais-bench"

    def __init__(self, metric: str = "accuracy") -> None:
        self.metric = metric

    def score(self, task: Any, output: str) -> float:
        """Compute AIS-Bench metric for *output*.

        TODO: call AIS-Bench evaluation API.
        """
        raise NotImplementedError("AIS-Bench integration pending")
