from strawberry.dataloader import DataLoader
from .service import get_workspaces_batch

workspace_loader = DataLoader(load_fn=get_workspaces_batch)
