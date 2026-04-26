"""
Notification service — business logic only.

Responsibilities:
- Validate business rules (e.g. future: deduplicate, rate-limit)
- Delegate persistence to the CRUD layer
- Raise HTTPException for domain-level errors (not DB errors)
"""

from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.api.notifications import crud
from app.schemas.notification import NotificationCreate, NotificationResponse


def create_notification(
    db: Session, payload: NotificationCreate, uid: UUID
) -> NotificationResponse:
    notification = crud.create_notification(db=db, notification=payload, uid=uid)
    return NotificationResponse.model_validate(notification)


def list_notifications(
    db: Session, skip: int = 0, limit: int = 100
) -> list[NotificationResponse]:
    notifications = crud.get_notifications(db=db, skip=skip, limit=limit)
    return [NotificationResponse.model_validate(n) for n in notifications]


def mark_as_read(db: Session, notification_id: UUID, uid: UUID) -> NotificationResponse:
    notification = crud.get_notification_by_id(db=db, notification_id=notification_id)
    if not notification:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    if notification.uid != uid:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not your notification")
    updated = crud.mark_notification_read(db=db, notification=notification)
    return NotificationResponse.model_validate(updated)
