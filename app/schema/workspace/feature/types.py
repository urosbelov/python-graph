from datetime import datetime
from enum import Enum
from typing import Optional
import strawberry

from app.context import Context
from app.helpers.converter.core import StrawberryConverter
from app.schema.workspace.amenity.types import WorkspaceAmenity


@strawberry.enum
class WorkspaceFeatureStatus(Enum):
    PENDING = "pending"
    INACTIVE = "inactive"
    ACTIVE = "active"
    DELETED = "deleted"


@strawberry.type
class WorkspaceFeature:

    # Core
    id: strawberry.ID
    status: WorkspaceFeatureStatus
    created_by: strawberry.ID

    # Timestamps
    created_at: datetime
    updated_at: Optional[datetime]

    # Deletion
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[strawberry.ID] = None

    # Base
    workspace_id: str
    amenity_id: int

    @strawberry.field
    async def amenity(
        self, info: strawberry.Info[Context]
    ) -> Optional[WorkspaceAmenity]:
        converter = StrawberryConverter()
        amenity = await info.context.amenity_loader.load(int(self.amenity_id))
        return converter.from_sdk(amenity, WorkspaceAmenity)
