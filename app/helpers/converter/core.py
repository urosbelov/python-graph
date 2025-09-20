from typing import Any, Type


class StrawberryConverter:
    @staticmethod
    def to_dict(obj: Any, exclude_none: bool = True) -> Any:
        """Recursively convert a Strawberry input object to a dictionary, handling nested inputs and arrays."""
        if obj is None and exclude_none:
            return None
        if hasattr(obj, "__dict__"):
            return {
                k: StrawberryConverter.to_dict(v, exclude_none)
                for k, v in obj.__dict__.items()
                if not exclude_none or v is not None
            }
        elif isinstance(obj, (list, tuple)):
            return [StrawberryConverter.to_dict(item, exclude_none) for item in obj]
        elif isinstance(obj, dict):
            return {
                k: StrawberryConverter.to_dict(v, exclude_none) for k, v in obj.items()
            }
        return obj

    @staticmethod
    def from_sdk(sdk_obj: Any, gql_type: Type[Any]) -> Any:
        from .graphql import map_to_graphql_type

        """Convert an SDK object or list of SDK objects to GraphQL type(s), handling arrays."""
        if sdk_obj is None:
            return None
        if isinstance(sdk_obj, (list, tuple)):
            return [StrawberryConverter.from_sdk(item, gql_type) for item in sdk_obj]
        return map_to_graphql_type(sdk_obj, gql_type)
