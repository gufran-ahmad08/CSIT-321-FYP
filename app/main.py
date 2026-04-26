from fastapi import FastAPI

from app.api.comments.routes import router as comments_router
from app.api.notifications.routes import router as notifications_router
from app.api.posts.routes import router as posts_router

app = FastAPI(title="Aged Care API", version="0.1.0")

app.include_router(posts_router, prefix="/api")
app.include_router(comments_router, prefix="/api")
app.include_router(notifications_router, prefix="/api")