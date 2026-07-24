from fastapi import APIRouter

router = APIRouter(
    prefix="/health", 
    tags=["Health"]
)


@router.get("/")
def health_check():
    return {
        "status": "healthy",
        "message": "AI Software Engineer Assistant is running successfully."
    }