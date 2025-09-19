import strawberry

from app.schema.workspace.membership.inputs import CreateWorkspaceMembershipInput


@strawberry.type
class WorkspaceMembershipMutations:

    @strawberry.mutation
    def add_workspace_member(self, input: CreateWorkspaceMembershipInput) -> str:
        return f"Member with user ID {input.user_id} added to role ID {input.role_id}"

    @strawberry.mutation
    def delete_workspace_member(self, id: strawberry.ID) -> str:
        return f"Member with ID {id} deleted"
