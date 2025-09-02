import strawberry

from app.context import Context


@strawberry.type
class FetchWorkspacesQueries:
    @strawberry.field
    def workspaces(self, info: strawberry.Info[Context]) -> str:
        return "workspaces"
