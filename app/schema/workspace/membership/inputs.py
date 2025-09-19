import strawberry


@strawberry.input
class CreateWorkspaceMembershipInput:
    user_id: strawberry.ID
    role_id: strawberry.ID


@strawberry.input
class UpdateWorkspaceMembershipInput:
    role_id: strawberry.ID
