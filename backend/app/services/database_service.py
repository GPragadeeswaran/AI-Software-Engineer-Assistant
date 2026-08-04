from pathlib import Path
from app.utils.repository_constants import (
    IMPORTANT_FILES,
    IGNORE_FOLDERS
)

class DatabaseService:

    def detect_database(self, repository_path: str):

        database_keywords = {
            "PostgreSQL": [
                "psycopg2",
                "postgresql://",
                "postgresql+psycopg2"
            ],
            "MySQL": [
                "pymysql",
                "mysql://",
                "mysql"
            ],
            "SQLite": [
                "sqlite3",
                ".db"
            ],
            "MongoDB": [
                "pymongo",
                "mongodb://",
                "mongo"
            ],
            "Redis": [
                "import redis",
                "redis://",
                "redis.Redis("
            ]
        }

        for file in Path(repository_path).rglob("*"):

            if any(folder in file.parts for folder in IGNORE_FOLDERS):
                continue

            if not file.is_file():
                continue

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

            for database, keywords in database_keywords.items():

                for keyword in keywords:

                    if keyword in content:
                        return database

        return "Unknown"