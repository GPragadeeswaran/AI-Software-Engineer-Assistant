from pathlib import Path


class ArchitectureService:

    def detect_architecture(self, repository_path: str):

        folders = {
            folder.name.lower()
            for folder in Path(repository_path).rglob("*")

            if folder.is_dir()
        }

        layered_folders = {
            "api",
            "routes",
            "controllers",
            "services",
            "schemas",
            "models",
            "repositories",
            "db",
            "core"
        }

        mvc_folders = {
            "models",
            "views",
            "controllers",
            "templates",
            "static"
        }

        clean_folders = {
            "domain",
            "application",
            "infrastructure",
            "entities",
            "use_cases",
            "interfaces"
        }

        layered_score = len(folders.intersection(layered_folders))
        mvc_score = len(folders.intersection(mvc_folders))
        clean_score = len(folders.intersection(clean_folders))

        if mvc_score >= 3:
            return "MVC"

        if layered_score >= 4:
            return "Layered Architecture"

        if clean_score >= 3:
            return "Clean Architecture"

        return "Monolithic"