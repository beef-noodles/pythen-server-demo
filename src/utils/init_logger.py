import logging
import logging.config
import os
import yaml

from src.configs.env_config import env_log_level


def init_logger():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open("logging.yaml", "rt") as f:
        config = yaml.safe_load(f.read())
        config["root"]["level"] = (
            env_log_level() if env_log_level() else config["root"]["level"]
        )
        logging.config.dictConfig(config)
