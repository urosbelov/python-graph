import strawberry

from app.schema.post.types import Post
from .resolvers import create_post


@strawberry.type
class PostMutations:
    create_post: Post = strawberry.field(resolver=create_post)
