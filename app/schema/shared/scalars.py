import strawberry
from app.helpers import base62

# Functional scalar for Base62 IDs
Base62ID = strawberry.scalar(
    int,  # underlying type is numeric ID
    serialize=lambda numeric_id: base62.encode(numeric_id),
    parse_value=lambda value: base62.decode(value),
)
