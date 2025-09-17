from typing import Optional
from internal_sdk.workspace.client import PaginationRequest
from app.helpers.relay.encoder import decode_cursor


def compose_pagination_request(
    first: Optional[int] = None,
    last: Optional[int] = None,
    before: Optional[str] = None,
    after: Optional[str] = None,
    default_limit: int = 20,
) -> PaginationRequest:
    """
    Converts Relay pagination parameters into a microservice PaginationRequest.

    - first: number of items forward
    - last: number of items backward
    - before: cursor to paginate backward
    - after: cursor to paginate forward
    """
    after_id = decode_cursor(after)
    before_id = decode_cursor(before)

    # Determine direction and cursor
    if first is not None:
        direction = "NEXT"
        cursor = after_id
        limit = first
    elif last is not None:
        direction = "PREV"
        cursor = before_id
        limit = last
    else:
        direction = "NEXT"
        cursor = None
        limit = default_limit

    return PaginationRequest(
        limit=limit,
        cursor=str(cursor) if cursor is not None else None,
        direction=direction,
    )
