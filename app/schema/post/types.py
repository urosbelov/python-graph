from typing import List, Optional
import strawberry
from strawberry import Info
from app.context import Context
from app.helpers.converter.core import StrawberryConverter
from app.schema.post.post_media.types import PostMedia
from app.schema.scalars import Base62ID


@strawberry.type
class Post:
    # Core
    id: Base62ID  # type: ignore
    description: Optional[str] = None
    workspace_id: Optional[strawberry.ID] = None

    @strawberry.field
    async def media(self, info: Info[Context]) -> Optional[List[PostMedia]]:
        converter = StrawberryConverter()
        items = await info.context.post_media_loader.load(self.id)
        return converter.from_sdk(items, PostMedia)
