from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


class Image(Base):
    __tablename__ = "image"

    image_id = Column(Integer, primary_key=True, index=True) 
    base_64 = Column(String)
    user_id = Column(ForeignKey('user'))
