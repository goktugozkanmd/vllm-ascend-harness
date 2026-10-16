"""Event bus for decoupled inter-module communication.

Provides a lightweight publish/subscribe mechanism so that the agent
loop, telemetry, and evaluator modules can communicate without hard
dependencies.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable


EventHandler = Callable[[Any], None]


class EventBus:
    """In-process publish/subscribe event bus.

    Modules subscribe to named event topics; the bus dispatches
    published events to all registered handlers synchronously.
    """

    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(self, topic: str, handler: EventHandler) -> None:
        """Register *handler* for *topic*."""
        self._handlers[topic].append(handler)

    def unsubscribe(self, topic: str, handler: EventHandler) -> None:
        """Remove *handler* from *topic*."""
        handlers = self._handlers.get(topic, [])
        if handler in handlers:
            handlers.remove(handler)

    def publish(self, topic: str, event: Any = None) -> None:
        """Publish *event* to all subscribers of *topic*.

        TODO: add async dispatch and error isolation options.
        """
        for handler in self._handlers.get(topic, []):
            handler(event)

    def clear(self) -> None:
        """Remove all subscriptions."""
        self._handlers.clear()
