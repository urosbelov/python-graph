import strawberry
from app.schema.types.post import Post


@strawberry.type
class PostMutation:
    @strawberry.field
    def create_post(self, title: str, content: str) -> Post:
        pass
