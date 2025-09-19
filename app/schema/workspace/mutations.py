import strawberry
from app.context import Context
from app.helpers.mapper import map_to_graphql_type
from app.schema.workspace.inputs import CreateWorkspaceInput, UpdateWorkspaceInput
from app.schema.workspace.types import Workspace
from app.helpers.sdk.call import safe_sdk_call

# Nested
from app.schema.workspace.category.mutations import WorkspaceCategoryMutations
from app.schema.workspace.amenity.mutations import WorkspaceAmenityMutations
from app.schema.workspace.feature.mutations import WorkspaceFeatureMutations


@strawberry.type
class WorkspaceMutations(
    WorkspaceCategoryMutations, WorkspaceAmenityMutations, WorkspaceFeatureMutations
):

    @strawberry.mutation
    async def create_workspace(
        self, input: CreateWorkspaceInput, info: strawberry.Info[Context]
    ) -> Workspace:
        input_data = input.__dict__
        workspace = await safe_sdk_call(
            info.context.workspace_api.create_workspace,
            input_data,
            context=info.context,
        )
        return map_to_graphql_type(workspace, Workspace)

    @strawberry.mutation
    async def update_workspace(
        self,
        workspace_id: strawberry.ID,
        input: UpdateWorkspaceInput,
        info: strawberry.Info[Context],
    ) -> Workspace:
        input_data = {k: v for k, v in input.__dict__.items() if v is not None}
        workspace = await safe_sdk_call(
            info.context.workspace_api.update_workspace,
            workspace_id,
            input_data,
            context=info.context,
        )
        return map_to_graphql_type(workspace, Workspace)

    @strawberry.mutation
    async def delete_workspace(
        self,
        workspace_id: strawberry.ID,
        info: strawberry.Info[Context],
    ) -> None:
        await safe_sdk_call(
            info.context.workspace_api.delete_workspace,
            workspace_id,
            context=info.context,
        )
