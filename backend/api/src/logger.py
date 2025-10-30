import sys
import logging

from src.config import config


def get_logger(name: str) -> logging.Logger:
    level = config.LOG_LEVEL
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


__all__ = [
    'get_logger'
]
