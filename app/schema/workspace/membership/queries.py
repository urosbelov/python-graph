import strawberry


@strawberry.type
class WorkspaceMembershipQueries:
    @strawberry.field
    def workspace_membership(self, id: strawberry.ID) -> str:
        return f"Workspace membership details for ID {id}"

    @strawberry.field
    def workspace_memberships(self) -> str:
        return "List of workspace memberships"
