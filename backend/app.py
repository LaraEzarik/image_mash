from ariadne import QueryType, make_executable_schema, load_schema_from_path, upload_scalar
from ariadne.asgi import GraphQL
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from resolvers.upload import upload_mutation
from resolvers.vote import vote_mutation
from resolvers.images import query


typedefs = load_schema_from_path('schema/')

schema = make_executable_schema(typedefs, query, upload_mutation, vote_mutation, upload_scalar)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000/graphql",
    "http://localhost:5173",
    "http://127.0.0.1",
    "http://127.0.0.1:3000/graphql"
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/graphql', GraphQL(schema, debug=True))
app.mount("/static", StaticFiles(directory="static"), name="static")