from app.core.logger import logger

from dataclasses import fields, is_dataclass
from typing import Type, TypeVar
from internal_sdk.workspace.client import WorkspaceClient

T = TypeVar("T")

import httpx
from app.core.logger import logger


async def get_workspaces_batch(keys):
    logger.debug(f"Fetching workspaces for keys: {keys}")
    async with httpx.AsyncClient(base_url="http://0.0.0.0:4001") as client:
        response = await client.post("/api/v1/workspaces/batch", json={"ids": keys})
        response.raise_for_status()
        return response.json()  #


def map_to_dataclass(cls: Type[T], item: dict) -> T:
    """
    Dynamically map a dict to a Strawberry dataclass of type `cls`.
    Only fields defined in the dataclass are used.
    """
    if not is_dataclass(cls):
        raise ValueError(f"{cls.__name__} is not a dataclass")

    allowed_keys = {f.name for f in fields(cls)}
    filtered_item = {k: v for k, v in item.items() if k in allowed_keys}
    return cls(**filtered_item)
