import strawberry


@strawberry.input
class LocationInput:
    latitude: float
    longitude: float


@strawberry.type
class Location:
    latitude: float
    longitude: float


@strawberry.input
class BBoxInput:
    south_west: LocationInput
    north_east: LocationInput
