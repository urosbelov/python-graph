from typing import List
import strawberry

from strawberry import Info, ID
from app.context import Context
from app.helpers.mapper import map_to_graphql_type
from app.helpers.sdk.call import safe_sdk_call
from app.helpers.sdk.extract import extract_items
from app.schema.post.post_media.queries import PostMediaQueries
from app.schema.post.types import Post


@strawberry.type
class PostQueries(PostMediaQueries):
    @strawberry.field
    async def post(self, id: ID, info: Info[Context]) -> Post:
        workspace_data = await safe_sdk_call(
            info.context.workspace_api.get_workspace_by_id,
            id,
            context=info.context,
        )
        return map_to_graphql_type(workspace_data, Post) if workspace_data else None

    @strawberry.field
    async def posts(self, info: Info[Context]) -> List[Post]:
        response = await safe_sdk_call(
            info.context.posts_api.list_posts, context=info.context
        )
        items = extract_items(response, "posts")
        return [map_to_graphql_type(item, Post) for item in items]
