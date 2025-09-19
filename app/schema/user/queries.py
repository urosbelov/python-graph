from typing import List
import strawberry

from app.context import Context
from app.helpers.mapper import map_to_graphql_type
from app.helpers.sdk.call import safe_sdk_call
from app.helpers.sdk.extract import extract_items
from app.schema.user.types import User


@strawberry.type
class UserQueries:

    @strawberry.field
    async def users(self, info: strawberry.Info[Context]) -> List[User]:
        response = await safe_sdk_call(
            info.context.users_api.list_users, context=info.context
        )
        items = extract_items(response)
        return [map_to_graphql_type(item, User) for item in items]
