import strawberry
from typing import Optional
from app.schema.types.workspace import (
    WorkspaceFilters,
    WorkspaceConnection,
    WorkspaceEdge,
)

from app.schema.types.pagination import PageRequest
from app.helpers.relay import create_connection
from app.helpers.pagination import build_pagination
from internal_sdk.workspace.client import (
    WorkspaceClient,
    WorkspaceListRequest,
)


@strawberry.type
class WorkspaceQuery:

    @strawberry.field
    def workspaces(
        self,
        info: strawberry.Info,
        page: Optional[PageRequest] = None,
        filter: Optional[WorkspaceFilters] = None,
    ) -> WorkspaceConnection:

        client = WorkspaceClient("http://0.0.0.0:4001")

        pagination = build_pagination(page)
        list_request = WorkspaceListRequest(
            filter=filter,
            pagination=pagination,
        )

        # Fetch from workspace microservice
        response = client.list(request=list_request)

        # Wrap nodes in connection using SDK pagination directly
        connection = create_connection(
            nodes=response["workspaces"],
            pagination=response["pagination"],
            EdgeType=WorkspaceEdge,
            ConnectionType=WorkspaceConnection,
        )

        return connection
