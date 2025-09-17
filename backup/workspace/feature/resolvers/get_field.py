from typing import TYPE_CHECKING
from app.core.logger import logger

if TYPE_CHECKING:
    from app.schema.workspace.feature.types import WorkspaceFeature


def get_field(self: "WorkspaceFeature"):
    logger.info("Getting a workspace feature amenity")
    pass
