import strawberry


@strawberry.type
class UpdateWorkspaceMutation:

    @strawberry.mutation
    def update_workspace(self) -> str:
        return "update workspace"
