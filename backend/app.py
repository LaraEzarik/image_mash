from ariadne import QueryType, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from fastapi import FastAPI

typedefs = load_schema_from_path('schema/')

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello, world!"

schema = make_executable_schema(typedefs, query)

app = FastAPI()

app.mount('/graphql', GraphQL(schema, debug=True))