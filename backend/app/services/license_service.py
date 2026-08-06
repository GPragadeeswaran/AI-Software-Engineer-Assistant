from app.utils.score_detector import ScoreDetector
from app.utils.repository_scanner import RepositoryScanner
from app.utils.confidence_detector import ConfidenceDetector
from app.utils.repository_constants import LICENSE_KEYWORDS


class LicenseService:

    def detect_license(self, repository_path: str):

        license_files = {
            "license",
            "license.txt",
            "license.md",
            "copying"
        }

        scores = ScoreDetector.initialize_scores(LICENSE_KEYWORDS)

        for file in RepositoryScanner.scan_files(repository_path):

            # Only process license files
            if file.name.lower() not in license_files:
                continue

            try:
                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).lower()

            except Exception:
                continue

            for license_name, keywords in LICENSE_KEYWORDS.items():

                for keyword in keywords:

                    if keyword in content:
                        scores[license_name] += 1

        return {
            "name": ScoreDetector.get_best_match(scores),
            "confidence": ConfidenceDetector.calculate(scores)
        }