from graphql import GraphQLError
from workspace_sdk.workspace_sdk.exceptions import ApiException


class GraphqlErrorMiddleware:
    async def resolve(self, next_, root, info, **kwargs):
        try:
            return await next_(root, info, **kwargs)
        except GraphQLError:
            # Already a proper GraphQLError, just re-raise
            raise
        except ApiException as e:
            # Convert SDK ApiException to GraphQLError
            try:
                body = getattr(e, "body", None)
                errors = body.get("errors") if body else None
                message = errors[0]["message"] if errors else str(e)
                code = errors[0]["code"] if errors else getattr(e, "status", "ERROR")
                field = errors[0]["field"] if errors else None
            except Exception:
                message = str(e)
                code = getattr(e, "status", "ERROR")
                field = None

            raise GraphQLError(message, extensions={"code": code, "field": field})
        except Exception as e:
            # Catch-all for unexpected errors
            raise GraphQLError(str(e), extensions={"code": "INTERNAL_SERVER_ERROR"})
