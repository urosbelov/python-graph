from typing import List
import strawberry

from app.schema.workspace.amenity import resolvers
from app.schema.workspace.amenity.types import WorkspaceAmenity


@strawberry.type
class WorkspaceAmenityQueries:
    workspace_amenity: WorkspaceAmenity = strawberry.field(
        resolver=resolvers.get_workspace_amenity
    )
    workspace_amenities: List[WorkspaceAmenity] = strawberry.field(
        resolver=resolvers.list_workspace_amenities
    )
