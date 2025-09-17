from typing import Optional, Union
from uuid import UUID

from app.core.config import load_settings

from workspace_sdk.workspace_sdk import ApiClient, Configuration
from workspace_sdk.workspace_sdk.api.v1_api import V1Api
from workspace_sdk.workspace_sdk.models import WorkspaceResponse, WorkspaceListResponse


class WorkspaceSDK:
    """
    Wrapper for Workspace microservice SDK supporting multiple API versions (v1, v2).
    """

    def __init__(self, token: Optional[str] = None):
        settings = load_settings()

        config = Configuration(
            host=settings.get_client("workspace"),
            api_key={"Authorization": f"Bearer {token}"} if token else {},
        )
        client = ApiClient(config)

        # Versioned APIs
        self.v1 = V1Api(client)

    # -------------------------
    # V1 Methods
    # -------------------------
    def list_workspaces_v1(
        self, x_user_id: Optional[UUID] = None, x_workspace_id: Optional[int] = None
    ) -> WorkspaceListResponse:
        return self.v1.list_workspaces(
            x_user_id=x_user_id, x_workspace_id=x_workspace_id
        )

    def get_workspace_v1(
        self,
        workspace_id: Union[int, str],
        x_user_id: Optional[UUID] = None,
        x_workspace_id: Optional[int] = None,
    ) -> WorkspaceResponse:
        return self.v1.get_workspace(
            workspace_id=workspace_id,
            x_user_id=x_user_id,
            x_workspace_id=x_workspace_id,
        )
