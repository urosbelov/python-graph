from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class UserIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Extract x-user-id header (default: None if missing)
        user_id = request.headers.get("x-user-id")
        request.scope["user_id"] = user_id

        response = await call_next(request)
        return response
