import strawberry

from .queries.fetch import FetchWorkspacesQueries

from .mutations.create import CreateWorkspaceMutation
from .mutations.update import UpdateWorkspaceMutation


@strawberry.type
class WorkspaceQuery(FetchWorkspacesQueries):
    pass


@strawberry.type
class WorkspaceMutation(CreateWorkspaceMutation, UpdateWorkspaceMutation):
    pass
