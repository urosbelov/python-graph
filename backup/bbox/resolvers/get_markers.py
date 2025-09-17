from typing import List
from app.core.logger import logger
import strawberry

from app.context import Context
from app.schema.bbox.types import Marker
from app.schema.shared.geospatial import BBoxInput


def get_markers(self, input: BBoxInput, info: strawberry.Info[Context]) -> List[Marker]:
    logger.debug(f"Fetching markers with bbox: {input}")
    # Query from Workspaces
    # Query from POIs
    # Make markers from both queries
    pass
