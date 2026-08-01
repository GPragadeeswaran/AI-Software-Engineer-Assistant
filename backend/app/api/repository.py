from fastapi import APIRouter
from app.schemas.repository_schema import RepositoryRequest
from app.services.github_service import GitHubService
from app.services.ai_service import AIService

router = APIRouter(
    prefix="/repository",
    tags=["Repository"]
)

github_service = GitHubService()
ai_service = AIService()

@router.post("/analyze")
def analyze_repository(request: RepositoryRequest):

    repository_path = github_service.clone_repository(
    str(request.repository_url)
    )

    files = github_service.read_repository(repository_path)
    prompt = ai_service.prepare_repository(files)
    analysis = ai_service.analyze_repository(prompt)

    return {
    "message": "Repository analyzed successfully",
    "repository_path": repository_path,
    "total_files": len(files),
    "analysis": analysis,
    }