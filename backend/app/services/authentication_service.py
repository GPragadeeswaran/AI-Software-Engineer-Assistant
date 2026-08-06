from pathlib import Path
from app.utils.score_detector import ScoreDetector
from app.utils.repository_scanner import RepositoryScanner
from app.utils.confidence_detector import ConfidenceDetector
from app.utils.repository_constants import (
    IMPORTANT_FILES,
    IGNORE_FOLDERS,
    AUTHENTICATION_KEYWORDS
)


class AuthenticationService:

    def detect_authentication(self, repository_path: str):

        scores = ScoreDetector.initialize_scores(AUTHENTICATION_KEYWORDS)

        for file in RepositoryScanner.scan_files(repository_path):

            if (
                file.name.lower() not in IMPORTANT_FILES
                and file.suffix.lower() not in {
                    ".py", ".java", ".js", ".ts", ".cs"
                }
            ):
                continue

            try:
                content = file.read_text(
                    encoding="utf-8"
                ).lower()

            except Exception:
                continue

            for auth_type, keywords in AUTHENTICATION_KEYWORDS.items():

                for keyword in keywords:

                    if keyword.lower() in content:
                        scores[auth_type] += 1

        return {
                "name": ScoreDetector.get_best_match(scores),
                "confidence": ConfidenceDetector.calculate(scores)
            }