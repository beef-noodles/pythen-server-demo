from os import getenv


def env_log_level():
    return getenv("LOG_LEVEL")
