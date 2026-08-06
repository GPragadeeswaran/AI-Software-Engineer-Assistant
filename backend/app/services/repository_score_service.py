from app.utils.repository_constants import HEALTH_SCORE_WEIGHTS


class RepositoryScoreService:

    def calculate_health_score(
        self,
        metadata: dict,
        architecture: dict,
        database: str,
        api_framework: dict,
        authentication: dict,
        testing_framework: dict,
        docker: str,
        cicd: str,
        license_type: dict
    ):

        score = 0

        # README
        if metadata["readme"]["exists"]:
            score += HEALTH_SCORE_WEIGHTS["readme"]

        # Architecture
        if architecture["name"] != "Unknown":
            score += HEALTH_SCORE_WEIGHTS["architecture"]

        # Database
        if database != "Unknown":
            score += HEALTH_SCORE_WEIGHTS["database"]

        # API Framework
        if api_framework["name"] != "Unknown":
            score += HEALTH_SCORE_WEIGHTS["api_framework"]

        # Authentication
        if authentication["name"] != "Unknown":
            score += HEALTH_SCORE_WEIGHTS["authentication"]

        # Testing
        if testing_framework["name"] != "Unknown":
            score += HEALTH_SCORE_WEIGHTS["testing"]

        # Docker
        if docker != "Not Detected":
            score += HEALTH_SCORE_WEIGHTS["docker"]

        # CI/CD
        if cicd != "Not Detected":
            score += HEALTH_SCORE_WEIGHTS["cicd"]

        # License
        if license_type["name"] != "Unknown":
            score += HEALTH_SCORE_WEIGHTS["license"]

        # Grade
        if score >= 90:
            grade = "A"

        elif score >= 75:
            grade = "B"

        elif score >= 60:
            grade = "C"

        elif score >= 40:
            grade = "D"

        else:
            grade = "F"

        return {
            "score": score,
            "grade": grade
        }