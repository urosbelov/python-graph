from typing import List, Optional
import strawberry
from app.schema.workspace.types import Workspace


@strawberry.type
class WorkspaceQueries(WorkspaceAmenityQueries, WorkspaceCategoryQueries):
    workspace: Optional[Workspace] = strawberry.field(resolver=get_workspace)
    workspaces: Optional[List[Workspace]] = strawberry.field(resolver=list_workspaces)
