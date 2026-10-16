"""Unit tests for base adapter interface."""

from vllm_ascend_harness.adapters.base import (
    BaseModelAdapter,
    GenerationRequest,
    GenerationResult,
)


class DummyAdapter(BaseModelAdapter):
    name = "dummy"

    def generate(self, request):
        return GenerationResult(text="ok", prompt_tokens=2, completion_tokens=1)


def test_dummy_adapter_generate():
    adapter = DummyAdapter()
    result = adapter.generate(GenerationRequest(prompt="hi"))
    assert result.text == "ok"
    assert result.completion_tokens == 1


def test_health_check_default():
    adapter = DummyAdapter()
    assert adapter.health_check() is True
