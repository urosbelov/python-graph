import strawberry

from app.context import Context
from app.helpers.converter.core import StrawberryConverter
from app.helpers.sdk.call import safe_sdk_call
from app.schema.user.inputs import CreateUserInput
from app.schema.user.responses import CreateUserResponse


@strawberry.type
class UserMutations:
    @strawberry.mutation
    async def create_user(
        self, input: CreateUserInput, info: strawberry.Info[Context]
    ) -> CreateUserResponse:
        converter = StrawberryConverter()
        response = await safe_sdk_call(
            info.context.users_api.create_user,
            converter.to_dict(input),
            context=info.context,
        )
        return converter.from_sdk(response, CreateUserResponse)
