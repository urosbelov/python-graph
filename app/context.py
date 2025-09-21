from functools import cached_property
from typing import Optional

from strawberry.fastapi import BaseContext
from strawberry.dataloader import DataLoader

# ---- Load Settings ----
from app.core.config import load_settings

settings = load_settings()

# ---- Loaders ----
from app.loaders.amenity import create_amenity_loader
from app.loaders.media import create_media_loader
from app.loaders.post_media import create_post_media_loader
from app.loaders.posts import create_post_loader
from app.loaders.user import create_user_loader
from app.loaders.workspace import create_workspace_loader
from app.loaders.category import create_category_loader

# ---- SDK Clients ----
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


# -------------------
# Shared API Builder
# -------------------
def build_api(api_cls, client_cls, client_key: str):
    """Helper to build an API client using Settings.get_client()."""
    host = settings.get_client(client_key)
    config = Configuration()
    config.host = host
    config.retries = 3
    config.timeout = 10.0
    return api_cls(client_cls(configuration=config))


class Context(BaseContext):
    # -------------------
    # Request Info
    # -------------------
    @cached_property
    def user_id(self) -> Optional[str]:
        return self.request.headers.get("x-user-id") if self.request else None

    @cached_property
    def workspace_id(self) -> Optional[str]:
        return self.request.headers.get("x-workspace-id") if self.request else None

    # -------------------
    # API Clients
    # -------------------
    @cached_property
    def workspace_api(self) -> WorkspacesApi:
        return build_api(WorkspacesApi, WorkspaceApiClient, "workspace")

    @cached_property
    def media_api(self) -> MediaApi:
        return build_api(MediaApi, MediaApiClient, "media")

    @cached_property
    def category_api(self) -> CategoriesApi:
        return build_api(CategoriesApi, WorkspaceApiClient, "workspace")

    @cached_property
    def amenity_api(self) -> AmenitiesApi:
        return build_api(AmenitiesApi, WorkspaceApiClient, "workspace")

    @cached_property
    def feature_api(self) -> FeaturesApi:
        return build_api(FeaturesApi, WorkspaceApiClient, "workspace")

    @cached_property
    def users_api(self) -> UsersApi:
        return build_api(UsersApi, IdentityApiClient, "identity")

    @cached_property
    def sessions_api(self) -> SessionsApi:
        return build_api(SessionsApi, IdentityApiClient, "identity")

    @cached_property
    def posts_api(self) -> PostsApi:
        return build_api(PostsApi, PostApiClient, "post")

    @cached_property
    def post_media_api(self) -> PostMediaApi:
        return build_api(PostMediaApi, PostApiClient, "post")

    # -------------------
    # Dataloaders
    # -------------------
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


# -------------------
# Context Factory
# -------------------
async def get_context() -> Context:
    return Context()
