from enum import Enum
import random
import shutil
import string
from typing import Dict, List, Optional
from fastapi import APIRouter, Depends, status, Response, File, UploadFile
from pydantic import BaseModel
from sqlalchemy.orm.session import Session

from db.database import get_db
from routers.schemas import UserBase, UserDisplay
from db import db_user

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/create", response_model=UserDisplay)
def create(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)
