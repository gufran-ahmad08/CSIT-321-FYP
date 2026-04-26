from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    post_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True