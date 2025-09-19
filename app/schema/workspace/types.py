from datetime import datetime
from enum import Enum
from typing import Optional
import strawberry


from app.context import Context
from app.helpers.mapper import map_to_graphql_type
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
    id: strawberry.ID
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

    # ----------
    # Field resolvers
    # ----------
    @strawberry.field
    async def created_by_user(self, info: strawberry.Info[Context]) -> Optional[User]:
        user_obj = await info.context.users_loader.load(self.created_by)
        if user_obj is None:
            return None
        return map_to_graphql_type(user_obj, User)

    @strawberry.field
    async def category(
        self, info: strawberry.Info[Context]
    ) -> Optional[WorkspaceCategory]:
        category_obj = await info.context.category_loader.load(int(self.category_id))
        if category_obj is None:
            return None
        return map_to_graphql_type(category_obj, WorkspaceCategory)
