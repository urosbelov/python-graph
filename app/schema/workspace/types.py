from datetime import datetime
import enum
from typing import Optional
import strawberry


from app.context import Context
from app.helpers.mapper import map_to_graphql_type
from app.schema.workspace.category.types import WorkspaceCategory


@strawberry.enum
class WorkspaceType(enum.Enum):
    UNSPECIFIED = "unspecified"
    PERSONAL = "personal"
    ORGANIZATION = "organization"


@strawberry.enum
class WorkspaceStatus(enum.Enum):
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
    category_id: Optional[int] = None
    updated_at: datetime
    created_at: datetime
    deleted_at: Optional[datetime] = None
    avatar_id: Optional[str] = None
    cover_id: Optional[str] = None
    formatted_address: Optional[str] = None

    # ----------
    # Field resolvers
    # ----------
    @strawberry.field
    async def category(
        self, info: strawberry.Info[Context]
    ) -> Optional[WorkspaceCategory]:
        """Fetch the category using DataLoader."""
        if not self.category_id or self.category_id <= 0:
            return None

        # Load category via DataLoader
        category_obj = await info.context.category_loader.load(int(self.category_id))
        if category_obj is None:
            return None

        # Map SDK object to GraphQL type
        return map_to_graphql_type(category_obj, WorkspaceCategory)
