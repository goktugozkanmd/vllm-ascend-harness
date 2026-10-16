"""Unit tests for EventBus."""

from vllm_ascend_harness.core.event_bus import EventBus


def test_subscribe_and_publish():
    received: list = []
    bus = EventBus()
    bus.subscribe("test", received.append)
    bus.publish("test", "hello")
    assert received == ["hello"]


def test_unsubscribe():
    received: list = []
    bus = EventBus()
    handler = received.append
    bus.subscribe("test", handler)
    bus.unsubscribe("test", handler)
    bus.publish("test", "hello")
    assert received == []


def test_clear():
    received: list = []
    bus = EventBus()
    bus.subscribe("test", received.append)
    bus.clear()
    bus.publish("test", "hello")
    assert received == []
