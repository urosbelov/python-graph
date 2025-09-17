ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BASE = len(ALPHABET)
CHAR_TO_VALUE = {c: i for i, c in enumerate(ALPHABET)}


def encode(num: int) -> str:
    """Convert a numeric ID to Base62 string."""
    if num == 0:
        return ALPHABET[0]
    result = []
    while num > 0:
        num, rem = divmod(num, BASE)
        result.append(ALPHABET[rem])
    return "".join(reversed(result))


def decode(s: str) -> int:
    """Convert a Base62 string back to numeric ID."""
    num = 0
    for c in s:
        if c not in CHAR_TO_VALUE:
            raise ValueError(f"Invalid character in Base62 string: {c}")
        num = num * BASE + CHAR_TO_VALUE[c]
    return num
