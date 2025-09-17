import strawberry
from app.schema.workspace.feature import resolvers


@strawberry.type
class WorkspaceFeatureMutations:
    add_workspace_feature: bool = strawberry.field(
        resolver=resolvers.add_workspace_feature
    )
    delete_workspace_feature: bool = strawberry.field(
        resolver=resolvers.delete_workspace_feature
    )
