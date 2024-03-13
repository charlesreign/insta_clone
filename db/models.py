from db.database import Base
from sqlalchemy import Column, DateTime
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbUser(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    timestamp = Column(DateTime)
    items = relationship("DbPost", back_populates="user")


class DbPost(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    image_url_type = Column(String)
    caption = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey("User.id"))
    user = relationship("DbUser", back_populates="items")
