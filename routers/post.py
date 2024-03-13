from enum import Enum
import random
import shutil
import string
from typing import Dict, List, Optional
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Response,
    File,
    UploadFile,
)
from pydantic import BaseModel
from sqlalchemy.orm.session import Session

from db.database import get_db
from routers.schemas import PostBase, PostDisplay
from db import db_post

router = APIRouter(prefix="/post", tags=["Post"])

image_url_types = ["absolute", "relative"]


@router.post("/create", response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Parameter image_url_type can only take va;ues of 'absolute' or 'relative'",
        )
    return db_post.create_post(db, request)
