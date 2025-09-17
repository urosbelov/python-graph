from app.core.logger import logger
from app.schema.user.types import User


def populate_workspace_created_by(self) -> User:
    logger.debug(f"Resolving created_by_user for created_by: {self.created_by}")
    return User(
        id=self.created_by,
        first_name="Uros",
        middle_name="Zdravko",
        last_name="Kalajdzic",
    )
