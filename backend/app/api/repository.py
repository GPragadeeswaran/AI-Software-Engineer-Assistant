from fastapi import APIRouter
from app.schemas.repository_schema import RepositoryRequest
from app.services.github_service import GitHubService
from app.services.ai_service import AIService
from app.services.chunk_service import ChunkService

router = APIRouter(
    prefix="/repository",
    tags=["Repository"]
)

github_service = GitHubService()
ai_service = AIService()
chunk_service = ChunkService()

@router.post("/analyze")
def analyze_repository(request: RepositoryRequest):

    repository_path = github_service.clone_repository(
    str(request.repository_url)
    )

    files = github_service.read_repository(repository_path)
    chunks = chunk_service.create_chunks(files)

    all_analysis = []

    for chunk in chunks:
        prompt = ai_service.prepare_chunk(chunk)
        analysis = ai_service.analyze_chunk(prompt)
        all_analysis.append(analysis)

    final_analysis = ai_service.merge_analysis(all_analysis)
  
    return {
    "message": "Repository analyzed successfully",
    "repository_path": repository_path,
    "total_files": len(files),
    "total_chunks": len(chunks),
    "analysis": final_analysis
    }


