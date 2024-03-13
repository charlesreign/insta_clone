from typing import List
from pydantic import BaseModel
from fastapi import status
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True


# for post display
class User(BaseModel):
    username: str

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class PostDisplay:
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User

    class Config:
        from_attributes = True
