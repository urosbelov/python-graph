# loaders/category_loader.py
import asyncio
from typing import Any, List, Optional
from strawberry.dataloader import DataLoader
from strawberry.exceptions import GraphQLError
from workspace_sdk.workspace_sdk import CategoriesApi, GetCategoriesBatchRequest
from workspace_sdk.workspace_sdk.exceptions import ApiException


async def load_categories(
    keys: List[int], categories_api: CategoriesApi
) -> List[Optional[Any]]:
    """
    Batch load categories using the SDK batch method.
    keys: list of category IDs
    Returns a list of category objects in the same order as keys.
    """
    try:
        request_body = GetCategoriesBatchRequest(category_ids=keys)

        batch_response = await asyncio.to_thread(
            categories_api.get_categories_batch, request_body
        )

        categories_dict = batch_response.categories

        return [categories_dict.get(str(key)) for key in keys]

    except ApiException as e:
        raise GraphQLError(f"Failed to fetch categories batch: {e}")


def create_category_loader(category_api: CategoriesApi) -> DataLoader:
    """
    Factory function to create Strawberry DataLoader for categories.
    """
    return DataLoader(load_fn=lambda keys: load_categories(keys, category_api))
