# loaders/media_loader.py
import asyncio
from typing import Any, List, Optional
from strawberry.dataloader import DataLoader
from strawberry.exceptions import GraphQLError
from media_sdk.media_sdk import MediaApi, GetMediaBatchRequest
from media_sdk.media_sdk.exceptions import ApiException


async def load_media(keys: List[str], media_api: MediaApi) -> List[Optional[Any]]:
    """
    Batch load media using the SDK batch method.
    keys: list of media IDs
    Returns a list of media objects in the same order as keys.
    """
    try:
        request_body = GetMediaBatchRequest(media_ids=keys)

        batch_response = await asyncio.to_thread(
            media_api.get_media_batch, request_body
        )

        media_dict = batch_response.items

        return [media_dict.get(str(key)) for key in keys]

    except ApiException as e:
        raise GraphQLError(f"Failed to fetch media batch: {e}")


def create_media_loader(media_api: MediaApi) -> DataLoader:
    """
    Factory function to create Strawberry DataLoader for media.
    """
    return DataLoader(load_fn=lambda keys: load_media(keys, media_api))
