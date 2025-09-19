from typing import Optional
import strawberry
from app.schema.workspace.amenity.types import (
    WorkspaceAmenityStatus,
    WorkspaceAmenityType,
)


@strawberry.input
class CreateWorkspaceAmenityInput:
    name: str
    description: Optional[str] = None
    icon: Optional[str] = None
    type: Optional[WorkspaceAmenityType] = None


@strawberry.input
class UpdateWorkspaceAmenityInput:
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    status: Optional[WorkspaceAmenityStatus] = None
