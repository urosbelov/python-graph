import strawberry
from strawberry import relay
from typing import Iterable, Optional
from app.schema.workspace.types import WorkspaceNode
from internal_sdk.workspace.client import (
    WorkspaceClient,
    WorkspaceListRequest,
    PaginationRequest,
)
import base64


def encode_cursor(id: int) -> str:
    return base64.b64encode(str(id).encode()).decode()


def decode_cursor(cursor: Optional[str]) -> Optional[int]:
    if cursor is None:
        return None
    return int(base64.b64decode(cursor.encode()).decode())


def map_to_workspace_node(item: dict) -> WorkspaceNode:
    allowed_keys = {f.name for f in WorkspaceNode.__dataclass_fields__.values()}
    filtered_item = {k: v for k, v in item.items() if k in allowed_keys}
    return WorkspaceNode(**filtered_item)


@strawberry.type
class WorkspaceCustomPaginationConnection(relay.Connection[WorkspaceNode]):
    @classmethod
    def resolve_connection(
        cls,
        nodes: Iterable[
            WorkspaceNode
        ] = None,  # ignored, data fetched from microservice
        *,
        info=None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        first: Optional[int] = None,
        last: Optional[int] = None,
        filters: Optional[dict] = None,
        **kwargs,
    ):
        # Decode Relay 'after' cursor
        after_id = decode_cursor(after)
        first = first or 20

        # Prepare request to microservice
        client = WorkspaceClient("http://0.0.0.0:4001")
        request = WorkspaceListRequest(
            pagination=PaginationRequest(
                limit=first, cursor=str(after_id) if after_id else None
            ),
        )
        response = client.list(request)

        # Extract items and pagination info from microservice
        items = response.get("workspaces", [])
        pagination = response.get("pagination", {})

        # Build edges with encoded cursors
        edges = [
            relay.Edge(
                node=map_to_workspace_node(item),
                cursor=encode_cursor(item["id"]),
            )
            for item in items
        ]

        # Build Relay PageInfo using microservice pagination
        page_info = relay.PageInfo(
            start_cursor=edges[0].cursor if edges else None,
            end_cursor=edges[-1].cursor if edges else None,
            has_previous_page=pagination.get("has_previous_page", after_id is not None),
            has_next_page=pagination.get("has_next_page", len(items) == first),
        )

        return cls(edges=edges, page_info=page_info)
