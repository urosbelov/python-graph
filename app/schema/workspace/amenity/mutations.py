import strawberry
from app.context import Context
from app.schema.workspace.amenity.inputs import (
    CreateWorkspaceAmenityInput,
    UpdateWorkspaceAmenityInput,
)


@strawberry.type
class WorkspaceAmenityMutations:

    @strawberry.mutation
    async def create_workspace_amenity(
        self, input: CreateWorkspaceAmenityInput, info: strawberry.Info[Context]
    ) -> str:
        return "Workspace amenity created"

    @strawberry.mutation
    async def update_workspace_amenity(
        self,
        id: strawberry.ID,
        input: UpdateWorkspaceAmenityInput,
        info: strawberry.Info[Context],
    ) -> str:
        return "Workspace amenity updated"
