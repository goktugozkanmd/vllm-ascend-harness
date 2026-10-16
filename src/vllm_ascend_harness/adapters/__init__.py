"""Model backend adapters.

Provides a uniform interface for different LLM inference backends.
The vllm-ascend adapter is the primary target.
"""

from vllm_ascend_harness.adapters.base import BaseModelAdapter

__all__ = ["BaseModelAdapter"]
