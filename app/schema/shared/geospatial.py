import strawberry


@strawberry.input
class LatLngInput:
    lat: float
    lng: float


@strawberry.type
class Location:
    latitude: float
    longitude: float


@strawberry.input
class BBoxInput:
    south_west: LatLngInput
    north_east: LatLngInput
