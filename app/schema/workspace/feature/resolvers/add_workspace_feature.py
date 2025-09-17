from app.core.logger import logger
from app.schema.workspace.feature.inputs import WorkspaceFeatureInput


def add_workspace_feature(input: WorkspaceFeatureInput) -> bool:
    logger.info("Adding a workspace feature")
    return True
