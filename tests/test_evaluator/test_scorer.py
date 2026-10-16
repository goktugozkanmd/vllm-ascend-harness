"""Unit tests for ExactMatchScorer."""

from vllm_ascend_harness.evaluator.scorer import ExactMatchScorer


def test_exact_match_success():
    scorer = ExactMatchScorer()
    task = type("T", (), {"expected": "hello"})()
    assert scorer.score(task, "hello") == 1.0


def test_exact_match_fail():
    scorer = ExactMatchScorer()
    task = type("T", (), {"expected": "hello"})()
    assert scorer.score(task, "world") == 0.0


def test_exact_match_no_expected():
    scorer = ExactMatchScorer()
    task = type("T", (), {"expected": None})()
    assert scorer.score(task, "anything") == 0.0
