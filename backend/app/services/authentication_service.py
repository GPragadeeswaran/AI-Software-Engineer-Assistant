from pathlib import Path
from app.utils.repository_constants import (
    IMPORTANT_FILES,
    IGNORE_FOLDERS
)


class AuthenticationService:

    def detect_authentication(self, repository_path: str):

        authentication_keywords = {

            "JWT": [
                "jwt.encode",
                "jwt.decode",
                "pyjwt",
                "jsonwebtoken",
                "jjwt",
                "jwtbearer",
                "bearer ",
                "authorization: bearer",
                "bearer token"
            ],

            "OAuth": [
                "oauth2passwordbearer",
                "oauth2",
                "oauth",
                "authlib",
                "passport-google-oauth20",
                "spring-security-oauth2",
                "microsoft.aspnetcore.authentication",
                "google.oauth",
                "github.oauth"
            ],

            "Session": [
                "flask_login",
                "login_user",
                "@login_required",
                "request.session",
                "httpsession",
                "express-session",
                "cookie-session",
                "sessionmiddleware"
            ],

            "API Key": [
                "x-api-key",
                "x-auth-token",
                "api_key",
                "apikey",
                "api-token"
            ]
        }

        scores = {
            "JWT": 0,
            "OAuth": 0,
            "Session": 0,
            "API Key": 0
        }

        for file in Path(repository_path).rglob("*"):

            if any(folder in file.parts for folder in IGNORE_FOLDERS):
                continue

            if not file.is_file():
                continue

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

            for auth_type, keywords in authentication_keywords.items():

                for keyword in keywords:

                    if keyword.lower() in content:
                        scores[auth_type] += 1

        highest_score = max(scores.values())

        if highest_score == 0:
            return "Unknown"

        return max(scores, key=scores.get)