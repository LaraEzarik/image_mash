from ariadne import QueryType, make_executable_schema, load_schema_from_path, upload_scalar
from ariadne.asgi import GraphQL
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from resolvers.upload import upload_mutation


typedefs = load_schema_from_path('schema/')

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello, world!"

schema = make_executable_schema(typedefs, query, upload_mutation, upload_scalar)

app = FastAPI()

app.mount('/graphql', GraphQL(schema, debug=True))
app.mount("/static", StaticFiles(directory="static"), name="static")