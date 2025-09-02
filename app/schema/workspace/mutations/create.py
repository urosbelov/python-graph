import strawberry
from app.schema.workspace.types import Workspace


@strawberry.type
class CreateWorkspaceMutation:

    @strawberry.mutation
    def create_workspace(self) -> str:
        return "create workspace"
