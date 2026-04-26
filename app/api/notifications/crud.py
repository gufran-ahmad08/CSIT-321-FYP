from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.notification import Notification
from app.schemas.notification import NotificationCreate


def create_notification(db: Session, notification: NotificationCreate, uid: UUID) -> Notification:
    db_notification = Notification(
        uid=uid,
        title=notification.title,
        message=notification.message,
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


def get_notifications(db: Session, skip: int = 0, limit: int = 100) -> list[Notification]:
    query = select(Notification).offset(skip).limit(limit)
    return db.execute(query).scalars().all()


def get_notification_by_id(db: Session, notification_id: UUID) -> Notification | None:
    return db.get(Notification, notification_id)


def mark_notification_read(db: Session, notification: Notification) -> Notification:
    notification.is_read = True
    db.commit()
    db.refresh(notification)
    return notification
