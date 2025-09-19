import strawberry


@strawberry.type
class WorkspaceRoleQueries:

    @strawberry.field
    def role(self, id: strawberry.ID) -> str:
        return f"Role with ID {id}"

    @strawberry.field
    def roles(self) -> str:
        return "List of roles"
