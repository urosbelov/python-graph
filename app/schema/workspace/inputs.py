from datetime import datetime
from typing import Optional
import strawberry


@strawberry.input
class CreateWorkspaceInput:
    name: str
    handle: str
    category_id: int


@strawberry.input
class WorkspaceFiltersInput:
    owner_id: Optional[strawberry.ID] = None
    name: Optional[str] = None
    created_by: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    google_place_id: Optional[str] = None
