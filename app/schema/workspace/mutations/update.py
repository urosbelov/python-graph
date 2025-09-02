import strawberry

from app.schema.workspace.types import Workspace


@strawberry.type
class UpdateWorkspaceMutation:

    @strawberry.mutation
    def update_workspace(self) -> str:
        return "update workspace"
