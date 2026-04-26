from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user_id, get_db
from app.schemas.notification import NotificationCreate, NotificationResponse
from app.services import notification_service

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post("", response_model=NotificationResponse, status_code=status.HTTP_201_CREATED)
def create_notification_endpoint(
    payload: NotificationCreate,
    db: Session = Depends(get_db),
    uid: UUID = Depends(get_current_user_id),
):
    return notification_service.create_notification(db=db, payload=payload, uid=uid)


@router.get("", response_model=list[NotificationResponse])
def list_notifications_endpoint(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return notification_service.list_notifications(db=db, skip=skip, limit=limit)


@router.patch("/{notification_id}/read", response_model=NotificationResponse)
def mark_notification_read_endpoint(
    notification_id: UUID,
    db: Session = Depends(get_db),
    uid: UUID = Depends(get_current_user_id),
):
    return notification_service.mark_as_read(db=db, notification_id=notification_id, uid=uid)