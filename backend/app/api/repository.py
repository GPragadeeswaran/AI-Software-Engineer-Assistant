from fastapi import APIRouter
from app.schemas.repository_schema import RepositoryRequest
from app.services.github_service import GitHubService
from app.services.ai_service import AIService
from app.services.chunk_service import ChunkService
from app.services.metadata_service import MetadataService
from app.services.architecture_service import ArchitectureService
from app.services.authentication_service import AuthenticationService
from app.services.database_service import DatabaseService
from app.services.api_service import APIService
from app.services.testing_service import TestingService
from app.services.docker_service import DockerService
from app.services.cicd_service import CICDService
from app.services.license_service import LicenseService


router = APIRouter(
    prefix="/repository",
    tags=["Repository"]
)

github_service = GitHubService()
ai_service = AIService()
chunk_service = ChunkService()
metadata_service = MetadataService()
architecture_service = ArchitectureService()
authentication_service = AuthenticationService()
database_service = DatabaseService()
api_service = APIService()
testing_service = TestingService()
docker_service = DockerService()
cicd_service = CICDService()
license_service = LicenseService()


@router.post("/analyze")
def analyze_repository(request: RepositoryRequest):

    repository_path = github_service.clone_repository(
    str(request.repository_url)
    )

    files = github_service.read_repository(repository_path)
    metadata = metadata_service.extract_metadata(repository_path)
    architecture = architecture_service.detect_architecture(repository_path)
    database = database_service.detect_database(repository_path)
    api_framework = api_service.detect_api_framework(repository_path)
    authentication = authentication_service.detect_authentication(repository_path)
    testing_framework = testing_service.detect_testing_framework(repository_path)
    docker = docker_service.detect_docker(repository_path)
    cicd = cicd_service.detect_cicd(repository_path)
    license_type = license_service.detect_license(repository_path)
    
    return {
    "metadata": metadata,
    "architecture": architecture,
    "database": database,
    "api_framework": api_framework,
    "authentication": authentication,
    "testing_framework": testing_framework,
    "docker": docker,
    "cicd": cicd,
    "license": license_type
    }

    
   # chunks = chunk_service.create_chunks(files)

    all_analysis = []

    #for chunk in chunks:
      #  prompt = ai_service.prepare_chunk(chunk)
       # analysis = ai_service.analyze_chunk(prompt)
       # all_analysis.append(analysis)

    #final_analysis = ai_service.merge_analysis(all_analysis)
  
   

