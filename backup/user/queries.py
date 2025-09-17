from typing import List
import strawberry

from app.schema.user.resolvers import get_user, list_users
from app.schema.user.types import User


@strawberry.type
class UserQueries:
    user: User = strawberry.field(resolver=get_user)
    users: List[User] = strawberry.field(resolver=list_users)
