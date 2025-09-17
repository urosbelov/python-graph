from datetime import datetime
import enum
from typing import List, Optional
import strawberry

from app.schema.workspace import resolvers
from app.schema.workspace.feature.types import WorkspaceFeature


@strawberry.enum
class WorkspaceType(enum.Enum):
    UNSPECIFIED = "UNSPECIFIED"
    PERSONAL = "PERSONAL"
    ORGANIZATION = "ORGANIZATION"


@strawberry.enum
class WorkspaceStatus(enum.Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    SUSPENDED = "SUSPENDED"


@strawberry.type
class Workspace:
    id: strawberry.ID
    type: WorkspaceType
    status: WorkspaceStatus
    name: str
    handle: str
    description: Optional[str]
    category_id: Optional[int]
    updated_at: datetime
    created_at: datetime
    deleted_at: Optional[datetime]
    avatar_id: Optional[str]
    cover_id: Optional[str]
    formatted_address: Optional[str]
    features: Optional[List[WorkspaceFeature]] = strawberry.field(
        resolver=resolvers.get_workspace_features
    )
