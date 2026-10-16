"""Unit tests for CommandWhitelist."""

from vllm_ascend_harness.sandbox.whitelist import CommandWhitelist


def test_allowed_command():
    wl = CommandWhitelist()
    assert wl.is_allowed("ls -la") is True


def test_blocked_command():
    wl = CommandWhitelist()
    assert wl.is_allowed("rm -rf /") is False


def test_unknown_command():
    wl = CommandWhitelist()
    assert wl.is_allowed("dd if=/dev/zero of=/tmp/x") is False
