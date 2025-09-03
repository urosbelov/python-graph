from typing import Iterable, Optional
import strawberry
from strawberry import relay
from app.context import Context
from app.schema.workspace.service import map_to_dataclass


@strawberry.type(name="Workspace")
class WorkspaceNode(relay.Node):
    id: relay.NodeID[int]
    name: str
    google_place_id: Optional[str] = None

    # ---- Node resolver ----
    @classmethod
    async def resolve_nodes(
        cls,
        *,
        info: strawberry.Info[Context],
        node_ids: Iterable[str],
        required: bool = False,
    ):
        micro_ids = [int(nid) for nid in node_ids]
        loader = info.context.workspace_loader
        workspaces = await loader.load_many(micro_ids)
        print(f"Resolved workspaces: {workspaces}")
        return [map_to_dataclass(WorkspaceNode, ws) for ws in workspaces]
