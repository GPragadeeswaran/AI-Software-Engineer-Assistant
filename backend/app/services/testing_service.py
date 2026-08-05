from pathlib import Path
from app.utils.score_detector import ScoreDetector
from app.utils.repository_scanner import RepositoryScanner
from app.utils.repository_constants import (
    IMPORTANT_FILES,
    TESTING_KEYWORDS
)


class TestingService:

    def detect_testing_framework(self, repository_path: str):

        scores = ScoreDetector.initialize_scores(TESTING_KEYWORDS)

        for file in RepositoryScanner.scan_files(repository_path):

            if (
                file.name.lower() not in IMPORTANT_FILES
                and file.suffix.lower() not in {
                    ".py",
                    ".java",
                    ".js",
                    ".ts",
                    ".cs",
                    ".go",
                    ".rs"
                }
            ):
                continue


            try:
                content = file.read_text(
                    encoding="utf-8"
                ).lower()

            except Exception:
                continue

            for framework, keywords in TESTING_KEYWORDS.items():

                for keyword in keywords:

                    if keyword.lower() in content:
                        scores[framework] += 1


        return ScoreDetector.get_best_match(scores)