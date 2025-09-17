import asyncio

from graphql import GraphQLError
from workspace_sdk.workspace_sdk.exceptions import ApiException


async def safe_sdk_call(func, *args, **kwargs):
    """Run SDK call in thread and handle ApiException."""
    try:
        return await asyncio.to_thread(func, *args, **kwargs)
    except ApiException as e:
        if getattr(e, "status", None) == 404:
            return None
        raise GraphQLError(f"Workspace service error: {getattr(e, 'body', str(e))}")
