"""
Post service — business logic only.

Responsibilities:
- Enforce business rules (e.g. content length, future: spam detection)
- Orchestrate side-effects (e.g. future: fan-out notifications on new post)
- Delegate persistence to the CRUD layer
- Raise HTTPException for domain-level errors
"""

from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.api.posts import crud
from app.schemas.post import PostCreate, PostResponse


def create_post(db: Session, payload: PostCreate, uid: UUID) -> PostResponse:
    post = crud.create_post(db=db, post=payload, uid=uid)
    return PostResponse.model_validate(post)


def list_posts(db: Session, skip: int = 0, limit: int = 100) -> list[PostResponse]:
    posts = crud.get_posts(db=db, skip=skip, limit=limit)
    return [PostResponse.model_validate(p) for p in posts]


def get_post(db: Session, post_id: UUID) -> PostResponse:
    post = crud.get_post_by_id(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return PostResponse.model_validate(post)
