"""Token usage statistics collector.

Tracks prompt and completion token usage across agent steps and
evaluation runs for cost and resource observability.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TokenStats:
    """Aggregated token usage statistics."""

    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_calls: int = 0


class TokenStatsCollector:
    """Collects and aggregates token usage across runs.

    TODO: add persistence and time-series export.
    """

    def __init__(self) -> None:
        self._stats: dict[str, TokenStats] = {}

    def record(self, run_id: str, prompt_tokens: int, completion_tokens: int) -> None:
        """Record token usage for *run_id*."""
        stats = self._stats.setdefault(run_id, TokenStats())
        stats.prompt_tokens += prompt_tokens
        stats.completion_tokens += completion_tokens
        stats.total_calls += 1

    def get(self, run_id: str) -> TokenStats | None:
        """Return accumulated stats for *run_id*."""
        return self._stats.get(run_id)

    def summary(self) -> dict[str, TokenStats]:
        """Return all collected stats."""
        return dict(self._stats)
