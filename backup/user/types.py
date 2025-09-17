import enum
from typing import Optional
import strawberry


@strawberry.input
class CreateUserInput:
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: str
    country: Optional[str] = None


@strawberry.enum
class UserStatus(enum.Enum):
    UNSPECIFIED = "unspecified"
    PENDING = "pending"
    ACTIVE = "active"
    BLOCKED = "blocked"
    DELETED = "deleted"


@strawberry.input
class UserFiltersInput:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    country: Optional[str] = None
    status: Optional[UserStatus] = None


@strawberry.type()
class User:
    id: strawberry.ID
    first_name: str
    middle_name: Optional[str]
    last_name: str
