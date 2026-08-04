from pathlib import Path
from app.utils.repository_constants import (IGNORE_FOLDERS)



class DockerService:

    def detect_docker(self, repository_path: str):

        docker_files = {
            "dockerfile": "Docker",
            "docker-compose.yml": "Docker Compose",
            "docker-compose.yaml": "Docker Compose"
        }   

        for file in Path(repository_path).rglob("*"):

            if any(folder in file.parts for folder in IGNORE_FOLDERS):
                continue

            if not file.is_file():
                continue

            filename = file.name.lower()

            if filename in docker_files:
                return docker_files[filename]   


        return "Not Detected"    