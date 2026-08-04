from pathlib import Path
from app.utils.repository_constants import (
    IMPORTANT_FILES,
    IGNORE_FOLDERS
)


class TestingService:

    def detect_testing_framework(self, repository_path: str):

        testing_keywords = {

            "pytest": [
                "pytest",
                "import pytest",
                "@pytest"
            ],

            "unittest": [
                "import unittest",
                "unittest.TestCase"
            ],

            "nose": [
                "nose",
                "nosetest"
            ],

            "JUnit": [
                "org.junit",
                "@Test",
                "JUnit"
            ],

            "TestNG": [
                "org.testng",
                "@Test"
            ],

            "Jest": [
                "jest",
                "describe(",
                "test("
            ],

            "Mocha": [
                "mocha",
                "describe(",
                "it("
            ],

            "Vitest": [
                "vitest",
                "describe(",
                "expect("
            ],

            "NUnit": [
                "nunit",
                "[Test]"
            ],

            "xUnit": [
                "xunit",
                "[Fact]"
            ],

            "Go Testing": [
                "testing",
                "func Test"
            ],

            "Cargo Test": [
                "cargo test"
            ]
        }

        scores = {}

        for framework in testing_keywords:
            scores[framework] = 0

        for file in Path(repository_path).rglob("*"):

            if any(folder in file.parts for folder in IGNORE_FOLDERS):
                continue

            if not file.is_file():
                continue

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

            for framework, keywords in testing_keywords.items():

                for keyword in keywords:

                    if keyword.lower() in content:
                        scores[framework] += 1

        highest_score = max(scores.values())

        if highest_score == 0:
            return "Unknown"

        return max(scores, key=scores.get)