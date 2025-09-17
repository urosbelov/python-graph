import strawberry


@strawberry.type
class Media:
    id: strawberry.ID
    url: str
    type: str
    created_at: str
    updated_at: str
