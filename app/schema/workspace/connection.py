import strawberry
from strawberry import relay
from typing import Iterable, Optional
from app.schema.workspace.types import WorkspaceFiltersInput, WorkspaceNode
from internal_sdk.workspace.client import (
    WorkspaceClient,
    WorkspaceListRequest,
)
from app.helpers.relay.pagination import compose_pagination_request
from app.helpers.relay.page import compose_page_info
from app.helpers.relay.edge import compose_edges


@strawberry.type
class WorkspaceCustomPaginationConnection(relay.Connection[WorkspaceNode]):
    @classmethod
    def resolve_connection(
        cls,
        nodes: Iterable[WorkspaceNode] = None,  # Ignored
        *,
        info=None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        filters: Optional[WorkspaceFiltersInput] = None,
        **kwargs,
    ):
        # Compose microservice pagination request
        pagination_request = compose_pagination_request(
            first=first, last=last, before=before, after=after
        )

        # Fetch data from microservice
        client = WorkspaceClient("http://0.0.0.0:4001")
        response = client.list(
            WorkspaceListRequest(pagination=pagination_request, filters=filters)
        )
        items = response.get("workspaces", [])
        pagination = response.get("pagination", {})

        # Compose edges and PageInfo
        edges = compose_edges(WorkspaceNode, items)
        page_info = compose_page_info(
            edges, pagination, pagination_request.direction, pagination_request.limit
        )

        return cls(edges=edges, page_info=page_info)
