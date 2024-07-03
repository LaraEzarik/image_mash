from ariadne import MutationType
from sqlalchemy.orm import Session

from models import Upload
from database import engine

vote_mutation = MutationType()

@vote_mutation.field('eloVote')
async def resolve_upload_file(_, info, upvote, downvote):
    with Session(engine) as session:
        winner = session.query(Upload).filter(Upload.id == upvote).first()
        winner.upvotes += 1
        loser = session.query(Upload).filter(Upload.id == downvote).first()
        loser.downvotes += 1
        
        ea: float = 1 / (1 + 10 ** ((loser.elo - winner.elo) / 400))
        eb: float = 1 / (1 + 10 ** ((winner.elo - loser.elo) / 400))

        winner.elo = winner.elo + (32 * (1 - ea))
        loser.elo = loser.elo + (32 * (0 - eb))
        
        session.commit()
    return True    