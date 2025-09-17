from typing import List
import strawberry

from app.schema.workspace.category.types import WorkspaceCategory
from app.schema.workspace.category.resolvers import list_workspace_categories


@strawberry.type
class WorkspaceCategoryQueries:
    workspace_categories: List[WorkspaceCategory] = strawberry.field(
        resolver=list_workspace_categories
    )
