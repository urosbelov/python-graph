from libraries.logger.logger import init_logger
from app.core.config import load_settings

settings = load_settings()

logger = init_logger(
    name="graphql",
    mode=settings.ENVIRONMENT,
    environment=settings.ENVIRONMENT,
    sentry_dsn=None,
    sentry_release=None,
)
