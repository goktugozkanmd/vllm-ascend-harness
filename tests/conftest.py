"""Pytest configuration and shared fixtures for vllm-ascend-harness."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

# Ensure src is importable in test runs without installed package
_SRC = Path(__file__).resolve().parent.parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))


@pytest.fixture
def tmp_workspace(tmp_path: Path) -> Path:
    """Provide a temporary workspace directory."""
    return tmp_path
