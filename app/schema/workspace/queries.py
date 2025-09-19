from typing import List, Optional
import strawberry
from strawberry.types import Info
from app.context import Context
from app.helpers.mapper import map_to_graphql_type
from app.helpers.sdk.call import safe_sdk_call
from app.helpers.sdk.extract import extract_items
from app.schema.workspace.types import Workspace
from app.schema.workspace.category.queries import WorkspaceCategoryQueries

# Nested
from app.schema.workspace.category.queries import WorkspaceCategoryQueries
from app.schema.workspace.amenity.queries import WorkspaceAmenityQueries
from app.schema.workspace.feature.queries import WorkspaceFeatureQueries


@strawberry.type
class WorkspaceQueries(
    WorkspaceCategoryQueries, WorkspaceAmenityQueries, WorkspaceFeatureQueries
):

    @strawberry.field
    async def workspace(
        self, id: strawberry.ID, info: Info[Context]
    ) -> Optional[Workspace]:
        workspace_data = await safe_sdk_call(
            info.context.workspace_api.get_workspace_by_id,
            int(id),
            context=info.context,
        )
        return (
            map_to_graphql_type(workspace_data, Workspace) if workspace_data else None
        )

    @strawberry.field
    async def workspaces(self, info: Info[Context]) -> List[Workspace]:
        # Call SDK list method safely
        response = await safe_sdk_call(
            info.context.workspace_api.list_workspaces, context=info.context
        )
        # Safely extract items from response
        items = extract_items(response)
        # Map each SDK item to GraphQL type
        return [map_to_graphql_type(item, Workspace) for item in items]
