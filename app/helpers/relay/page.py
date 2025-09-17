from strawberry import relay
from typing import List


def compose_page_info(
    edges: List[relay.Edge],
    pagination: dict,
    direction: str,
    limit: int,
) -> relay.PageInfo:
    """
    Builds Relay PageInfo based on edges and microservice pagination.
    """
    has_previous_page = (
        pagination.get("has_previous_page", False)
        if direction == "NEXT"
        else len(edges) == limit
    )
    has_next_page = (
        pagination.get("has_next_page", False)
        if direction == "NEXT"
        else len(edges) == limit
    )

    return relay.PageInfo(
        start_cursor=edges[0].cursor if edges else None,
        end_cursor=edges[-1].cursor if edges else None,
        has_previous_page=has_previous_page,
        has_next_page=has_next_page,
    )
