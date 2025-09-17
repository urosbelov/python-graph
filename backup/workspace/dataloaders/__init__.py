from strawberry.dataloader import DataLoader
from .get_workspaces_batch import initiate as workspace_initiate
from .get_categories_batch import initiate as categories_initiate
from .get_amenities_batch import initiate as amenities_initiate
from .get_features_batch import initiate as features_initiate

workspace_loader = DataLoader(load_fn=workspace_initiate)
workspace_categories_loader = DataLoader(load_fn=categories_initiate)
workspace_amenities_loader = DataLoader(load_fn=amenities_initiate)
workspace_features_loader = DataLoader(load_fn=features_initiate)
