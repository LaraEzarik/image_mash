from ariadne import MutationType
import aiofiles
from sqlalchemy.orm import Session

from models import Upload
from database import engine

upload_mutation = MutationType()

@upload_mutation.field('upload')
async def resolve_upload_file(_, info, image):
    print(image)
    destination_path = f'static/{image.filename}'
    async with aiofiles.open(destination_path, 'wb') as out_file:
        content = await image.read()  # async read
        await out_file.write(content)
    upload = Upload(image=image.filename)
    with Session(engine) as session:
        session.add(upload)
        session.commit()
    return True