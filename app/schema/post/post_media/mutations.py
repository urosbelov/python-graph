import strawberry

from app.schema.post.post_media.inputs import CreatePostMediaInput, UpdatePostMediaInput


@strawberry.type
class PostMediaMutations:

    @strawberry.mutation
    def create_post_media(self, input: CreatePostMediaInput) -> str:
        return "CreatePostMedia"

    @strawberry.mutation
    def update_post_media(self, id: strawberry.ID, input: UpdatePostMediaInput) -> str:
        return "UpdatePostMedia"

    @strawberry.mutation
    def delete_post_media(self, id: strawberry.ID) -> str:
        return "DeletePostMedia"
