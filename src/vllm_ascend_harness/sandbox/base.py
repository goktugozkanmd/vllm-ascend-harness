"""Base sandbox interface.

Defines the contract for isolated task execution environments
(container-based or process-based).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SandboxResult:
    """Result of a sandboxed command execution."""

    exit_code: int
    stdout: str = ""
    stderr: str = ""
    duration_ms: int = 0
    metadata: dict | None = None


class BaseSandbox(ABC):
    """Abstract sandbox for isolated command execution.

    Extension point: implement container-based or process-based
    isolation strategies.
    """

    @abstractmethod
    def run(self, command: str, timeout: int = 60) -> SandboxResult:
        """Execute *command* inside the sandbox.

        TODO: enforce resource limits and network policies.
        """
        ...

    @abstractmethod
    def setup(self) -> None:
        """Prepare the sandbox environment (e.g. start container)."""
        ...

    @abstractmethod
    def teardown(self) -> None:
        """Destroy the sandbox environment."""
        ...

    def __enter__(self) -> "BaseSandbox":
        self.setup()
        return self

    def __exit__(self, *exc: object) -> None:
        self.teardown()
