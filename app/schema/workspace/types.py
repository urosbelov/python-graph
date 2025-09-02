import strawberry
from strawberry import relay


# class WorkspaceNode(Node):
#     def to_global_id(node_id: int) -> str:
#         return SnowflakeGenerator.encode_base62(node_id)

#     @staticmethod
#     def from_global_id(global_id: str) -> int:
#         return SnowflakeGenerator.decode_base62(global_id)


@strawberry.type
class Workspace:
    id: relay.NodeID[int]
    name: str
    google_place_id: str
