from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.comment import Comment
from app.schemas.comment import CommentCreate


def create_comment(
    db: Session, comment: CommentCreate, post_id: UUID, uid: UUID
) -> Comment:
    db_comment = Comment(post_id=post_id, uid=uid, content=comment.content)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comments_by_post(db: Session, post_id: UUID) -> list[Comment]:
    query = select(Comment).where(Comment.post_id == post_id)
    return db.execute(query).scalars().all()
