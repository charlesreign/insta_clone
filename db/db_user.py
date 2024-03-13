from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import DbUser
from routers.schemas import UserBase
from datetime import datetime


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
        timestamp=datetime.now(),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
