from app.core.logger import logger
from datetime import datetime
import enum
import strawberry
from app.schema.user.types import User
from app.schema.workspace.amenity.resolvers.populate_created_by import (
    populate_workspace_created_by,
)


@strawberry.enum
class WorkspaceAmenityType(enum.Enum):
    BOOLEAN = "BOOLEAN"
    JSON = "JSON"
    STANDALONE = "STANDALONE"


@strawberry.enum
class WorkspaceAmenityStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DEPRECATED = "DEPRECATED"


@strawberry.type
class WorkspaceAmenity:
    id: strawberry.ID
    type: WorkspaceAmenityType
    status: WorkspaceAmenityStatus
    key: str
    name: str
    created_at: datetime
    updated_at: datetime
    created_by: strawberry.ID
    created_by_user: User = strawberry.field(resolver=populate_workspace_created_by)
