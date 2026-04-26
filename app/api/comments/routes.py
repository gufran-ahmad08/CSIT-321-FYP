from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user_id, get_db
from app.schemas.comment import CommentCreate, CommentResponse
from app.services import comment_service

router = APIRouter(prefix="/posts/{post_id}/comments", tags=["comments"])


@router.post("", response_model=CommentResponse, status_code=status.HTTP_201_CREATED)
def create_comment_endpoint(
    post_id: UUID,
    payload: CommentCreate,
    db: Session = Depends(get_db),
    uid: UUID = Depends(get_current_user_id),
):
    return comment_service.create_comment(db=db, post_id=post_id, payload=payload, uid=uid)


@router.get("", response_model=list[CommentResponse])
def list_comments_endpoint(
    post_id: UUID,
    db: Session = Depends(get_db),
):
    return comment_service.list_comments(db=db, post_id=post_id)
