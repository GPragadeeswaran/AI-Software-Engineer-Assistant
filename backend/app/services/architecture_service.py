from pathlib import Path
from app.utils.score_detector import ScoreDetector
from app.utils.repository_scanner import RepositoryScanner
from app.utils.confidence_detector import ConfidenceDetector
from app.utils.repository_constants import (
    ARCHITECTURE_KEYWORDS
)


class ArchitectureService:

    def detect_architecture(self, repository_path: str):

        scores = ScoreDetector.initialize_scores(
            ARCHITECTURE_KEYWORDS
        )

        for folder in RepositoryScanner.scan_directories(repository_path):

            folder_name = folder.name.lower()

            for architecture, keywords in ARCHITECTURE_KEYWORDS.items():

                for keyword in keywords:

                    if folder_name == keyword.lower():
                        scores[architecture] += 1

        return {
            "name": ScoreDetector.get_best_match(scores),
            "confidence": ConfidenceDetector.calculate(scores)
        }