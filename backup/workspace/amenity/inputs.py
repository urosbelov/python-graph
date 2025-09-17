from typing import Optional
import strawberry


@strawberry.input
class CreateWorkspaceAmenityInput:
    name: str
    type: str
    icon: Optional[str] = None
    description: Optional[str] = None
