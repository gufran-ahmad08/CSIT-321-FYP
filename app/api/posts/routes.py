from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user_id, get_db
from app.schemas.post import PostCreate, PostResponse
from app.services import post_service

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post_endpoint(
    payload: PostCreate,
    db: Session = Depends(get_db),
    uid: UUID = Depends(get_current_user_id),
):
    return post_service.create_post(db=db, payload=payload, uid=uid)


@router.get("", response_model=list[PostResponse])
def list_posts_endpoint(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return post_service.list_posts(db=db, skip=skip, limit=limit)


@router.get("/{post_id}", response_model=PostResponse)
def get_post_endpoint(
    post_id: UUID,
    db: Session = Depends(get_db),
):
    return post_service.get_post(db=db, post_id=post_id)