from ariadne import MutationType
import aiofiles

from models import Upload

upload_mutation = MutationType()

@upload_mutation.field('upload')
async def resolve_upload_file(_, info, image):
    destination_path = f'static/{image.filename}'
    async with aiofiles.open(destination_path, 'wb') as out_file:
        content = await image.read()  # async read
        await out_file.write(content)
    Upload.create(image=image.filename)
    return True