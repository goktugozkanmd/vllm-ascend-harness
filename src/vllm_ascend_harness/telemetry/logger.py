"""Logging utilities.

Provides a project-wide logger factory with consistent formatting.
"""

from __future__ import annotations

import logging
import sys

_LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_logger(name: str = "vllm_ascend_harness", level: int = logging.INFO) -> logging.Logger:
    """Return a configured logger.

    TODO: add structured JSON logging and file rotation options.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(logging.Formatter(_LOG_FORMAT, _DATE_FORMAT))
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger
