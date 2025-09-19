from typing import Optional
import strawberry


@strawberry.input
class CreateUserInput:
    # Personal info
    first_name: str
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    country: Optional[str] = None

    # Core
    identifier_type: str
    identifier_value: str
