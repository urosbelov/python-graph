from internal_sdk.workspace.client import PaginationRequest
from app.schema.shared.pagination import PageRequest


def build_pagination(page: PageRequest | None) -> PaginationRequest:
    """
    Convert a GraphQL PageRequest to SDK PaginationRequest,
    handling defaults and enum-to-string conversion automatically.
    """
    return PaginationRequest(
        limit=page.limit if page and page.limit is not None else 20,
        cursor=page.cursor if page else None,
        direction=page.direction.value if page and page.direction else "NEXT",
    )
