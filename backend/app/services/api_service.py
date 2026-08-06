from pathlib import Path
from app.utils.score_detector import ScoreDetector
from app.utils.repository_scanner import RepositoryScanner
from app.utils.confidence_detector import ConfidenceDetector
from app.utils.repository_constants import (
    IMPORTANT_FILES,
    IGNORE_FOLDERS,
    API_KEYWORDS
)


class APIService:

    def detect_api_framework(self, repository_path: str):

        scores = ScoreDetector.initialize_scores(API_KEYWORDS)

        for file in RepositoryScanner.scan_files(repository_path):

            # Process only supported files
            if (
                file.name.lower() not in IMPORTANT_FILES
                and file.suffix.lower() not in {
                    ".py",
                    ".java",
                    ".js",
                    ".ts",
                    ".cs"
                }
            ):
                continue

            # Read file
            try:
                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).lower()

            except Exception:
                continue

            # Increase scores
            for framework, keywords in API_KEYWORDS.items():

                for keyword in keywords:

                    if keyword.lower() in content:
                        scores[framework] += 1

        return {
                "name": ScoreDetector.get_best_match(scores),
                "confidence": ConfidenceDetector.calculate(scores)
            }