from dataclasses import fields, is_dataclass
from typing import Type, TypeVar

T = TypeVar("T")


def map_to_dataclass(cls: Type[T], data: dict) -> T:
    """
    Automatically maps a JSON-like dict to a dataclass, ignoring extra keys.

    cls: Target dataclass type
    data: Dictionary to map
    """
    if not is_dataclass(cls):
        raise ValueError(f"{cls} must be a dataclass")

    allowed_keys = {f.name for f in fields(cls)}
    filtered_data = {k: v for k, v in data.items() if k in allowed_keys}
    return cls(**filtered_data)
