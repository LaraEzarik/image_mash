import random

from ariadne import QueryType
from sqlalchemy.orm import sessionmaker

from database import engine
from models import Upload
from config import URL, STATIC

Session = sessionmaker(bind=engine)
session = Session()

query = QueryType()

@query.field("compareImages")
def resolve_compareImages(_, info):
    # Query for all users
    uploads = session.query(Upload).all()

    images = []
    sample = random.sample(uploads, 2)
    for value in sample:
        images.append({'id': value.id,
                       'image': f'{URL}/{STATIC}/{value.image}',
                       'upvotes': value.upvotes,
                       'downvotes': value.downvotes,
                       'elo': value.elo})
    
    return images

@query.field('getAllImages')
def resolve_getAllImages(_, info):
    uploads = session.query(Upload).all()
    images = []
    for value in uploads:
        images.append({'id': value.id,
                       'image': f'{URL}/{STATIC}/{value.image}',
                       'upvotes': value.upvotes,
                       'downvotes': value.downvotes,
                       'elo': value.elo})
    return images