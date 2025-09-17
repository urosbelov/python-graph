from typing import List
import strawberry
from app.context import Context
from app.core.logger import logger
from app.schema.workspace.feature.types import WorkspaceFeature


def get_workspace_features(
    self, info: strawberry.Info[Context]
) -> List[WorkspaceFeature]:
    logger.info(f"Fetching workspace features {self.id}")
    return []
