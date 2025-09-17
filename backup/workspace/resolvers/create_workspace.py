from app.core.logger import logger
from app.schema.workspace.inputs import CreateWorkspaceInput
from app.schema.workspace.types import Workspace


def create_workspace(input: CreateWorkspaceInput) -> Workspace:
    logger.info("Creating workspace...")
    return Workspace()
