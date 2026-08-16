from pathlib import Path

from app.utils.repository_filter import RepositoryFilter
from app.utils.repository_scanner import RepositoryScanner


class DependencyService:

    DEPENDENCY_FILES = {
        # Python
        "requirements.txt",
        "pyproject.toml",
        "setup.py",
        "setup.cfg",
        "pipfile",

        # JavaScript
        "package.json",
        "package-lock.json",

        # Java
        "pom.xml",
        "build.gradle",

        # Go
        "go.mod",

        # Rust
        "cargo.toml",
    }

    def detect_dependencies(self, repository_path: str):

        detected_files = []
        dependencies = set()

        repository = Path(repository_path)

        for file in RepositoryScanner.scan_files(repository_path):

            if not RepositoryFilter.is_valid_file(file):
                continue

            if file.name.lower() not in self.DEPENDENCY_FILES:
                continue

            detected_files.append(str(file.relative_to(repository)))

            try:
                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

            except Exception:
                continue

            if file.name.lower() == "requirements.txt":
                self._parse_requirements(
                    content,
                    dependencies
                )

            elif file.name.lower() == "pyproject.toml":
                self._parse_pyproject(
                    content,
                    dependencies
                )

        return {
            "files_detected": detected_files,
            "total_dependencies": len(dependencies),
            "dependencies": sorted(dependencies)
        }

    def _parse_requirements(
        self,
        content: str,
        dependencies: set
    ):

        for line in content.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            dependency = (
                line.split("==")[0]
                    .split(">=")[0]
                    .split("<=")[0]
                    .strip()
            )

            if dependency:
                dependencies.add(dependency)

    def _parse_pyproject(self,content: str,dependencies: set):
    

        inside_dependencies = False

        for line in content.splitlines():

            line = line.strip()

            if line.startswith("dependencies"):
                inside_dependencies = True
                continue

            if inside_dependencies:

                if line.startswith("]"):
                    break

                line = line.strip().strip(",")

                line = line.strip('"').strip("'")

                if not line:
                    continue

                dependency = (
                    line.split("==")[0]
                        .split(">=")[0]
                        .split("<=")[0]
                        .split(">")[0]
                        .split("<")[0]
                        .strip()
                )

                if dependency:
                    dependencies.add(dependency)