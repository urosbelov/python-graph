import strawberry


@strawberry.input
class WorkspaceFeatureInput:
    workspace_id: strawberry.ID
    amenity_id: int
