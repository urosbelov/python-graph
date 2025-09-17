import base64
from typing import Optional


def encode_cursor(id: int) -> str:
    return base64.b64encode(str(id).encode()).decode()


def decode_cursor(cursor: Optional[str]) -> Optional[int]:
    if cursor is None:
        return None
    return int(base64.b64decode(cursor.encode()).decode())
