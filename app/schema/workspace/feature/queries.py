from typing import List
import strawberry

from app.context import Context
from app.helpers.mapper import map_to_graphql_type
from app.helpers.sdk.call import safe_sdk_call
from app.helpers.sdk.extract import extract_items
from app.schema.workspace.feature.types import WorkspaceFeature


@strawberry.type
class WorkspaceFeatureQueries:
    @strawberry.field
    async def workspace_feature(self, id: strawberry.ID) -> str:
        return f"Workspace feature details for ID {id}"

    @strawberry.field
    async def workspace_features(
        self, workspace_id: strawberry.ID, info: strawberry.Info[Context]
    ) -> List[WorkspaceFeature]:
        response = await safe_sdk_call(
            info.context.feature_api.get_workspace_features, workspace_id
        )
        items = extract_items(response)
        return [map_to_graphql_type(item, WorkspaceFeature) for item in items]
