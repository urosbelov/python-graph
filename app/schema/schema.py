import strawberry
from app.schema.queries.workspace_queries import WorkspaceQuery
from app.schema.mutations.post_mutations import PostMutation

# Dynamically combine all queries
Query = type("Query", (WorkspaceQuery,), {})
Mutation = type("Mutation", (PostMutation,), {})

schema = strawberry.Schema(query=Query, mutation=Mutation)
