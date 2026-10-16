"""Plugin manager with extensible registration interface.

Inspired by OpenHarness's plugin architecture.  Provides a central
registry for skills, adapters, and scorers to be discovered and
invoked at runtime.
"""

from __future__ import annotations

from typing import Any, Callable, Protocol


class Plugin(Protocol):
    """Protocol that all plugins must satisfy."""

    name: str

    def initialize(self, **kwargs: Any) -> None: ...


class PluginManager:
    """Central plugin registry.

    Extension point: third-party modules register custom skills,
    model adapters, or scorers via :meth:`register`.  Registered
    plugins are discoverable by name through :meth:`get`.
    """

    def __init__(self) -> None:
        self._plugins: dict[str, Plugin] = {}

    def register(self, plugin: Plugin, **kwargs: Any) -> None:
        """Register *plugin* and call its ``initialize`` hook."""
        if plugin.name in self._plugins:
            raise ValueError(f"Plugin already registered: {plugin.name}")
        plugin.initialize(**kwargs)
        self._plugins[plugin.name] = plugin

    def unregister(self, name: str) -> None:
        """Remove a registered plugin by *name*."""
        self._plugins.pop(name, None)

    def get(self, name: str) -> Plugin | None:
        """Look up a plugin by *name*."""
        return self._plugins.get(name)

    def list_plugins(self) -> list[str]:
        """Return all registered plugin names."""
        return list(self._plugins.keys())

    def register_factory(self, name: str, factory: Callable[..., Plugin]) -> None:
        """Register a lazy factory for plugin *name*.

        TODO: implement lazy instantiation on first ``get``.
        """
        raise NotImplementedError
