from functools import cached_property
from typing import Optional
import os
from strawberry.dataloader import DataLoader


from strawberry.fastapi import BaseContext
from app.loaders.amenity import create_amenity_loader
from app.loaders.user import create_user_loader
from workspace_sdk.workspace_sdk import (
    ApiClient as WorkspaceApiClient,
    Configuration,
    WorkspacesApi,
    CategoriesApi,
    AmenitiesApi,
    FeaturesApi,
)
from identity_sdk.identity_sdk import (
    ApiClient as IdentityApiClient,
    UsersApi,
    SessionsApi,
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

        return WorkspacesApi(WorkspaceApiClient(configuration=config))

    @cached_property
    def category_api(self) -> CategoriesApi:
        host = os.getenv("WORKSPACE_SERVICE_URL", "http://0.0.0.0:4001")
        config = Configuration()
        config.host = host
        config.retries = 3
        config.timeout = 10.0
        return CategoriesApi(WorkspaceApiClient(configuration=config))

    @cached_property
    def amenity_api(self) -> AmenitiesApi:
        host = os.getenv("WORKSPACE_SERVICE_URL", "http://0.0.0.0:4001")
        config = Configuration()
        config.host = host
        config.retries = 3
        config.timeout = 10.0
        return AmenitiesApi(WorkspaceApiClient(configuration=config))

    @cached_property
    def feature_api(self) -> FeaturesApi:
        host = os.getenv("WORKSPACE_SERVICE_URL", "http://0.0.0.0:4001")
        config = Configuration()
        config.host = host
        config.retries = 3
        config.timeout = 10.0
        return FeaturesApi(WorkspaceApiClient(configuration=config))

    @cached_property
    def users_api(self) -> UsersApi:
        host = os.getenv("WORKSPACE_SERVICE_URL", "http://0.0.0.0:4006")
        config = Configuration()
        config.host = host
        config.retries = 3
        config.timeout = 10.0
        return UsersApi(IdentityApiClient(configuration=config))

    @cached_property
    def sessions_api(self) -> SessionsApi:
        host = os.getenv("WORKSPACE_SERVICE_URL", "http://0.0.0.0:4006")
        config = Configuration()
        config.host = host
        config.retries = 3
        config.timeout = 10.0
        return SessionsApi(IdentityApiClient(configuration=config))

    # ----------
    # DATALOADERS
    # ----------
    @cached_property
    def category_loader(self) -> DataLoader:
        return create_category_loader(self.category_api)

    @cached_property
    def amenity_loader(self) -> DataLoader:
        return create_amenity_loader(self.amenity_api)

    @cached_property
    def users_loader(self) -> DataLoader:
        return create_user_loader(self.users_api)


async def get_context() -> Context:
    return Context()
