from typing import List, Optional
import strawberry
from strawberry.types import Info
from app.context import Context
from app.helpers.sdk.call import safe_sdk_call
from app.helpers.sdk.extract import extract_items
from app.schema.scalars import Base62ID
from app.schema.workspace.types import Workspace
from app.schema.workspace.category.queries import WorkspaceCategoryQueries

# Nested
from app.schema.workspace.category.queries import WorkspaceCategoryQueries
from app.schema.workspace.amenity.queries import WorkspaceAmenityQueries
from app.schema.workspace.feature.queries import WorkspaceFeatureQueries
from app.helpers.converter import StrawberryConverter


@strawberry.type
class WorkspaceQueries(
    WorkspaceCategoryQueries, WorkspaceAmenityQueries, WorkspaceFeatureQueries
):

    @strawberry.field
    async def workspace(
        self, workspace_id: Base62ID, info: Info[Context]  # type: ignore
    ) -> Optional[Workspace]:
        converter = StrawberryConverter()
        workspace_data = await safe_sdk_call(
            info.context.workspace_api.get_workspace_by_id,
            workspace_id,
            context=info.context,
        )
        return converter.from_sdk(workspace_data, Workspace)

    @strawberry.field
    async def workspaces(self, info: Info[Context]) -> List[Workspace]:
        converter = StrawberryConverter()
        response = await safe_sdk_call(
            info.context.workspace_api.list_workspaces, context=info.context
        )
        items = extract_items(response)
        return converter.from_sdk(items, Workspace)
