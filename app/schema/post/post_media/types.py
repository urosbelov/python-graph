from typing import List, Optional
import strawberry
from app.schema.scalars import Base62ID


@strawberry.type
class MediaField:
    thumbnail: str
    medium: str


@strawberry.type
class PostMedia:
    # Core
    id: strawberry.ID
    post_id: Base62ID  # type: ignore
    alt_text: Optional[str] = None
    media_id: strawberry.ID

    @strawberry.field
    def media(self, info) -> Optional[List[MediaField]]:
        first = MediaField(thumbnail="thumbnail_url", medium="medium_url")
        second = MediaField(thumbnail="thumbnail_url_2", medium="medium_url_2")
        return [first, second]
