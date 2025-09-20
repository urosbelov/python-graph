from datetime import datetime
from typing import Optional
import strawberry

from app.schema.shared.geospatial import LocationInput


@strawberry.input
class CreateWorkspaceInput:
    name: str
    handle: str
    category_id: int


@strawberry.input
class UpdateWorkspaceInput:
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[LocationInput] = None


@strawberry.input
class WorkspaceFiltersInput:
    owner_id: Optional[strawberry.ID] = None
    name: Optional[str] = None
    created_by: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    google_place_id: Optional[str] = None
