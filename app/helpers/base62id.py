# base62id.py

import string

# ---------- Base62 Alphabet ----------
ALPHABET = string.digits + string.ascii_letters  # 0-9, A-Z, a-z
BASE = len(ALPHABET)


# ---------- Base62 Encode / Decode ----------
def encode_base62(num: int) -> str:
    """Encode a 64-bit integer (Sonyflake ID) into Base62 string."""
    if num < 0:
        raise ValueError("Base62 encoding only supports non-negative integers")
    if num == 0:
        return ALPHABET[0]
    result = ""
    while num > 0:
        num, rem = divmod(num, BASE)
        result = ALPHABET[rem] + result
    return result


def decode_base62(s: str) -> int:
    """Decode a Base62 string back to integer (Sonyflake ID)."""
    num = 0
    for char in s:
        index = ALPHABET.find(char)
        if index == -1:
            raise ValueError(f"Invalid Base62 character: {char}")
        num = num * BASE + index
    return num


# ---------- Base62ID Class ----------
class Base62ID:
    """
    Wraps a Sonyflake ID for Base62 serialization.
    Can be used in URLs, GraphQL, or anywhere a compact unique ID is needed.
    """

    def __init__(self, id: int):
        if not isinstance(id, int):
            raise TypeError("id must be an integer")
        if id < 0:
            raise ValueError("id must be non-negative")
        self.id = id

    def __str__(self) -> str:
        return encode_base62(self.id)

    def __repr__(self) -> str:
        return f"<Base62ID {str(self)}>"

    @classmethod
    def from_string(cls, s: str):
        return cls(decode_base62(s))

    def __int__(self) -> int:
        return self.id

    def __eq__(self, other) -> bool:
        if isinstance(other, Base62ID):
            return self.id == other.id
        if isinstance(other, int):
            return self.id == other
        return False

    def __hash__(self) -> int:
        return hash(self.id)
