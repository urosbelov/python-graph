import enum
from typing import Optional
import strawberry


@strawberry.enum
class CategoryStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DEPRECATED = "deprecated"


@strawberry.type
class WorkspaceCategory:
    id: strawberry.ID
    status: CategoryStatus
    name: str
    description: Optional[str] = None
    created_at: str
    updated_at: str
