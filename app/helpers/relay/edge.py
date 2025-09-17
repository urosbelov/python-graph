from strawberry import relay
from typing import List, Type, Iterable
from app.helpers.mappers import map_to_dataclass
from app.helpers.relay.encoder import encode_cursor


def compose_edges(
    cls: Type,  # Target dataclass
    items: Iterable[dict],
) -> List[relay.Edge]:
    """
    Converts list of dict items to Relay edges with encoded cursors.
    """
    edges = [
        relay.Edge(
            node=map_to_dataclass(cls, item),
            cursor=encode_cursor(item["id"]),
        )
        for item in items
    ]
    return edges
