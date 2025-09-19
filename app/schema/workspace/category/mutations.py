import strawberry

from app.schema.workspace.category.inputs import (
    CreateWorkspaceCategoryInput,
    UpdateWorkspaceCategoryInput,
)


@strawberry.type
class WorkspaceCategoryMutations:

    @strawberry.mutation
    def create_workspace_category(self, input: CreateWorkspaceCategoryInput) -> str:
        return "Category created"

    @strawberry.mutation
    def update_workspace_category(
        self, id: strawberry.ID, input: UpdateWorkspaceCategoryInput
    ) -> str:
        return "Category updated"
