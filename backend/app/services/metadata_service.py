from pathlib import Path


class MetadataService:

    def extract_metadata(self, repository_path: str):

        repository = Path(repository_path)

        total_files = 0
        total_folders = 0

        primary_language = self.detect_language(repository_path)
        framework = self.detect_framework(repository_path)
        package_manager = self.detect_package_manager(repository_path)
        readme = self.detect_readme(repository_path)

        for item in repository.rglob("*"):

            if ".git" in item.parts:
                 continue

            if item.is_file():
                total_files += 1

            elif item.is_dir():
                total_folders += 1

        return {
            "total_files": total_files,
            "total_folders": total_folders,
            "primary_language": primary_language,
            "framework": framework,
            "package_manager": package_manager,
            "readme": readme        
            }

    def detect_language(self, repository_path: str):

        extensions = {}

        for file in Path(repository_path).rglob("*"):

             if ".git" in file.parts:
                 continue

             if file.is_file():

                extension = file.suffix.lower()

                if extension:
                        extensions[extension] = extensions.get(extension, 0) + 1

        language_map = {
            ".py": "Python",
            ".js": "JavaScript",
            ".ts": "TypeScript",
            ".java": "Java",
            ".cpp": "C++",
            ".c": "C",
            ".cs": "C#",
            ".go": "Go",
            ".rs": "Rust",
            ".php": "PHP",
            ".rb": "Ruby",
            ".swift": "Swift",
            ".kt": "Kotlin"
        }

        if not extensions:
            return "Unknown"

        primary_extension = max(extensions, key=extensions.get)

        return language_map.get(primary_extension, "Unknown")

    def detect_framework(self, repository_path: str):

        framework_map = {
            "fastapi": "FastAPI",
            "flask": "Flask",
            "django": "Django",
            "react": "React",
            "angular": "Angular",   
            "vue": "Vue",
            "spring": "Spring Boot"
        }

        for file in Path(repository_path).rglob("*"):

            if ".git" in file.parts:
                continue

            if file.is_file():

                file_name = file.name.lower()

                if file_name == "requirements.txt":

                    content = file.read_text(errors="ignore").lower()

                    for keyword, framework in framework_map.items():

                        if keyword in content:
                            return framework

        return "Unknown"

    def detect_package_manager(self, repository_path: str):

        package_managers = [
            ("uv.lock", "uv"),
            ("poetry.lock", "Poetry"),
            ("pyproject.toml", "pyproject"),
            ("requirements.txt", "pip"),
            ("package-lock.json", "npm"),
            ("pnpm-lock.yaml", "pnpm"),
            ("yarn.lock", "Yarn"),
            ("package.json", "npm"),
            ("pom.xml", "Maven"),
            ("build.gradle", "Gradle"),
            ("Cargo.toml", "Cargo"),
            ("go.mod", "Go Modules")
        ]
        files = {file.name for file in Path(repository_path).rglob("*") if file.is_file()}

        for file_name, package_manager in package_managers:

            if file_name in files:
                return package_manager

        return "Unknown"

    def detect_readme(self, repository_path: str):

        readme_files = [
            "README.md",
            "README.rst",
            "README.txt",
            "README"
        ]

        for file in Path(repository_path).rglob("*"):

            if ".git" in file.parts:
                continue

            if file.is_file():

                if file.name in readme_files:

                    return {
                        "exists": True,
                        "file_name": file.name
                    }

        return {
            "exists": False,
            "file_name": None
        }