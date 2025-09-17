from app.context import Context
from app.core.logger import logger
import strawberry
from app.schema.post.types import Post


def get_post(self, info: strawberry.Info[Context]) -> Post:
    logger.debug(f"Fetching post with id: {id}")
    pass
