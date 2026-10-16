"""Command allowlist enforcement.

Defines and enforces the set of commands permitted inside the
sandbox, blocking dangerous or unauthorised operations.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CommandWhitelist:
    """Allowlist of permitted sandbox commands.

    TODO: load from YAML config and support glob patterns.
    """

    allowed: list[str] | None = None
    blocked: list[str] | None = None

    def __post_init__(self) -> None:
        if self.allowed is None:
            self.allowed = ["ls", "cat", "python", "pytest", "git", "ruff"]
        if self.blocked is None:
            self.blocked = ["rm -rf /", "sudo", "curl", "wget", "chmod 777"]

    def is_allowed(self, command: str) -> bool:
        """Return whether *command* is permitted.

        TODO: implement robust parsing and pattern matching.
        """
        base = command.strip().split()[0] if command.strip() else ""
        blocked = self.blocked or []
        allowed = self.allowed or []
        if any(b in command for b in blocked):
            return False
        return base in allowed
