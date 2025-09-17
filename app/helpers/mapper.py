from dataclasses import fields, is_dataclass
from typing import Type, Any
from enum import Enum


def map_to_graphql_type(sdk_obj: Any, gql_type: Type) -> Any:
    """
    Convert an SDK object to a GraphQL type by keeping only matching fields.
    Works with dicts, dataclasses, or objects with to_dict().
    """
    if sdk_obj is None:
        return None

    # Convert SDK object to dict safely
    if hasattr(sdk_obj, "to_dict"):
        data = sdk_obj.to_dict()
    elif is_dataclass(sdk_obj):
        data = {f.name: getattr(sdk_obj, f.name) for f in fields(sdk_obj)}
    elif isinstance(sdk_obj, dict):
        data = sdk_obj
    else:
        # fallback: try vars, or wrap in empty dict if it fails
        try:
            data = vars(sdk_obj)
        except TypeError:
            data = {}

    # Keep only fields that exist in GraphQL type
    gql_fields = {f.name for f in fields(gql_type)}
    filtered_data = {k: v for k, v in data.items() if k in gql_fields}

    # Convert enums to values
    for k, v in filtered_data.items():
        if isinstance(v, Enum):
            filtered_data[k] = v.value

    return gql_type(**filtered_data)
