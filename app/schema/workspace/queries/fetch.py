from typing import Iterable, Optional
import strawberry
from strawberry import relay

from app.schema.workspace.connection import (
    WorkspaceCustomPaginationConnection,
)
from app.schema.workspace.types import WorkspaceNode


@strawberry.input
class WorkspaceFilters:
    name: Optional[str] = None


@strawberry.type
class FetchWorkspaceQueries:
    node: relay.Node = relay.node()

    @relay.connection(WorkspaceCustomPaginationConnection)
    def workspaces(self) -> Iterable[WorkspaceNode]:
        # You can return an empty list because resolve_connection fetches from microservice
        return []
