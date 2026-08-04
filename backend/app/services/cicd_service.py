from pathlib import Path

from app.utils.repository_constants import IGNORE_FOLDERS


class CICDService:

    def detect_cicd(self, repository_path: str):

        cicd_files = {
            ".gitlab-ci.yml": "GitLab CI",
            "Jenkinsfile": "Jenkins",
            "azure-pipelines.yml": "Azure Pipelines",
            ".travis.yml": "Travis CI"
        }

        # Detect GitHub Actions
        workflow_dir = Path(repository_path) / ".github" / "workflows"

        if workflow_dir.exists():

            for workflow in workflow_dir.iterdir():

                if workflow.is_file() and workflow.suffix.lower() in {
                    ".yml",
                    ".yaml"
                }:
                    return "GitHub Actions"

        # Detect other CI/CD tools
        for item in Path(repository_path).rglob("*"):

            if any(folder in item.parts for folder in IGNORE_FOLDERS):
                continue

            if not item.is_file():
                continue

            filename = item.name

            if filename in cicd_files:
                return cicd_files[filename]

        return "Not Detected"