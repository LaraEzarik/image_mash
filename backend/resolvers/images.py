import random

from ariadne import QueryType
from sqlalchemy.orm import sessionmaker

from database import engine
from models import Upload

Session = sessionmaker(bind=engine)
session = Session()

query = QueryType()

@query.field("randomImages")
def resolve_randomImages(_, info):
    # Query for all users
    uploads = session.query(Upload).all()

    value = random.sample(uploads, 2)
    images = [val.image for val in value]
    return images