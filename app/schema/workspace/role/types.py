import strawberry


@strawberry.type
class WorkspaceRole:
    # Core
    id: strawberry.ID

    # Timestamps
    created_at: str
    created_by: strawberry.ID

    # Base
    name: str
    description: str
