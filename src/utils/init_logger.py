import logging
import logging.config
import os
import yaml


def init_logger():
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open("logging.yaml", "rt") as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
