from functools import cached_property
from typing import Optional
import os
from strawberry.dataloader import DataLoader


from strawberry.fastapi import BaseContext
from workspace_sdk.workspace_sdk import (
    ApiClient,
    WorkspacesApi,
    CategoriesApi,
    Configuration,
)
from app.loaders.category import create_category_loader


class Context(BaseContext):
    @cached_property
    def user_id(self) -> Optional[str]:
        if not self.request:
            return None
        return self.request.headers.get("x-user-id")

    @cached_property
    def workspace_id(self) -> Optional[str]:
        if not self.request:
            return None
        return self.request.headers.get("x-workspace-id")

    @cached_property
    def workspace_api(self) -> WorkspacesApi:
        """Workspace API client, configured per environment."""
        host = os.getenv("WORKSPACE_SERVICE_URL", "http://0.0.0.0:4001")

        config = Configuration()
        config.host = host

        # optionally configure timeouts / retries
        config.retries = 3
        config.timeout = 10.0

        client = ApiClient(configuration=config)
        return WorkspacesApi(client)

    @cached_property
    def category_api(self) -> CategoriesApi:
        host = os.getenv("WORKSPACE_SERVICE_URL", "http://0.0.0.0:4001")
        config = Configuration()
        config.host = host
        config.retries = 3
        config.timeout = 10.0
        return CategoriesApi(ApiClient(configuration=config))

    # ----------
    # DATALOADERS
    # ----------
    @cached_property
    def category_loader(self) -> DataLoader:
        return create_category_loader(self.category_api)


async def get_context() -> Context:
    return Context()
