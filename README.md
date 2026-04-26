# Aged Care API — Notifications & Community Module

## Stack
- **FastAPI** — web framework
- **SQLAlchemy 2.0** — ORM (mapped_column style)
- **Alembic** — database migrations
- **SQLite** — dev database (`test.db`)
- **Pydantic v2** — request/response validation

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

- Swagger docs: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## Migrations

```bash
# After changing a model:
alembic revision --autogenerate -m "describe_change"
alembic upgrade head

# Rollback one step:
alembic downgrade -1
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/notifications` | Create a notification |
| `GET` | `/api/notifications` | List notifications |
| `PATCH` | `/api/notifications/{id}/read` | Mark notification read |
| `POST` | `/api/posts` | Create a post |
| `GET` | `/api/posts` | List posts |
| `GET` | `/api/posts/{post_id}` | Get single post |
| `POST` | `/api/posts/{post_id}/comments` | Add comment to post |
| `GET` | `/api/posts/{post_id}/comments` | List comments on post |

## Architecture

```
routes      → HTTP in/out, status codes, DI (db + user)
services    → business logic, validation, orchestration, raises HTTPException
crud        → raw DB queries only, returns ORM objects, no HTTP/business logic
models      → SQLAlchemy table definitions
schemas     → Pydantic request/response shapes
api/deps.py → shared get_db + get_current_user_id (mock until auth is ready)
db/base.py  → single DeclarativeBase imported by all models + Alembic
```

## Auth (Mock)
`get_current_user_id()` in `app/api/deps.py` returns a random UUID.
Replace with JWT decoding once the auth module is integrated.

## Project Structure

```
app/
├── main.py
├── api/
│   ├── deps.py               # shared dependencies
│   ├── notifications/
│   │   ├── crud.py
│   │   └── routes.py
│   ├── posts/
│   │   ├── crud.py
│   │   └── routes.py
│   └── comments/
│       ├── crud.py
│       └── routes.py
├── core/
│   └── config.py
├── db/
│   ├── base.py               # DeclarativeBase (Alembic source)
│   └── database.py           # engine + SessionLocal
├── models/
│   ├── notification.py
│   ├── post.py
│   └── comment.py
├── schemas/
│   ├── notification.py
│   ├── post.py
│   └── comment.py
└── services/
    ├── notification_service.py
    ├── post_service.py
    └── comment_service.py
alembic/
└── versions/
```
