import strawberry

from app.context import Context
from app.helpers.mapper import map_to_graphql_type
from app.helpers.sdk.call import safe_sdk_call
from app.schema.user.inputs import CreateUserInput
from app.schema.user.responses import CreateUserResponse


@strawberry.type
class UserMutations:
    @strawberry.mutation
    async def create_user(
        self, input: CreateUserInput, info: strawberry.Info[Context]
    ) -> CreateUserResponse:
        input_data = input.__dict__
        response = await safe_sdk_call(
            info.context.users_api.create_user,
            input_data,
            context=info.context,
        )
        return map_to_graphql_type(response, CreateUserResponse)
