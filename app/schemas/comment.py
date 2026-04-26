from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class CommentBase(BaseModel):
    content: str


class CommentCreate(CommentBase):
    pass


class CommentResponse(CommentBase):
    comment_id: UUID
    post_id: UUID
    uid: UUID
    created_at: datetime

    model_config = {"from_attributes": True}
