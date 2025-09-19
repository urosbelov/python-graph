from datetime import datetime
import enum
from typing import Optional
import strawberry


@strawberry.enum
class WorkspaceCategoryStatus(enum.Enum):
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"
    DEPRECATED = "deprecated"


@strawberry.type
class WorkspaceCategory:
    # Core
    id: Optional[int] = None
    status: WorkspaceCategoryStatus
    created_by: strawberry.ID

    # Timestamps
    created_at: datetime
    updated_at: Optional[datetime] = None

    # Deprecation
    deprecated_at: Optional[datetime] = None
    deprecated_by: Optional[strawberry.ID] = None

    # Base
    name: str
    key: str
    description: Optional[str] = None
    icon: Optional[str] = None
