#!/usr/bin/env python
"""Example: run a single-turn agent task.

Demonstrates the basic agent loop with a dummy adapter.
Replace the adapter with VllmAscendAdapter when Ascend NPU is available.

Usage:
    python examples/run_agent.py --prompt "Hello, vllm-ascend!"
"""

from __future__ import annotations

import argparse
import sys

from vllm_ascend_harness.adapters.base import (
    BaseModelAdapter,
    GenerationRequest,
    GenerationResult,
)
from vllm_ascend_harness.core.agent_loop import AgentContext, AgentLoop


class StubAdapter(BaseModelAdapter):
    """Minimal stub adapter for demonstration."""

    name = "stub"

    def generate(self, request: GenerationRequest) -> GenerationResult:
        return GenerationResult(
            text=f"[stub] {request.prompt}",
            prompt_tokens=len(request.prompt.split()),
            completion_tokens=5,
        )


class StubAgentLoop(AgentLoop):
    """Minimal agent loop that runs one step then stops."""

    def step(self):
        from vllm_ascend_harness.core.agent_loop import AgentStep

        adapter: BaseModelAdapter = self.context.metadata.get("adapter")
        req = GenerationRequest(prompt=self.context.prompt)
        result = adapter.generate(req)
        return AgentStep(skill="generate", input=self.context.prompt, output=result.text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a single-turn agent task")
    parser.add_argument("--prompt", default="Hello, vllm-ascend!", help="Prompt text")
    args = parser.parse_args()

    adapter = StubAdapter()
    context = AgentContext(
        task_id="demo-001",
        prompt=args.prompt,
        max_steps=1,
        metadata={"adapter": adapter},
    )
    loop = StubAgentLoop(context)
    steps = loop.run()

    for s in steps:
        print(f"skill={s.skill}  output={s.output}")
    print("\nAgent task complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
