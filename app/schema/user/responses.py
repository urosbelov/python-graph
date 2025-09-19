import strawberry


@strawberry.type
class CreateUserResponse:
    password: strawberry.ID
