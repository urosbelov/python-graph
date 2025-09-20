from functools import cached_property
from typing import Optional
import os
from strawberry.dataloader import DataLoader


from strawberry.fastapi import BaseContext
from app.loaders.amenity import create_amenity_loader
from app.loaders.media import create_media_loader
from app.loaders.post_media import create_post_media_loader
from app.loaders.posts import create_post_loader
from app.loaders.user import create_user_loader
from app.loaders.workspace import create_workspace_loader
from media_sdk.media_sdk.api.media_api import ApiClient as MediaApiClient, MediaApi
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

from post_sdk.post_sdk import ApiClient as PostApiClient, PostsApi, PostMediaApi
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
    def media_api(self) -> MediaApi:
        host = os.getenv("MEDIA_SERVICE_URL", "http://0.0.0.0:4007")
        config = Configuration()
        config.host = host
        config.retries = 3
        config.timeout = 10.0
        return MediaApi(MediaApiClient(configuration=config))

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

    @cached_property
    def posts_api(self) -> PostsApi:
        host = os.getenv("POST_SERVICE_URL", "http://0.0.0.0:4003")
        config = Configuration()
        config.host = host
        config.retries = 3
        config.timeout = 10.0
        return PostsApi(PostApiClient(configuration=config))

    @cached_property
    def post_media_api(self) -> PostMediaApi:
        host = os.getenv("POST_SERVICE_URL", "http://0.0.0.0:4003")
        config = Configuration()
        config.host = host
        config.retries = 3
        config.timeout = 10.0
        return PostMediaApi(PostApiClient(configuration=config))

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

    @cached_property
    def posts_loader(self) -> DataLoader:
        return create_post_loader(self.posts_api)

    @cached_property
    def post_media_loader(self) -> DataLoader:
        return create_post_media_loader(self.post_media_api)

    @cached_property
    def workspaces_loader(self) -> DataLoader:
        return create_workspace_loader(self.workspace_api)

    @cached_property
    def media_loader(self) -> DataLoader:
        return create_media_loader(self.media_api)


async def get_context() -> Context:
    return Context()
