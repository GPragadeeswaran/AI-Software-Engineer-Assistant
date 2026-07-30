from fastapi import FastAPI
from app.api.health import router as health_router
from app.core.config import settings
from contextlib import asynccontextmanager
from app.api.auth import router as auth_router
from app.db.database import create_tables
from app.api.repository import router as repository_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Application is starting...")

    create_tables()

    print("✅ Database tables are ready.")

    yield

    print("🛑 Application is shutting down...")

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    lifespan=lifespan
)

app.include_router(health_router)
app.include_router(auth_router)
app.include_router(repository_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Software Engineer Assistant 🚀"
    }