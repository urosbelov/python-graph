from enum import Enum
from typing import Optional
import strawberry


@strawberry.type
class PageInfo:
    has_next_page: bool
    has_previous_page: bool
    next_cursor: Optional[str] = None
    previous_cursor: Optional[str] = None


@strawberry.enum
class PageDirection(Enum):
    NEXT = "NEXT"
    PREV = "PREV"


@strawberry.input
class PageRequest:
    limit: Optional[int] = 20
    cursor: Optional[str] = None
    direction: PageDirection = PageDirection.NEXT
