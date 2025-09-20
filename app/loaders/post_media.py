# loaders/post_media_loader.py
import asyncio
from typing import Any, List, Optional
from strawberry.dataloader import DataLoader
from strawberry.exceptions import GraphQLError
from post_sdk.post_sdk import PostMediaApi, GetPostMediaBatchRequest
from post_sdk.post_sdk.exceptions import ApiException


async def load_post_media(
    keys: List[int], post_media_api: PostMediaApi
) -> List[Optional[Any]]:
    """
    Batch load post media using the SDK batch method.
    keys: list of post media IDs
    Returns a list of post media objects in the same order as keys.
    """
    try:
        request_body = GetPostMediaBatchRequest(post_ids=keys)

        batch_response = await asyncio.to_thread(
            post_media_api.get_post_media_batch, request_body
        )

        media_dict = batch_response.post_media

        return [media_dict.get(str(key)) for key in keys]

    except ApiException as e:
        raise GraphQLError(f"Failed to fetch post media batch: {e}")


def create_post_media_loader(post_media_api: PostMediaApi) -> DataLoader:
    """
    Factory function to create Strawberry DataLoader for post media.
    """
    return DataLoader(load_fn=lambda keys: load_post_media(keys, post_media_api))
