from typing import Optional
import strawberry


@strawberry.input
class CreateWorkspaceCategoryInput:
    name: str
    description: Optional[str] = None


@strawberry.input
class UpdateWorkspaceCategoryInput:
    name: Optional[str]
    description: Optional[str]
