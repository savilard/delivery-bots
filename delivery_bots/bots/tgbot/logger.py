import logging
from typing import Union

from loguru import logger


class InterceptHandler(logging.Handler):
    """Forwards standard logger messages to Loguru."""

    def emit(self, record):  # noqa: D102
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = frame.f_back  # type: ignore
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def configure_logging(level: Union[str, int] = 'DEBUG'):
    """
    Configures the logger.

    @param level: logging level, DEBUG by default
    """
    logging.getLogger().handlers = [InterceptHandler()]
    logging.getLevelName(level)
