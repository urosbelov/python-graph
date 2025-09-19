import strawberry


@strawberry.input
class CreatePostInput:
    description: str


@strawberry.input
class UpdatePostInput:
    description: str
