import uuid
from datetime import datetime, timezone
from sqlalchemy import String, UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Notification(Base):
    __tablename__ = "notifications"

    # Mapped[uuid.UUID] tells Python this is a UUID object
    # UUID(as_uuid=True) tells the DB how to store it
    notification_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4
    )
    
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        nullable=False
    )
    
    title: Mapped[str] = mapped_column(String, nullable=False)
    message: Mapped[str] = mapped_column(String, nullable=False)
    is_read: Mapped[bool] = mapped_column(default=False)
    
    # Use timezone-aware UTC for modern apps
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
