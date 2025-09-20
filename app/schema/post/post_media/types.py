from typing import List, Optional
import strawberry
from app.context import Context
from app.schema.scalars import Base62ID
from media_sdk.media_sdk.models.media import Media


@strawberry.type
class MediaField:
    thumbnail: Optional[str] = None
    medium: Optional[str] = None


@strawberry.type
class PostMedia:
    # Core
    id: strawberry.ID
    post_id: Base62ID  # type: ignore
    alt_text: Optional[str] = None
    media_id: strawberry.ID

    @strawberry.field
    async def media(self, info: strawberry.Info[Context]) -> Optional[List[MediaField]]:
        items: Optional[List[Media]] = await info.context.media_loader.load(
            self.media_id
        )
        if not items:
            return []
        return [
            MediaField(thumbnail=item.variants["webp_80"], medium=None)
            for item in items
        ]
