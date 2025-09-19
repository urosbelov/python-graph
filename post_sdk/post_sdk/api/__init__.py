# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from post_sdk.api.post_media_api import PostMediaApi
    from post_sdk.api.posts_api import PostsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from post_sdk.api.post_media_api import PostMediaApi
from post_sdk.api.posts_api import PostsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
