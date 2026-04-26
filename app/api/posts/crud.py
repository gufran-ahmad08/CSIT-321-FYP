from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.post import Post
from app.schemas.post import PostCreate


def create_post(db: Session, post: PostCreate, uid: UUID) -> Post:
    db_post = Post(uid=uid, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session, skip: int = 0, limit: int = 100) -> list[Post]:
    query = select(Post).offset(skip).limit(limit)
    return db.execute(query).scalars().all()


def get_post_by_id(db: Session, post_id: UUID) -> Post | None:
    return db.get(Post, post_id)
