from sqlalchemy import Column, Integer, String

from database import Base

class Upload(Base):
    __tablename__ = "uploads"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, index=True)
    upvotes = Column(Integer, default=0)
    downvotes = Column(Integer, default=0)
    elo = Column(Integer, default=1200)