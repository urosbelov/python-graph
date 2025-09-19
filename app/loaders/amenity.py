# loaders/amenity_loader.py
import asyncio
from typing import Any, List, Optional
from strawberry.dataloader import DataLoader
from strawberry.exceptions import GraphQLError
from workspace_sdk.workspace_sdk import AmenitiesApi, GetAmenitiesBatchRequest
from workspace_sdk.workspace_sdk.exceptions import ApiException


async def load_amenities(
    keys: List[int], amenities_api: AmenitiesApi
) -> List[Optional[Any]]:
    """
    Batch load amenities using the SDK batch method.
    keys: list of amenity IDs
    Returns a list of amenity objects in the same order as keys.
    """
    try:
        request_body = GetAmenitiesBatchRequest(amenity_ids=keys)

        batch_response = await asyncio.to_thread(
            amenities_api.get_amenities_batch, request_body
        )

        amenities_dict = batch_response.amenities

        return [amenities_dict.get(str(key)) for key in keys]

    except ApiException as e:
        raise GraphQLError(f"Failed to fetch amenities batch: {e}")


def create_amenity_loader(amenities_api: AmenitiesApi) -> DataLoader:
    """
    Factory function to create Strawberry DataLoader for amenities.
    """
    return DataLoader(load_fn=lambda keys: load_amenities(keys, amenities_api))
