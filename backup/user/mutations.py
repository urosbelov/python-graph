import strawberry

from app.schema.user.types import User
from app.schema.user.resolvers import create_user


@strawberry.type
class UserMutations:
    create_user: User = strawberry.field(resolver=create_user)
