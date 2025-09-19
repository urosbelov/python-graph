from typing import Optional
import strawberry

from app.schema.workspace.feature.types import WorkspaceFeatureStatus


@strawberry.input
class CreateWorkspaceFeatureInput:
    amenity_id: int


@strawberry.input
class UpdateWorkspaceFeatureInput:
    status: Optional[WorkspaceFeatureStatus] = None
