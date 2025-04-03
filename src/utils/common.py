import os
import pytz
from datetime import datetime
from google.cloud import secretmanager
from src.env_config import EnvConfig


def retrieve_secret(secret_id: str) -> str:
    # current_app.logger.info(f"Retrieving secret: {EnvConfig.PROJECT_ID}, {secret_id}")
    if EnvConfig.ENVIRONMENT == "development":
        return os.getenv(secret_id.upper(), "dev-key")

    client = secretmanager.SecretManagerServiceClient()
    secret_name = client.secret_version_path(
        project=EnvConfig.PROJECT_ID, secret=secret_id, secret_version="latest"
    )
    response = client.access_secret_version(name=secret_name)
    secret = response.payload.data.decode("UTF-8")
    return secret


def format_datetime(timestamp: datetime) -> str:
    timezone = pytz.timezone(EnvConfig.TIMEZONE)
    return timestamp.astimezone(timezone).isoformat()
