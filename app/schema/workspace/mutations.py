import strawberry
from app.context import Context
from app.schema.shared.scalars import Base62ID
from app.schema.workspace.inputs import CreateWorkspaceInput, UpdateWorkspaceInput
from app.schema.workspace.types import Workspace
from app.helpers.sdk.call import safe_sdk_call

# Nested
from app.schema.workspace.category.mutations import WorkspaceCategoryMutations
from app.schema.workspace.amenity.mutations import WorkspaceAmenityMutations
from app.schema.workspace.feature.mutations import WorkspaceFeatureMutations
from app.helpers.converter import StrawberryConverter


@strawberry.type
class WorkspaceMutations(
    WorkspaceCategoryMutations, WorkspaceAmenityMutations, WorkspaceFeatureMutations
):

    @strawberry.mutation
    async def create_workspace(
        self, input: CreateWorkspaceInput, info: strawberry.Info[Context]
    ) -> Workspace:
        converter = StrawberryConverter()
        workspace = await safe_sdk_call(
            info.context.workspace_api.create_workspace,
            converter.to_dict(input),
            context=info.context,
        )
        return converter.from_sdk(workspace, Workspace)

    @strawberry.mutation
    async def update_workspace(
        self,
        workspace_id: Base62ID,  # type: ignore
        input: UpdateWorkspaceInput,
        info: strawberry.Info[Context],
    ) -> Workspace:
        converter = StrawberryConverter()
        workspace = await safe_sdk_call(
            info.context.workspace_api.update_workspace,
            workspace_id,
            converter.to_dict(input),
            context=info.context,
        )
        return converter.from_sdk(workspace, Workspace)

    @strawberry.mutation
    async def delete_workspace(
        self,
        workspace_id: Base62ID,  # type: ignore
        info: strawberry.Info[Context],
    ) -> None:
        await safe_sdk_call(
            info.context.workspace_api.delete_workspace,
            workspace_id,
            context=info.context,
        )
