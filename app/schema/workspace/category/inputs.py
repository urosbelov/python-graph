from typing import Optional
import strawberry
from app.schema.workspace.category.types import WorkspaceCategoryStatus


@strawberry.input
class CreateWorkspaceCategoryInput:
    name: str
    description: Optional[str] = None
    icon: Optional[str] = None


@strawberry.input
class UpdateWorkspaceCategoryInput:
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    status: Optional[WorkspaceCategoryStatus] = None
