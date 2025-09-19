import strawberry

from app.schema.workspace.role.types import WorkspaceRole


@strawberry.type
class WorkspaceMembership:
    # Core
    id: strawberry.ID
    created_by: strawberry.ID

    # Timestamps
    created_at: str
    updated_at: str

    # Base
    user_id: strawberry.ID
    workspace_id: strawberry.ID
    role: WorkspaceRole
