import strawberry


@strawberry.input
class CreateWorkspaceRoleInput:
    name: str
    description: str


@strawberry.input
class UpdateWorkspaceRoleInput:
    name: strawberry.ID
    description: str
