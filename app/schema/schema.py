import strawberry

from app.schema.workspace.resolvers import WorkspaceQuery, WorkspaceMutation


# Dynamically combine queries and mutations
Query = type("Query", (WorkspaceQuery,), {})
Mutation = type("Mutation", (WorkspaceMutation,), {})

schema = strawberry.Schema(query=Query, mutation=Mutation)
