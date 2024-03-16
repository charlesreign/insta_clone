from fastapi import APIRouter, Depends, status, Response, File, UploadFile
from sqlalchemy.orm.session import Session

from auth.oauth2 import get_current_user
from db.database import get_db
from routers.schemas import CommentBase, UserAuth
from db import db_comment

router = APIRouter(prefix="/comment", tags=["Comment"])


@router.post("/create")
def create(
    request: CommentBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    return db_comment.create_comment(db, request)


@router.get("/all/{post_id}")
def comments(post_id: int, db: Session = Depends(get_db)):
    return db_comment.get_all_comments(db, post_id)
