# loaders/category_loader.py
import asyncio
from typing import Any, List, Optional
from strawberry.dataloader import DataLoader
from strawberry.exceptions import GraphQLError
from workspace_sdk.workspace_sdk import CategoriesApi, BatchCategoriesRequest
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
        # Wrap keys into SDK request model
        request_body = BatchCategoriesRequest(ids=keys)

        # Call SDK batch method in thread
        batch_response = await asyncio.to_thread(
            categories_api.batch_categories, request_body
        )

        # Extract the inner dict of categories
        categories_dict = batch_response.get("categories", {})

        # Map results to the same order as requested keys
        return [categories_dict.get(str(key)) for key in keys]

    except ApiException as e:
        raise GraphQLError(f"Failed to fetch categories batch: {e}")


def create_category_loader(category_api: CategoriesApi) -> DataLoader:
    """
    Factory function to create Strawberry DataLoader for categories.
    """
    return DataLoader(load_fn=lambda keys: load_categories(keys, category_api))
