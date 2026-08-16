from pathlib import Path


class SourceDetector:

    SOURCE_EXTENSIONS = {
        ".py",
        ".js",
        ".ts",
        ".java",
        ".cs"
    }

    IGNORED_DIRECTORIES = {
        ".git",
        "__pycache__",
        "node_modules",
        ".venv",
        "venv",
        "env",
        "site-packages",
        "vendor",
        "vendors",
        "third_party",
        "third-party",
        "build",
        "dist"
    }

    @staticmethod
    def is_source_file(file: Path) -> bool:

        if file.suffix.lower() not in SourceDetector.SOURCE_EXTENSIONS:
            return False

        if any(
            directory.lower() in {
                part.lower() for part in file.parts
            }
            for directory in SourceDetector.IGNORED_DIRECTORIES
        ):
            return False

        return True