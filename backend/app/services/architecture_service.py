from pathlib import Path
from app.utils.score_detector import ScoreDetector
from app.utils.repository_scanner import RepositoryScanner
from app.utils.repository_constants import (
    IGNORE_FOLDERS,
    ARCHITECTURE_KEYWORDS
)


class ArchitectureService:

    def detect_architecture(self, repository_path: str):

        scores = ScoreDetector.initialize_scores(ARCHITECTURE_KEYWORDS)

        for folder in RepositoryScanner.scan_directories(repository_path):

            folder_name = folder.name.lower()

            # Compare folder names
            for architecture, keywords in ARCHITECTURE_KEYWORDS.items():

                for keyword in keywords:

                    if folder_name == keyword.lower():
                        scores[architecture] += 1

        return ScoreDetector.get_best_match(scores)