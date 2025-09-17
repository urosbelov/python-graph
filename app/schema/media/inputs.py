import strawberry


@strawberry.input
class GetSignedUrlInput:
    media_type: str
