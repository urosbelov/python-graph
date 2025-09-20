from typing import List
import strawberry

from app.context import Context
from app.helpers.converter.core import StrawberryConverter
from app.helpers.sdk.call import safe_sdk_call
from app.helpers.sdk.extract import extract_items
from app.schema.user.types import User


@strawberry.type
class UserQueries:

    @strawberry.field
    async def users(self, info: strawberry.Info[Context]) -> List[User]:
        converter = StrawberryConverter()
        response = await safe_sdk_call(
            info.context.users_api.list_users, context=info.context
        )
        items = extract_items(response)
        return converter.from_sdk(items, User)
