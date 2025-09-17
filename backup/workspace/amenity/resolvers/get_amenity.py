from datetime import datetime
import strawberry
from app.core.logger import logger
from app.schema.workspace.amenity.types import (
    WorkspaceAmenity,
    WorkspaceAmenityStatus,
    WorkspaceAmenityType,
)


def get_workspace_amenity(id: strawberry.ID) -> WorkspaceAmenity:
    mock_amenity = WorkspaceAmenity(
        id=id,
        type=WorkspaceAmenityType.BOOLEAN,
        status=WorkspaceAmenityStatus.ACTIVE,
        key="wifi",
        name="WiFi",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        created_by="42",
    )
    return mock_amenity
