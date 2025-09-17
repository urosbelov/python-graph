import enum
from app.schema.shared.geospatial import Location
import strawberry


@strawberry.enum
class MarkerType(enum.Enum):
    UNSPECIFIED = "UNSPECIFIED"
    WORKSPACE = "WORKSPACE"


@strawberry.type
class Marker:
    id: strawberry.ID
    type: MarkerType
    name: str
    location: Location
