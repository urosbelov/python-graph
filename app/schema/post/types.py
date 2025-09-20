from typing import List, Optional
import strawberry
from strawberry import Info
from app.context import Context
from app.helpers.mapper import map_to_graphql_type
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
        # Load media objects for this post
        items = await info.context.post_media_loader.load(self.id)
        if not items:
            return None
        return [map_to_graphql_type(item, PostMedia) for item in items]
