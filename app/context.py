from functools import cached_property
from typing import Optional
from strawberry.fastapi import BaseContext
from app.schema.workspace.dataloaders import workspace_loader


class Context(BaseContext):
    @cached_property
    def user_id(self) -> Optional[str]:
        if not self.request:
            return None
        # Extract user_id from headers or authorization logic
        # Example: return authorization_service.get_user_id(self.request.headers.get("Authorization"))
        return self.request.headers.get("x-user-id")

    @cached_property
    def workspace_id(self) -> Optional[str]:
        if not self.request:
            return None
        return self.request.headers.get("x-workspace-id")

    @cached_property
    def workspace_loader(self):
        return workspace_loader


async def get_context() -> Context:
    return Context()
