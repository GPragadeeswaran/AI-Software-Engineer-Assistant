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
from app.services.summary_service import SummaryService
from app.services.repository_score_service import RepositoryScoreService
from app.services.suggestion_service import SuggestionService
from app.services.code_quality_service import CodeQualityService
from app.services.dependency_service import DependencyService
from app.services.security_service import SecurityService
from app.services.repo_advisor import RepoAdvisor
from app.services.repository_insight_service import RepositoryInsightService


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

summary_service = SummaryService()
repository_score_service = RepositoryScoreService()
suggestion_service = SuggestionService()
code_quality_service = CodeQualityService()
dependency_service = DependencyService()
security_service = SecurityService()
advisor = RepoAdvisor()
repository_insight_service = RepositoryInsightService()


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
    code_quality = code_quality_service.detect_code_quality(repository_path)
    dependencies = dependency_service.detect_dependencies(repository_path)
    security = security_service.detect_security_issues(repository_path)
    
   

    # Generate AI Summary
    summary = summary_service.generate_summary(
        metadata,
        architecture,
        api_framework,
        authentication,
        testing_framework,
        cicd,
        license_type
    )

    repository_score = repository_score_service.calculate_health_score(
    metadata,
    architecture,
    database,
    api_framework,
    authentication,
    testing_framework,
    docker,
    cicd,
    license_type
    )

    suggestions = suggestion_service.generate_suggestions(
    metadata,
    architecture,
    database,
    api_framework,
    authentication,
    testing_framework,
    docker,
    cicd,
    license_type
    )

    analysis_result = {
    "metadata": metadata,
    "architecture": architecture,
    "database": database,
    "api_framework": api_framework,
    "authentication": authentication,
    "testing_framework": testing_framework,
    "docker": docker,
    "cicd": cicd,
    "license": license_type,
    "code_quality": code_quality,
    "dependencies": dependencies,
    "security": security
     }

    #AI advisor

    recommendations = advisor.generate_recommendations(
    docker=docker,
    database=database,
    dependencies=dependencies,
    security=security,
    code_quality=code_quality
    )

    insights = repository_insight_service.generate_insights(analysis_result)

    return {
        "metadata": metadata,
        "architecture": architecture,
        "database": database,
        "api_framework": api_framework,
        "authentication": authentication,
        "testing_framework": testing_framework,
        "docker": docker,
        "cicd": cicd,
        "license": license_type,
        "summary": summary,
        "repository_score": repository_score,
        "suggestions": suggestions,
        "code_quality": code_quality,
        "dependencies": dependencies,
        "security": security,
        "recommendations": recommendations,
        "insights": insights
    }

    # chunks = chunk_service.create_chunks(files)

    # all_analysis = []

    # for chunk in chunks:
    #     prompt = ai_service.prepare_chunk(chunk)
    #     analysis = ai_service.analyze_chunk(prompt)
    #     all_analysis.append(analysis)

    # final_analysis = ai_service.merge_analysis(all_analysis)