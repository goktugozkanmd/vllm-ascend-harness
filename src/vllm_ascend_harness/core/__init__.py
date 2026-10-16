"""Core micro-kernel: agent loop, event bus, plugin manager.

Inherits OpenHarness design philosophy.
"""

from vllm_ascend_harness.core.agent_loop import AgentLoop
from vllm_ascend_harness.core.event_bus import EventBus
from vllm_ascend_harness.core.plugin_manager import PluginManager

__all__ = ["AgentLoop", "EventBus", "PluginManager"]
