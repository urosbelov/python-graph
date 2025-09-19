import strawberry
from strawberry.extensions import ValidationCache

# ----------
# MAIN
# ----------
from app.core.middleware import GraphqlErrorMiddleware
from app.schema.user import UserQueries, UserMutations
from app.schema.workspace import WorkspaceQueries, WorkspaceMutations


@strawberry.type
class Query(UserQueries, WorkspaceQueries):
    pass


@strawberry.type
class Mutation(UserMutations, WorkspaceMutations):
    pass


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        ValidationCache(),  # caches GraphQL document validation
    ],
)
