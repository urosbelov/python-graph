import strawberry


@strawberry.type
class PostMediaQueries:
    @strawberry.field
    def post_media(self, id: strawberry.ID) -> str:
        return "PostMedia"

    @strawberry.field
    def post_medias(self) -> str:
        return "PostMedias"
