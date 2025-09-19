import strawberry
from strawberry.extensions import ValidationCache

from app.schema.post.types import BigInt
from app.schema.user import UserQueries, UserMutations
from app.schema.workspace import WorkspaceQueries, WorkspaceMutations
from app.schema.post import PostQueries, PostMutations


@strawberry.type
class Query(UserQueries, WorkspaceQueries, PostQueries):
    pass


@strawberry.type
class Mutation(UserMutations, WorkspaceMutations, PostMutations):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        ValidationCache(),  # caches GraphQL document validation
    ],
)
