from contextvars import Context
from app.core.logger import logger
import strawberry

from app.schema.post.inputs import CreatePostInput
from app.schema.post.types import Post


def create_post(input: CreatePostInput, info: strawberry.Info[Context]) -> Post:
    logger.debug("Creating a new post")
    pass
