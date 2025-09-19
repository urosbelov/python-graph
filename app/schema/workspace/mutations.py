import strawberry
from app.context import Context
from app.helpers.mapper import map_to_graphql_type
from app.schema.workspace.inputs import CreateWorkspaceInput
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
        # Convert input to dict
        input_data = input.__dict__

        # Call SDK safely
        workspace = await safe_sdk_call(
            info.context.workspace_api.create_workspace,
            input_data,
            context=info.context,
        )

        return map_to_graphql_type(workspace, Workspace)
