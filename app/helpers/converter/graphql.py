from typing import Type, Any, List, Union, get_origin, get_args, ForwardRef
from dataclasses import is_dataclass
from enum import Enum
from strawberry.types.field import StrawberryField
import inspect


def map_to_graphql_type(sdk_obj: Any, gql_type: Type) -> Any:
    if sdk_obj is None:
        return None

    # Convert SDK object to dict
    if isinstance(sdk_obj, dict):
        data = sdk_obj
    elif hasattr(sdk_obj, "to_dict"):
        data = sdk_obj.to_dict()
    elif is_dataclass(sdk_obj):
        data = {
            f.name: getattr(sdk_obj, f.name)
            for f in sdk_obj.__dataclass_fields__.values()
        }
    else:
        try:
            data = vars(sdk_obj)
        except TypeError:
            return sdk_obj  # Return raw value if conversion fails

    # Get constructor fields for gql_type
    init_fields = {}
    if hasattr(gql_type, "__annotations__"):
        for name, f_type in gql_type.__annotations__.items():
            # Skip fields with resolvers
            field = getattr(gql_type, name, None)
            if isinstance(field, StrawberryField) and field.resolver is not None:
                continue  # Skip fields with explicit resolvers
            init_fields[name] = f_type

    # Get valid constructor parameters
    constructor_params = set()
    if hasattr(gql_type, "__init__"):
        sig = inspect.signature(gql_type.__init__)
        constructor_params = set(sig.parameters.keys()) - {"self"}  # Exclude 'self'

    mapped_data = {}
    for name, f_type in init_fields.items():
        if name not in constructor_params:
            continue  # Skip fields not in constructor
        value = data.get(name)

        if value is None:
            mapped_data[name] = None
            continue

        # Handle forward references
        if isinstance(f_type, (str, ForwardRef)):
            continue  # Skip unresolved types

        origin = get_origin(f_type)
        args = get_args(f_type)

        # Handle Optional[T] (Union[T, NoneType])
        if origin is Union and type(None) in args:
            inner_type = next((a for a in args if a is not type(None)), None)
            if inner_type is None or isinstance(inner_type, (str, ForwardRef)):
                continue  # Skip invalid inner types
            mapped_data[name] = map_to_graphql_type(value, inner_type)
        # Handle Strawberry Union types
        elif hasattr(f_type, "_type_definition") and f_type._type_definition.is_union:
            for union_type in f_type._type_definition.union_types:
                try:
                    mapped_data[name] = map_to_graphql_type(value, union_type)
                    break
                except (TypeError, ValueError):
                    continue
            else:
                mapped_data[name] = None  # No valid union type matched
        # Handle List[T]
        elif origin in (list, List):
            inner_type = args[0] if args else None
            if inner_type is None or isinstance(inner_type, (str, ForwardRef)):
                continue  # Skip invalid inner types
            if not isinstance(value, (list, tuple)):
                continue  # Skip invalid list data
            mapped_data[name] = [map_to_graphql_type(v, inner_type) for v in value]
        # Handle Enum
        elif isinstance(f_type, type) and issubclass(f_type, Enum):
            mapped_data[name] = value.value if isinstance(value, Enum) else value
        # Handle nested Strawberry types or dataclasses
        elif is_dataclass(f_type) or (
            hasattr(f_type, "_type_definition")
            and f_type._type_definition.is_graphql_type
        ):
            mapped_data[name] = map_to_graphql_type(value, f_type)
        # Handle raw scalar values
        else:
            mapped_data[name] = value

    try:
        return gql_type(**mapped_data)
    except TypeError as e:
        raise TypeError(
            f"Failed to construct {gql_type.__name__} with data {mapped_data}: {e}"
        )
