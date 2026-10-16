"""Task sandbox module.

Provides container isolation and command allowlist enforcement,
integrating with the "天罗地网" (sky-net) defense system to
ensure safe execution of agent-driven commands.
"""

from vllm_ascend_harness.sandbox.base import BaseSandbox
from vllm_ascend_harness.sandbox.whitelist import CommandWhitelist

__all__ = ["BaseSandbox", "CommandWhitelist"]
