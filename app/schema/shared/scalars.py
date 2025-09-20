import strawberry
from app.helpers.base62id import decode_base62, encode_base62

# Functional scalar for Base62 IDs
Base62ID = strawberry.scalar(
    int,  # underlying type is numeric ID
    serialize=lambda numeric_id: encode_base62(numeric_id),
    parse_value=lambda value: decode_base62(value),
)
