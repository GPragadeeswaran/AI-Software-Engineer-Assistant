# Download and read the repository.

from pathlib import Path
from uuid import uuid4

from git import Repo


class GitHubService:

    def clone_repository(self, repository_url: str) -> str:

        repositories_dir = Path("repositories")
        repositories_dir.mkdir(exist_ok=True)

        repository_folder = repositories_dir / str(uuid4())

        Repo.clone_from(
            repository_url,
            repository_folder
        )

        return str(repository_folder)

    def read_repository(self, repository_path: str):

        repository = Path(repository_path)

        ALLOWED_EXTENSIONS = {
            ".py",
            ".md",
            ".txt",
            ".json",
            ".yaml",
            ".yml",
            ".toml",
            ".ini",
            ".cfg",
            ".html",
            ".css",
            ".js",
            ".ts",
            ".sql"
        }

        IGNORED_DIRECTORIES = {
            ".git",
            ".github",
            "__pycache__",
            ".pytest_cache",
            ".venv",
            "venv",
            "node_modules",
            "dist",
            "build"
        }

        ALLOWED_FILES_WITHOUT_EXTENSION = {
            "README",
            "LICENSE",
            "Dockerfile",
            "Makefile"
        }

        MAX_FILE_SIZE = 1 * 1024 * 1024

        files = []

        for file in repository.rglob("*"):

            if not file.is_file():
                continue

            if any(part in IGNORED_DIRECTORIES for part in file.parts):
                continue

            if (
              file.suffix.lower() not in ALLOWED_EXTENSIONS and file.name not in ALLOWED_FILES_WITHOUT_EXTENSION ):  
                continue

            if file.stat().st_size > MAX_FILE_SIZE:
                continue

            try:
                content = file.read_text(encoding="utf-8")

                files.append({
                    "file_name": str(file.relative_to(repository)),
                    "content": content
                })

            except UnicodeDecodeError:
                continue

        return files