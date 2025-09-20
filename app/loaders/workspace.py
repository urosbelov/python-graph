# loaders/workspace_loader.py
import asyncio
from typing import Any, List, Optional
from strawberry.dataloader import DataLoader
from strawberry.exceptions import GraphQLError
from workspace_sdk.workspace_sdk import WorkspacesApi, GetWorkspacesBatchRequest
from workspace_sdk.workspace_sdk.exceptions import ApiException


async def load_workspaces(
    keys: List[int], workspaces_api: WorkspacesApi
) -> List[Optional[Any]]:
    """
    Batch load workspaces using the SDK batch method.
    keys: list of workspace IDs
    Returns a list of workspace objects in the same order as keys.
    """
    try:

        request_body = GetWorkspacesBatchRequest(ids=keys)

        batch_response = await asyncio.to_thread(
            workspaces_api.get_workspaces_batch, request_body
        )

        workspaces_dict = batch_response.workspaces

        return [workspaces_dict.get(str(key)) for key in keys]

    except ApiException as e:
        raise GraphQLError(f"Failed to fetch workspaces batch: {e}")


def create_workspace_loader(workspaces_api: WorkspacesApi) -> DataLoader:
    """
    Factory function to create Strawberry DataLoader for workspaces.
    """
    return DataLoader(load_fn=lambda keys: load_workspaces(keys, workspaces_api))
