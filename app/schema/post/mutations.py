import strawberry

from app.schema.post.inputs import CreatePostInput, UpdatePostInput
from app.schema.post.post_media.mutations import PostMediaMutations


@strawberry.type
class PostMutations(PostMediaMutations):
    @strawberry.mutation
    def create_post(self, input: CreatePostInput) -> str:
        return "Create Post"

    @strawberry.mutation
    def update_post(self, id: strawberry.ID, input: UpdatePostInput) -> str:
        return "Update Post"

    @strawberry.mutation
    def delete_post(self, id: strawberry.ID) -> str:
        return "Delete Post"
