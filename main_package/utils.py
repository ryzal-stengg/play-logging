"""Utility functions applicable and made useable by the whole package."""

import logging
import yaml


logger = logging.getLogger(__name__)


class FilterNoQuotes(logging.Filter):

    def filter(self, record):
        if isinstance(record.msg, str):
            record.msg = record.msg.replace('"', "")
            return 1


def setup_logging(
    logging_config_path: str = "./conf/logging.yaml",
    default_level: int = logging.INFO,
    exclude_handlers: list = [],
):
    """Load a specified custom configuration for logging.

    Parameters
    ----------
    logging_config_path : str, optional
        Path to the logging YAML configuration file, by default "./conf/logging.yaml"
    default_level : int, optional
        Default logging level to use if the configuration file is not found,
        by default logging.INFO
    """
    try:
        with open(logging_config_path, "rt", encoding="utf-8") as file:
            log_config = yaml.safe_load(file.read())

        logging_handlers = log_config["root"]["handlers"]
        log_config["root"]["handlers"] = [
            handler for handler in logging_handlers if handler not in exclude_handlers
        ]

        logging.config.dictConfig(log_config)

        logger.info('Successfully "loaded" custom logging some configuration.')

    except FileNotFoundError as error:
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=default_level,
        )
        logger.info(error)
        logger.info("Logging config file is not found. Basic config is being used.")
