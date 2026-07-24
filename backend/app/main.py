from fastapi import FastAPI
from app.api.health import router as health_router
from app.core.config import settings
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Application is starting...")

    # Startup tasks go here

    yield

    # Shutdown tasks go here

    print("🛑 Application is shutting down...")

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    lifespan=lifespan
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to AI Software Engineer Assistant 🚀"
    }