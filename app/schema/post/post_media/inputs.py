import strawberry


@strawberry.input
class CreatePostMediaInput:
    post_id: strawberry.ID
    alt_text: str
    media_id: strawberry.ID


@strawberry.input
class UpdatePostMediaInput:
    alt_text: str
