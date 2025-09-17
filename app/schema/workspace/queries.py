import asyncio
from typing import List, Optional
import strawberry
from strawberry.types import Info
from app.context import Context
from app.helpers.mapper import map_to_graphql_type
from app.helpers.sdk.call import safe_sdk_call
from app.schema.workspace.types import Workspace


@strawberry.type
class WorkspaceQueries:

    @strawberry.field
    async def workspace(
        self, id: strawberry.ID, info: Info[Context]
    ) -> Optional[Workspace]:
        workspace_data = await safe_sdk_call(
            info.context.workspace_api.get_workspace, int(id)
        )
        return (
            map_to_graphql_type(workspace_data, Workspace) if workspace_data else None
        )

    @strawberry.field
    async def workspaces(self, info: Info[Context]) -> List[Workspace]:
        response = await safe_sdk_call(info.context.workspace_api.list_workspaces)
        items = getattr(response, "items", []) or []
        return [map_to_graphql_type(item, Workspace) for item in items]
