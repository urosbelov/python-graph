from typing import List, Optional
import strawberry

from app.schema.types.pagination import PageInfo
from internal_sdk.place.google.client import GooglePlaceClient
from strawberry.dataloader import DataLoader

from typing import Type, TypeVar, Any
from dataclasses import is_dataclass


T = TypeVar("T")


def map_to_strawberry(obj: Any, cls: Type[T]) -> T:
    """
    Map a dict or dataclass-like object to a Strawberry dataclass,
    assigning only the fields that exist in the target type.
    """
    # Get field names from target Strawberry dataclass
    field_names = {f.name for f in cls.__dataclass_fields__.values()}

    # Convert obj to dict
    if is_dataclass(obj):
        data = obj.__dict__
    elif isinstance(obj, dict):
        data = obj
    else:
        # fallback: use __dict__ of any object
        data = getattr(obj, "__dict__", {})

    # Filter keys to match target fields
    filtered = {k: v for k, v in data.items() if k in field_names}

    return cls(**filtered)


@strawberry.type
class Place:
    id: str
    google_place_id: str
    display_name: str


async def load_places(keys: List[str]) -> List[Place]:
    place_client = GooglePlaceClient("http://0.0.0.0:4002")
    places_list = place_client.places(keys)
    return [map_to_strawberry(place_info, Place) for place_info in places_list]


@strawberry.type
class Workspace:
    id: strawberry.ID
    name: str
    google_place_id: str

    @strawberry.field
    async def location(self, info) -> Place:
        loader: DataLoader = info.context["places_loader"]
        return await loader.load(self.google_place_id)


@strawberry.input
class WorkspaceFilters:
    name: Optional[str] = None


@strawberry.type
class WorkspaceEdge:
    node: Workspace
    cursor: str


@strawberry.type
class WorkspaceConnection:
    edges: list[WorkspaceEdge]
    page_info: PageInfo
