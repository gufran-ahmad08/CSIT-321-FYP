# Centralised metadata — imported by Alembic env.py so it can autogenerate migrations.
# Every model must import Base from here (NOT from database.py).

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
