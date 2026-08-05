from pathlib import Path
from app.utils.repository_scanner import RepositoryScanner
from app.utils.repository_constants import (
    IMPORTANT_FILES,
    IGNORE_FOLDERS,DATABASE_KEYWORDS
)

class DatabaseService:

    def detect_database(self, repository_path: str):

        for file in RepositoryScanner.scan_files(repository_path):

            if (
                    file.name.lower() not in IMPORTANT_FILES and file.suffix.lower() != ".csproj"
                ):
                    continue

            try:
                content = file.read_text(
                    encoding="utf-8"
                ).lower()

            except Exception:
                continue

            for database, keywords in DATABASE_KEYWORDS.items():

                for keyword in keywords:

                    if keyword in content:
                        return database

        return "Unknown"