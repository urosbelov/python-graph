import strawberry

from app.schema.workspace.amenity import resolvers
from app.schema.workspace.amenity.types import WorkspaceAmenity


@strawberry.type
class WorkspaceAmenityMutations:
    create_workspace_amenity: WorkspaceAmenity = strawberry.field(
        resolver=resolvers.create_workspace_amenity
    )
