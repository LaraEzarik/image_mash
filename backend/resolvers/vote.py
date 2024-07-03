from ariadne import MutationType
from sqlalchemy.orm import Session

from models import Upload
from database import engine

vote_mutation = MutationType()

@vote_mutation.field('eloVote')
async def resolve_upload_file(_, info, upvote, downvote):
    with Session(engine) as session:
        upload = session.query(Upload).filter(Upload.id == upvote).first()
        upload.upvotes += 1
        upload = session.query(Upload).filter(Upload.id == downvote).first()
        upload.downvotes += 1
        session.commit()
    return True    