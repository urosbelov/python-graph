import asyncio
from graphql import GraphQLError
from app.context import Context
from workspace_sdk.workspace_sdk.exceptions import ApiException


async def safe_sdk_call(func, *args, context: Context = None, **kwargs):
    """
    Run SDK call in a thread and handle ApiException.
    Automatically passes x_user_id and x_workspace_id from Strawberry context as parameters.
    Any additional kwargs are passed to the SDK method.
    """
    auto_params = {}

    if context:
        if getattr(context, "user_id", None) is not None:
            auto_params["x_user_id"] = str(context.user_id)
        if getattr(context, "workspace_id", None) is not None:
            auto_params["x_workspace_id"] = str(context.workspace_id)

    # Merge automatic params with caller kwargs
    final_kwargs = {**auto_params, **kwargs}

    try:
        return await asyncio.to_thread(func, *args, **final_kwargs)
    except ApiException as e:
        if getattr(e, "status", None) == 404:
            return None
        raise GraphQLError(f"Workspace service error: {getattr(e, 'body', str(e))}")
