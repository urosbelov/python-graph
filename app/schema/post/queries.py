from app.core.logger import logger
from typing import List
import strawberry

from strawberry import Info
from app.context import Context
from app.helpers.converter.core import StrawberryConverter
from app.helpers.sdk.call import safe_sdk_call
from app.helpers.sdk.extract import extract_items
from app.schema.post.post_media.queries import PostMediaQueries
from app.schema.post.types import Post
from app.schema.scalars import Base62ID


@strawberry.type
class PostQueries(PostMediaQueries):
    @strawberry.field
    async def post(self, id: Base62ID, info: Info[Context]) -> Post:  # type: ignore
        converter = StrawberryConverter()
        data = await safe_sdk_call(
            info.context.workspace_api.get_workspace_by_id,
            id,
            context=info.context,
        )
        return converter.from_sdk(data, Post)

    @strawberry.field
    async def posts(self, info: Info[Context]) -> List[Post]:
        converter = StrawberryConverter()
        response = await safe_sdk_call(
            info.context.posts_api.list_posts, context=info.context
        )
        items = extract_items(response, "posts")
        return converter.from_sdk(items, Post)
