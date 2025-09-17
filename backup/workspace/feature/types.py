from datetime import datetime
import enum
from typing import Optional
import strawberry
from app.schema.workspace.amenity.types import WorkspaceAmenity
from app.schema.workspace.feature import resolvers


@strawberry.enum
class WorkspaceFeatureStatus(enum.Enum):
    PENDING = "PENDING"
    INACTIVE = "INACTIVE"
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"


@strawberry.type
class WorkspaceFeature:
    id: strawberry.ID
    status: WorkspaceFeatureStatus
    workspace_id: strawberry.ID
    amenity_id: strawberry.ID
    amenity: WorkspaceAmenity = strawberry.field(resolver=resolvers.get_field)
    created_by: Optional[str]
    created_at: datetime
    updated_at: datetime
