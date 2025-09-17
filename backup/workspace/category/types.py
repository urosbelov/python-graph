import strawberry


@strawberry.type
class WorkspaceCategory:
    id: strawberry.ID
    name: str
    created_at: str
    updated_at: str
