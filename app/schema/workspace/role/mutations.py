import strawberry

from app.schema.workspace.role.inputs import (
    CreateWorkspaceRoleInput,
    UpdateWorkspaceRoleInput,
)


@strawberry.type
class WorkspaceRoleMutations:

    @strawberry.mutation
    def create_role(self, input: CreateWorkspaceRoleInput) -> str:
        return f"Role {input.name} created"

    @strawberry.mutation
    def update_role(self, id: strawberry.ID, input: UpdateWorkspaceRoleInput) -> str:
        return f"Role with ID {id} updated"
