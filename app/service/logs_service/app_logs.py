import logging

import config


def init_logging() -> None:
    """
    Configure the logger.

    Returns:
        None
    """
    logging.basicConfig(
        level=getattr(logging, config.LOGGING_MODE),
        format=config.LOGGER_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    logging.info("SET UP FINISHED\n")


def config_logs() -> None:
    """
    Logs appearing when the microservice is started.

    Returns:
        None
    """
    logging.info(f"{config.SERVICE_NAME=}")
    logging.info(f"{config.MS_VERSION=}")
    logging.info(f"{config.SERVICE_PORT=}")
    logging.info(f"{config.LOGGING_MODE=}")
    logging.info("\n")
