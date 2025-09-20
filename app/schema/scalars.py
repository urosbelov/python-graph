import strawberry
from typing import NewType
from app.helpers.base62id import encode_base62, decode_base62


Base62ID = strawberry.scalar(
    NewType("Base62ID", int),
    serialize=lambda v: encode_base62(v),  # Python int → Base62 string
    parse_value=lambda v: decode_base62(v),  # Base62 string → Python int
)
