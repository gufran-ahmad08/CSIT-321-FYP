"""
Shared FastAPI dependencies.

- get_db      : yields a DB session, always closed after request.
- get_current_user_id : mocked until real JWT auth is wired in.
"""

import uuid
from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user_id() -> UUID:
    """Mock: returns a random UUID as the logged-in user.
    Replace with real JWT decoding when auth module is ready.
    """
    return uuid.uuid4()
