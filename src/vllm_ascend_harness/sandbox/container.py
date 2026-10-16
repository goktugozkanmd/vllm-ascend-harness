"""Container-based sandbox implementation.

TODO: implement Docker / podman-based isolation for Ascend NPU tasks.
"""

from __future__ import annotations

from vllm_ascend_harness.sandbox.base import BaseSandbox, SandboxResult
from vllm_ascend_harness.sandbox.whitelist import CommandWhitelist


class ContainerSandbox(BaseSandbox):
    """Sandbox backed by a container runtime.

    TODO: integrate with Docker / podman, mount Ascend device nodes,
    enforce resource cgroups and network isolation.
    """

    def __init__(self, image: str = "vllm-ascend/harness:latest") -> None:
        self.image = image
        self.whitelist = CommandWhitelist()
        self._container_id: str | None = None

    def setup(self) -> None:
        """Start the sandbox container.

        TODO: docker run --device /dev/davinci* ...
        """
        raise NotImplementedError

    def run(self, command: str, timeout: int = 60) -> SandboxResult:
        """Execute *command* inside the container.

        TODO: docker exec with whitelist enforcement.
        """
        if not self.whitelist.is_allowed(command):
            return SandboxResult(exit_code=126, stderr="Command blocked by allowlist")
        raise NotImplementedError

    def teardown(self) -> None:
        """Stop and remove the sandbox container.

        TODO: docker rm -f ...
        """
        raise NotImplementedError
