# loaders/user_loader.py
import asyncio
from typing import Any, List, Optional
from strawberry.dataloader import DataLoader
from strawberry.exceptions import GraphQLError
from identity_sdk.identity_sdk import UsersApi, GetUsersBatchRequest
from identity_sdk.identity_sdk.exceptions import ApiException


async def load_users(keys: List[int], users_api: UsersApi) -> List[Optional[Any]]:
    """
    Batch load users using the SDK batch method.
    keys: list of user IDs
    Returns a list of user objects in the same order as keys.
    """
    try:
        request_body = GetUsersBatchRequest(user_ids=keys)

        batch_response = await asyncio.to_thread(
            users_api.get_users_batch, request_body
        )

        users_dict = batch_response.users

        return [users_dict.get(str(key)) for key in keys]

    except ApiException as e:
        raise GraphQLError(f"Failed to fetch users batch: {e}")


def create_user_loader(users_api: UsersApi) -> DataLoader:
    """
    Factory function to create Strawberry DataLoader for users.
    """
    return DataLoader(load_fn=lambda keys: load_users(keys, users_api))
