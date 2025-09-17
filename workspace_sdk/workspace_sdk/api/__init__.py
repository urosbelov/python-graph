# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from workspace_sdk.api.amenities_api import AmenitiesApi
    from workspace_sdk.api.categories_api import CategoriesApi
    from workspace_sdk.api.v1_api import V1Api
    from workspace_sdk.api.workspaces_api import WorkspacesApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from workspace_sdk.api.amenities_api import AmenitiesApi
from workspace_sdk.api.categories_api import CategoriesApi
from workspace_sdk.api.v1_api import V1Api
from workspace_sdk.api.workspaces_api import WorkspacesApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
