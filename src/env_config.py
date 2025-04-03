import os
from dotenv import load_dotenv

load_dotenv()


class EnvConfig:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    PROJECT_ID = os.getenv("PROJECT_ID", "project_id")
    TIMEZONE = os.getenv("TIMEZONE", "Asia/Shanghai")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
