"""vLLM-Ascend inference backend adapter.

Primary adapter target — wraps the vllm-ascend inference engine
to satisfy the :class:`BaseModelAdapter` contract for Ascend NPU.
"""

from __future__ import annotations

from typing import Iterator

from vllm_ascend_harness.adapters.base import (
    BaseModelAdapter,
    GenerationRequest,
    GenerationResult,
)


class VllmAscendAdapter(BaseModelAdapter):
    """Adapter for the vllm-ascend inference backend.

    TODO: integrate vllm-ascend engine for Ascend NPU inference.
    """

    name = "vllm-ascend"

    def __init__(self, model: str, **kwargs: object) -> None:
        self.model = model
        self._engine = None
        # TODO: initialise vllm-ascend LLM engine
        raise NotImplementedError("vllm-ascend engine integration pending")

    def generate(self, request: GenerationRequest) -> GenerationResult:
        """Generate a completion via the vllm-ascend engine.

        TODO: call self._engine.generate(...) and map to GenerationResult.
        """
        raise NotImplementedError

    def stream(self, request: GenerationRequest) -> Iterator[GenerationResult]:
        """Stream tokens from the vllm-ascend engine.

        TODO: implement async streaming.
        """
        raise NotImplementedError

    def health_check(self) -> bool:
        """Probe vllm-ascend engine readiness.

        TODO: query engine health endpoint.
        """
        return self._engine is not None
