import strawberry


@strawberry.type
class CreateWorkspaceMutation:

    @strawberry.mutation
    def create_workspace(self) -> str:
        return "create workspace"
