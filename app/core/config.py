import os
import yaml
from dotenv import load_dotenv
from typing import Any

load_dotenv()  # Load environment variables from .env


def get_environment() -> str:
    return os.getenv("ENVIRONMENT", "production").lower()


def load_yaml_config(environment: str = "production") -> dict:
    config_file = f"config.{environment}.yml"
    if not os.path.exists(config_file):
        config_file = "config.yml"  # Fallback
    with open(config_file, "r") as f:
        return yaml.safe_load(f)


ENVIRONMENT = get_environment()
CONFIG = load_yaml_config(ENVIRONMENT)


def get_config_value(env_var: str, config_value: Any, cast_type=str) -> Any:
    raw = os.getenv(env_var)
    if raw is not None and raw.strip() != "":
        try:
            return cast_type(raw)
        except ValueError:
            pass
    return config_value


class Settings:
    def __init__(self):
        # ENVIRONMENT
        self.ENVIRONMENT = get_config_value(
            "ENVIRONMENT", CONFIG.get("environment", "production")
        )

        # HTTP
        self.HTTP_HOST = get_config_value(
            "HTTP_HOST", CONFIG.get("http", {}).get("host", "0.0.0.0")
        )
        self.HTTP_PORT = get_config_value(
            "HTTP_PORT", CONFIG.get("http", {}).get("port", 4000), int
        )

        # LOGGING
        self.LOG_LEVEL = "debug" if self.ENVIRONMENT == "development" else "info"

    def __repr__(self):
        return (
            f"Settings(HTTP_HOST={self.HTTP_HOST}, HTTP_PORT={self.HTTP_PORT}, "
            f"LOG_LEVEL={self.LOG_LEVEL})"
        )


def load_settings() -> Settings:
    return Settings()
