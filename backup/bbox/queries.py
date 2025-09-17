import strawberry
from typing import List
from app.schema.bbox.types import Marker
from .resolvers import get_markers


@strawberry.type
class BBoxQueries:
    get_markers: List[Marker] = strawberry.field(resolver=get_markers)
