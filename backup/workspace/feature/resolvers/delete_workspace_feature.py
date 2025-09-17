from app.core.logger import logger
from app.schema.workspace.feature.inputs import WorkspaceFeatureInput


def delete_workspace_feature(input: WorkspaceFeatureInput) -> bool:
    logger.info("Deleting a workspace feature")
    return True
