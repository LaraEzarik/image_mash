from ariadne import QueryType, MutationType, make_executable_schema, load_schema_from_path, upload_scalar
from ariadne.asgi import GraphQL
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import aiofiles


typedefs = load_schema_from_path('schema/')

query = QueryType()
mutation = MutationType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hello, world!"

@mutation.field('upload')
async def resolve_upload_file(_, info, image):
    destination_path = f'static/{image.filename}'
    async with aiofiles.open(destination_path, 'wb') as out_file:
        content = await image.read()  # async read
        await out_file.write(content)
    return True

schema = make_executable_schema(typedefs, query, mutation, upload_scalar)

app = FastAPI()

app.mount('/graphql', GraphQL(schema, debug=True))
app.mount("/static", StaticFiles(directory="static"), name="static")