"""Artifact collection utilities.

Collects and organises output artifacts (logs, traces, results)
produced during agent and evaluation runs.

TODO: implement artifact store with local and remote backends.
"""

from __future__ import annotations

from pathlib import Path


class ArtifactCollector:
    """Collects run artifacts to a local directory.

    TODO: add remote upload (S3 / OBS) and retention policies.
    """

    def __init__(self, base_dir: str | Path = "artifacts") -> None:
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save(self, run_id: str, name: str, content: str) -> Path:
        """Save *content* as artifact *name* under *run_id*."""
        run_dir = self.base_dir / run_id
        run_dir.mkdir(parents=True, exist_ok=True)
        path = run_dir / name
        path.write_text(content, encoding="utf-8")
        return path

    def list_artifacts(self, run_id: str) -> list[Path]:
        """List artifacts for *run_id*."""
        run_dir = self.base_dir / run_id
        if not run_dir.exists():
            return []
        return sorted(run_dir.iterdir())
