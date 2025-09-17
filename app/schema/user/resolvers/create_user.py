from app.core.logger import logger
from app.schema.user.types import CreateUserInput, User


def create_user(input: CreateUserInput) -> User:
    logger.debug(f"Creating user with input: {input}")
    return User()
