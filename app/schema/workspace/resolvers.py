import strawberry

from .queries.fetch import FetchWorkspaceQueries


from .mutations.create import CreateWorkspaceMutation
from .mutations.update import UpdateWorkspaceMutation


@strawberry.type
class WorkspaceQuery(FetchWorkspaceQueries):
    pass


@strawberry.type
class WorkspaceMutation(CreateWorkspaceMutation, UpdateWorkspaceMutation):
    pass
