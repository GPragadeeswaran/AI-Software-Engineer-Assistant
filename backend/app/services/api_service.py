from pathlib import Path
from app.utils.repository_constants import (
    IMPORTANT_FILES,
    IGNORE_FOLDERS
)

class APIService:

    def detect_api(self, repository_path: str):
        api_keywords = {

            "FastAPI": [
                "fastapi",
                "@app.get",
                "@app.post",
                "@app.put",
                "@app.delete",
                "APIRouter"
            ],

            "Flask": [
                "flask",
                "@app.route",
                "Blueprint"
            ],

            "Django": [
                "django",
                "urlpatterns",
                "path(",
                "re_path("
            ],

            "Express.js": [
                "express",
                "app.get(",
                "app.post(",
                "router.get(",
                "router.post("
            ],

            "Spring Boot": [
                "@RestController",
                "@GetMapping",
                "@PostMapping",
                "@RequestMapping"
            ],

            "ASP.NET Core": [
                "[ApiController]",
                "[HttpGet]",
                "[HttpPost]",
                "MapGet(",
                "MapPost("
            ]
        }

        for file in Path(repository_path).rglob("*"):

            if any(folder in file.parts for folder in IGNORE_FOLDERS):
                continue

            if not file.is_file():
                continue

            if (
                file.name.lower() not in IMPORTANT_FILES
                and file.suffix.lower() != ".csproj"
            ):
                continue

            try:
                content = file.read_text(
                    encoding="utf-8"
                ).lower()

            except Exception:
                continue

            for framework, keywords in api_keywords.items():

                for keyword in keywords:

                    if keyword.lower() in content:
                        return framework

        return "Unknown"