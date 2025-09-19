# loaders/post_loader.py
import asyncio
from typing import Any, List, Optional
from strawberry.dataloader import DataLoader
from strawberry.exceptions import GraphQLError
from post_sdk.post_sdk import PostsApi, GetPostsBatchRequest
from post_sdk.post_sdk.exceptions import ApiException


async def load_posts(keys: List[int], posts_api: PostsApi) -> List[Optional[Any]]:
    """
    Batch load posts using the SDK batch method.
    keys: list of post IDs
    Returns a list of post objects in the same order as keys.
    """
    try:
        request_body = GetPostsBatchRequest(ids=keys)

        batch_response = await asyncio.to_thread(
            posts_api.get_posts_batch, request_body
        )

        posts_dict = batch_response.posts

        return [posts_dict.get(str(key)) for key in keys]

    except ApiException as e:
        raise GraphQLError(f"Failed to fetch posts batch: {e}")


def create_post_loader(posts_api: PostsApi) -> DataLoader:
    """
    Factory function to create Strawberry DataLoader for posts.
    """
    return DataLoader(load_fn=lambda keys: load_posts(keys, posts_api))
