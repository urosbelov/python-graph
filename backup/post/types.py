from datetime import datetime
from enum import IntEnum
from typing import Optional
import strawberry


@strawberry.input
class PostInput:
    description: Optional[str] = None


@strawberry.enum
class PostStatus(IntEnum):
    UNSPECIFIED = 0
    DRAFT = 1
    ACTIVE = 2
    INACTIVE = 3
    FLAGGED = 4
    DELETED = 5


@strawberry.type
class Post:
    id: strawberry.ID
    status: PostStatus
    description: Optional[str] = None
    workspace_id: Optional[int] = None
    view_count: int
    place_id: Optional[int] = None
    short_url: str
    deleted_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
