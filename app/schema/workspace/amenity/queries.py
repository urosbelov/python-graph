from typing import List
import strawberry

from app.context import Context
from app.helpers.converter import StrawberryConverter
from app.helpers.sdk.call import safe_sdk_call
from app.helpers.sdk.extract import extract_items
from app.schema.workspace.amenity.types import WorkspaceAmenity


@strawberry.type
class WorkspaceAmenityQueries:

    @strawberry.field
    async def workspace_amenity(self, id: strawberry.ID) -> str:
        return f"Workspace amenity details for ID {id}"

    @strawberry.field
    async def workspace_amenities(
        self, info: strawberry.Info[Context]
    ) -> List[WorkspaceAmenity]:
        converter = StrawberryConverter()
        response = await safe_sdk_call(info.context.amenity_api.list_amenities)
        items = extract_items(response)
        return converter.from_sdk(items, WorkspaceAmenity)
