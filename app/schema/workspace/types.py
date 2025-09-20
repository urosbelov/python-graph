from datetime import datetime
from enum import Enum
from typing import Optional
import strawberry

from app.core.logger import logger

from app.context import Context
from app.helpers.converter.core import StrawberryConverter
from app.schema.scalars import Base62ID
from app.schema.shared.geospatial import Location
from app.schema.user.types import User
from app.schema.workspace.category.types import WorkspaceCategory


@strawberry.enum
class WorkspaceType(Enum):
    UNSPECIFIED = "unspecified"
    PERSONAL = "personal"
    ORGANIZATION = "organization"


@strawberry.enum
class WorkspaceStatus(Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"
    DELETED = "deleted"


@strawberry.type
class Workspace:
    id: Base62ID  # type: ignore
    type: WorkspaceType
    status: WorkspaceStatus
    name: str
    handle: str
    description: Optional[str] = None
    category_id: int
    updated_at: datetime
    created_at: datetime
    deleted_at: Optional[datetime] = None
    avatar_id: Optional[str] = None
    cover_id: Optional[str] = None
    formatted_address: Optional[str] = None
    created_by: Optional[strawberry.ID]
    location: Optional[Location] = None

    # ----------
    # Field resolvers
    # ----------
    @strawberry.field
    async def created_by_user(self, info: strawberry.Info[Context]) -> Optional[User]:
        user_obj = await info.context.users_loader.load(self.created_by)
        converter = StrawberryConverter()
        return converter.from_sdk(user_obj, User)

    @strawberry.field
    async def category(
        self, info: strawberry.Info[Context]
    ) -> Optional[WorkspaceCategory]:
        logger.info(f"Loading category for workspace: {self.id}")
        converter = StrawberryConverter()
        category_obj = await info.context.category_loader.load(int(self.category_id))
        return converter.from_sdk(category_obj, WorkspaceCategory)
