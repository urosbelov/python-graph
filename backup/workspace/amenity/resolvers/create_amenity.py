from app.core.logger import logger
from app.schema.workspace.amenity.inputs import CreateWorkspaceAmenityInput
from app.schema.workspace.amenity.types import WorkspaceAmenity


def create_workspace_amenity(input: CreateWorkspaceAmenityInput) -> WorkspaceAmenity:
    logger.info("Creating amenity")
    return WorkspaceAmenity()
