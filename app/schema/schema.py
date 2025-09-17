import strawberry

# ----------
# MAIN
# ----------
from app.schema.user import UserQueries, UserMutations
from app.schema.workspace import WorkspaceQueries, WorkspaceMutations

# ----------
# SOCIAL
# ----------
from app.schema.post import PostQueries, PostMutations

# ----------
# MEDIA
# ----------
from app.schema.media.queries import MediaQueries

# ----------
# GEOSPATIAL
# ----------
from app.schema.bbox.queries import BBoxQueries


@strawberry.type
class Query(
    UserQueries,
    WorkspaceQueries,
    PostQueries,
    MediaQueries,
    BBoxQueries,
):
    pass


@strawberry.type
class Mutation(UserMutations, WorkspaceMutations, PostMutations):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
