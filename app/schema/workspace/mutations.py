import strawberry

from app.schema.workspace.types import Workspace
from app.schema.workspace.resolvers import create_workspace, update_workspace
from app.schema.workspace.amenity.mutations import WorkspaceAmenityMutations
from app.schema.workspace.category.mutations import WorkspaceCategoryMutations
from app.schema.workspace.feature.mutations import WorkspaceFeatureMutations


@strawberry.type
class WorkspaceMutations(
    WorkspaceAmenityMutations, WorkspaceCategoryMutations, WorkspaceFeatureMutations
):
    create_workspace: Workspace = strawberry.field(resolver=create_workspace)
    update_workspace: Workspace = strawberry.field(resolver=update_workspace)
