import sys
import uvicorn
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema.schema import schema
from app.core.config import load_settings
from app.core.logger import logger
from app.context import get_context


settings = load_settings()


# Create GraphQL router
graphql_app = GraphQLRouter(
    schema=schema,
    context_getter=get_context,  # Inject context!
    graphql_ide=True if settings.ENVIRONMENT == "development" else False,
)

# Prepare server
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


def main() -> None:
    try:
        logger.info(f"Starting GraphQL service with settings: {settings}")

        uvicorn.run(
            "app.main:app",
            host=settings.HTTP_HOST,
            port=settings.HTTP_PORT,
            log_config=None,  # disable uvicorn’s default loggers
            log_level=settings.LOG_LEVEL,
            reload=settings.ENVIRONMENT == "development",
        )
    except Exception as e:
        logger.error(f"Application failed to start: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
