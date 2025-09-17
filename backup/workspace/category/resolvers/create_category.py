from app.core.logger import logger
from app.schema.workspace.category.inputs import CreateWorkspaceCategoryInput
from app.schema.workspace.category.types import WorkspaceCategory


def create_workspace_category(input: CreateWorkspaceCategoryInput) -> WorkspaceCategory:
    logger.info("Creating a new workspace category")
    return WorkspaceCategory()
