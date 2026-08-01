from pydantic import BaseModel, HttpUrl


class RepositoryRequest(BaseModel):
    repository_url: HttpUrl
    branch: str = "main"
    analysis_type: str = "full"