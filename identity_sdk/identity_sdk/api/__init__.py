# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from identity_sdk.api.auth_api import AuthApi
    from identity_sdk.api.flow_api import FlowApi
    from identity_sdk.api.identifiers_api import IdentifiersApi
    from identity_sdk.api.sessions_api import SessionsApi
    from identity_sdk.api.users_api import UsersApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from identity_sdk.api.auth_api import AuthApi
from identity_sdk.api.flow_api import FlowApi
from identity_sdk.api.identifiers_api import IdentifiersApi
from identity_sdk.api.sessions_api import SessionsApi
from identity_sdk.api.users_api import UsersApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
