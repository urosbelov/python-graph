from typing import List
import strawberry

from app.context import Context
from app.helpers.converter import StrawberryConverter
from app.helpers.sdk.call import safe_sdk_call
from app.helpers.sdk.extract import extract_items
from app.schema.workspace.category.types import WorkspaceCategory


@strawberry.type
class WorkspaceCategoryQueries:

    @strawberry.field
    async def workspace_categories(
        self, info: strawberry.Info[Context]
    ) -> List[WorkspaceCategory]:
        converter = StrawberryConverter()
        response = await safe_sdk_call(info.context.category_api.list_categories)
        items = extract_items(response)
        return converter.from_sdk(items, WorkspaceCategory)
