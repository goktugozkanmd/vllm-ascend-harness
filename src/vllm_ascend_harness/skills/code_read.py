"""Code reading skill.

Reads file contents from the workspace for agent analysis.

TODO: implement path validation and size limits.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from vllm_ascend_harness.skills.base import BaseSkill, SkillResult


class CodeReadSkill(BaseSkill):
    """Skill that reads file contents from the workspace."""

    name = "code_read"
    description = "Read the contents of a file in the workspace."

    def execute(self, file_path: str = "", **kwargs: Any) -> SkillResult:
        """Read *file_path* and return its contents.

        TODO: enforce workspace boundary and file size limits.
        """
        path = Path(file_path)
        if not path.exists():
            return SkillResult(output=f"File not found: {file_path}", success=False)
        try:
            content = path.read_text(encoding="utf-8")
            return SkillResult(output=content)
        except Exception as exc:
            return SkillResult(output=str(exc), success=False)
