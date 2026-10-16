"""Built-in skills module.

Provides a collection of tool skills that the agent can invoke:
code reading, PR review, command execution, etc.
"""

from vllm_ascend_harness.skills.base import BaseSkill

__all__ = ["BaseSkill"]
