from typing import List
import strawberry
from app.schema.post.types import Post
from app.schema.post.resolvers import get_post, list_posts


@strawberry.type
class PostQueries:
    post: Post = strawberry.field(resolver=get_post)
    posts: List[Post] = strawberry.field(resolver=list_posts)
