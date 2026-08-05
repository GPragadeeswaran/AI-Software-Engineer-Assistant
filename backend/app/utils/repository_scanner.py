from pathlib import Path

from app.utils.repository_constants import IGNORE_FOLDERS


class RepositoryScanner:

    @staticmethod
    def scan_files(repository_path: str):

        for item in Path(repository_path).rglob("*"):

            if any(folder in item.parts for folder in IGNORE_FOLDERS):
                continue

            if not item.is_file():
                continue

            yield item

    @staticmethod
    def scan_directories(repository_path: str):

        for item in Path(repository_path).rglob("*"):

            if any(folder in item.parts for folder in IGNORE_FOLDERS):
                continue

            if not item.is_dir():
                continue

            yield item