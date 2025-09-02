import sys
import uvicorn
from fastapi import FastAPI, Request
from strawberry.fastapi import GraphQLRouter
from app.schema.schema import schema
from app.core.config import load_settings
from app.core.logger import logger
from typing import Dict, Optional
from strawberry.dataloader import DataLoader
from app.schema.types.workspace import load_places


settings = load_settings()


# Context getter for GraphQLRouter
async def get_context(request: Request) -> Dict[str, Optional[str]]:
    """
    Extract x-user-id and x-workspace-id headers from the request
    and return them in the GraphQL context.
    """
    user_id = request.headers.get("x-user-id")
    workspace_id = request.headers.get("x-workspace-id")

    # Optionally log missing headers
    if not user_id:
        import logging

        logging.getLogger("graphql").warning("x-user-id header missing")

    if not workspace_id:
        import logging

        logging.getLogger("graphql").warning("x-workspace-id header missing")

    return {
        "user_id": user_id,
        "workspace_id": workspace_id,
        "places_loader": DataLoader(load_fn=load_places),
    }


# Create GraphQL router
graphql_app = GraphQLRouter(
    schema=schema,
    context_getter=get_context,
    graphql_ide=True if settings.ENVIRONMENT == "development" else False,
)

# Prepare server
app = FastAPI()
# app.add_middleware(UserIDMiddleware)
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
