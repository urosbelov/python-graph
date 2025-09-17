import strawberry

from app.schema.media.types import Media
from .resolvers import get_media, get_signed_url


@strawberry.type
class MediaQueries:
    get_media: Media = strawberry.field(resolver=get_media)
    get_signed_url: bool = strawberry.field(resolver=get_signed_url)
