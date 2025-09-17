import strawberry
from app.schema.workspace.category.resolvers import create_workspace_category
from app.schema.workspace.category.types import WorkspaceCategory


@strawberry.type
class WorkspaceCategoryMutations:
    create_workspace_category: WorkspaceCategory = strawberry.field(
        resolver=create_workspace_category
    )
