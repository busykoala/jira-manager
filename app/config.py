import os
from pathlib import Path

from dotenv import load_dotenv


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    JIRA_URL = os.getenv("JIRA_URL")
    USERNAME = os.getenv("USERNAME")
    CHROME_BINARY = os.getenv("CHROME_BINARY")


def get_config():
    return Config()
