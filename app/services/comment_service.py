"""
Comment service — business logic only.

Responsibilities:
- Verify the parent post exists before adding a comment
- Enforce ownership rules on delete
- Delegate persistence to the CRUD layer
- Raise HTTPException for domain-level errors
"""

from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.api.comments import crud as comment_crud
from app.api.posts import crud as post_crud
from app.schemas.comment import CommentCreate, CommentResponse


def create_comment(
    db: Session, post_id: UUID, payload: CommentCreate, uid: UUID
) -> CommentResponse:
    post = post_crud.get_post_by_id(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    comment = comment_crud.create_comment(db=db, comment=payload, post_id=post_id, uid=uid)
    return CommentResponse.model_validate(comment)


def list_comments(db: Session, post_id: UUID) -> list[CommentResponse]:
    post = post_crud.get_post_by_id(db=db, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    comments = comment_crud.get_comments_by_post(db=db, post_id=post_id)
    return [CommentResponse.model_validate(c) for c in comments]
