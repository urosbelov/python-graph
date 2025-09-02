import strawberry
from .pagination import PageInfo


# ----------------------
# Node type
@strawberry.type
class Post:
    id: strawberry.ID
    name: str

    @strawberry.field
    def full_name(self) -> str:
        return f"Post: {self.id} + {self.name}"


# ----------------------


# ----------------------
# Edge & Connection
@strawberry.type
class PostEdge:
    node: Post
    cursor: str


@strawberry.type
class PostConnection:
    edges: list[PostEdge]
    page_info: PageInfo


# ----------------------


# ----------------------
# Input filter
@strawberry.input
class PostFilter:
    id: strawberry.ID
    name: str


# ----------------------
