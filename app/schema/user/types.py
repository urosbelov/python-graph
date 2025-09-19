from datetime import datetime
import enum
from typing import Optional
import strawberry


@strawberry.enum
class UserStatus(enum.Enum):
    UNSPECIFIED = "unspecified"
    PENDING = "pending"
    ACTIVE = "active"
    SUSPENDED = "suspended"
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
    # Core
    id: strawberry.ID

    # Timestamps
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    deleted_by: Optional[strawberry.ID] = None

    # Personal info
    first_name: str
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    country: Optional[str] = None
    # Birthday
    birthday: Optional[datetime] = None

    # Administrations
    must_change_password: bool
