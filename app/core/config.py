import os
import yaml
from dotenv import load_dotenv
from typing import Any

# Load environment variables from .env
load_dotenv()


def get_environment() -> str:
    """Return the current environment (default: production)."""
    return os.getenv("ENVIRONMENT", "production").lower()


def load_yaml_config(environment: str = "production") -> dict:
    """
    Load YAML configuration based on the environment.
    Falls back to config.yml if environment-specific file does not exist.
    """
    config_file = f"config.{environment}.yml"
    if not os.path.exists(config_file):
        config_file = "config.yml"
    with open(config_file, "r") as f:
        return yaml.safe_load(f) or {}


def get_config_value(env_var: str, config_value: Any, cast_type=str) -> Any:
    """
    Return the value from environment variable if set, otherwise return from config.
    Supports optional type casting.
    """
    raw = os.getenv(env_var)
    if raw is not None and raw.strip() != "":
        try:
            return cast_type(raw)
        except ValueError:
            pass
    return config_value


# Load environment and configuration
ENVIRONMENT = get_environment()
CONFIG = load_yaml_config(ENVIRONMENT)


class Settings:
    """Application settings loaded from YAML and environment variables."""

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
            "HTTP_PORT", CONFIG.get("http", {}).get("port", 8000), int
        )

        # LOGGING
        self.LOG_LEVEL = "debug" if self.ENVIRONMENT == "development" else "info"

        # CLIENTS
        self.CLIENTS = CONFIG.get("clients", {})

    def get_client(self, client_key: str) -> str | None:
        """
        Return the client URL by key.
        Supports environment variable override:
        Example: CLIENT_IDENTITY=http://override-url.com
        """
        env_var = f"CLIENT_{client_key.upper()}"
        return os.getenv(env_var) or self.CLIENTS.get(client_key)

    def __repr__(self):
        return (
            f"Settings(HTTP_HOST={self.HTTP_HOST}, HTTP_PORT={self.HTTP_PORT}, "
            f"LOG_LEVEL={self.LOG_LEVEL}, CLIENTS={self.CLIENTS})"
        )


def load_settings() -> Settings:
    """Factory function to load Settings instance."""
    return Settings()

