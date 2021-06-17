import logging
from typing import Union


def configure_logging(level: Union[str, int] = 'DEBUG'):
    """
    Configures the logger.

    @param level: logging level, DEBUG by default
    """
    logging.basicConfig(level=level)
