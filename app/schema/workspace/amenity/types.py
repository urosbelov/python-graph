from datetime import datetime
from enum import Enum
from typing import Optional
import strawberry


@strawberry.enum
class WorkspaceAmenityType(Enum):
    BOOLEAN = "boolean"
    JSON = "json"
    STANDALONE = "standalone"


@strawberry.enum
class WorkspaceAmenityStatus(Enum):
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"
    DEPRECATED = "deprecated"


@strawberry.type
class WorkspaceAmenity:
    # Core
    id: strawberry.ID
    status: WorkspaceAmenityStatus
    created_by: strawberry.ID

    # Timestamps
    created_at: datetime
    updated_at: datetime

    # Deprecation
    deprecated_at: Optional[datetime]
    deprecated_by: Optional[strawberry.ID]

    # Base
    type: WorkspaceAmenityType
    name: str
    key: str
    icon: Optional[str]
