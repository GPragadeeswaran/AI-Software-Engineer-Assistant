from pathlib import Path


class RepositoryFilter:

    EXCLUDED_DIRECTORIES = {
        ".git",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        "venv",
        ".venv",
        "env",
        "node_modules",
        "dist",
        "build",
        "docs",
        "examples",
        "example",
        "samples",
        "sample",
        "demo",
    }

    @staticmethod
    def is_valid_file(file_path: Path) -> bool:

        for part in file_path.parts:
            if part.lower() in RepositoryFilter.EXCLUDED_DIRECTORIES:
                return False

        return file_path.is_file()