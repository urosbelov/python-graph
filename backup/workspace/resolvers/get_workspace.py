import strawberry
from app.core.logger import logger
from app.schema.workspace.types import Workspace


def get_workspace(id: strawberry.ID) -> Workspace:
    logger.debug("get_workspace called")
    return Workspace()
