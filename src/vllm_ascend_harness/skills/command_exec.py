"""Command execution skill.

Executes shell commands inside a sandbox, returning stdout/stderr.

TODO: integrate with sandbox module for isolation.
"""

from __future__ import annotations

from typing import Any

from vllm_ascend_harness.skills.base import BaseSkill, SkillResult


class CommandExecSkill(BaseSkill):
    """Skill that executes shell commands in a sandbox."""

    name = "command_exec"
    description = "Execute a shell command inside the sandbox."

    def __init__(self, sandbox: Any | None = None) -> None:
        self.sandbox = sandbox

    def execute(self, command: str = "", timeout: int = 60, **kwargs: Any) -> SkillResult:
        """Execute *command* inside the sandbox.

        TODO: wire to sandbox.run() and format output.
        """
        if self.sandbox is None:
            return SkillResult(output="No sandbox configured", success=False)
        result = self.sandbox.run(command, timeout=timeout)
        return SkillResult(
            output=result.stdout,
            success=(result.exit_code == 0),
            metadata={"exit_code": result.exit_code, "stderr": result.stderr},
        )
