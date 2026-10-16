"""Evaluation module.

Provides batch task execution, scorers, AIS-Bench integration,
and regression metric collection for vLLM-Ascend model evaluation.
"""

from vllm_ascend_harness.evaluator.runner import EvalRunner
from vllm_ascend_harness.evaluator.scorer import BaseScorer

__all__ = ["EvalRunner", "BaseScorer"]
