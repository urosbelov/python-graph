from typing import Optional
import strawberry


@strawberry.input
class CreatePostInput:
    description: Optional[str]
