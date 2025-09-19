import strawberry

from app.schema.workspace.feature.inputs import (
    CreateWorkspaceFeatureInput,
    UpdateWorkspaceFeatureInput,
)


@strawberry.type
class WorkspaceFeatureMutations:
    @strawberry.mutation
    def create_workspace_feature(self, input: CreateWorkspaceFeatureInput) -> str:
        return "Feature created"

    @strawberry.mutation
    def update_workspace_feature(
        self, id: strawberry.ID, input: UpdateWorkspaceFeatureInput
    ) -> str:
        return "Feature updated"
