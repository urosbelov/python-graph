from types import SimpleNamespace
from typing import List
from app.schema.types.pagination import PageInfo


def dict_to_obj(d):
    """Recursively convert dicts to SimpleNamespace for attribute access."""
    if isinstance(d, dict):
        return SimpleNamespace(**{k: dict_to_obj(v) for k, v in d.items()})
    elif isinstance(d, list):
        return [dict_to_obj(i) for i in d]
    else:
        return d


def create_connection(
    nodes: List,
    pagination: dict,
    EdgeType,
    ConnectionType,
):
    """
    Wrap a list of nodes into a GraphQL connection using backend-provided UUIDs
    as cursors and SDK pagination info.

    Args:
        nodes: list of workspace dicts
        pagination: dict with keys 'next_cursor', 'previous_cursor', 'has_next_page', 'has_previous_page'
        EdgeType: GraphQL Edge type
        ConnectionType: GraphQL Connection type
    """
    edges = [
        EdgeType(
            node=dict_to_obj(node), cursor=node["id"]
        )  # use backend UUID7 as cursor
        for node in nodes
    ]

    page_info = PageInfo(
        has_next_page=pagination.get("has_next_page", False),
        has_previous_page=pagination.get("has_previous_page", False),
        next_cursor=pagination.get("next_cursor"),
        previous_cursor=pagination.get("previous_cursor"),
    )

    return ConnectionType(edges=edges, page_info=page_info)
