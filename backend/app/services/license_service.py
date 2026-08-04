from pathlib import Path


class LicenseService:

    def detect_license(self, repository_path: str):

        license_files = {
            "license",
            "license.txt",
            "license.md",
            "copying"
        }

        license_keywords = {

            "MIT": [
                "mit license",
                "permission is hereby granted"
            ],

            "Apache 2.0": [
                "apache license",
                "apache license, version 2.0",
                "version 2.0, january 2004"
            ],

            "BSD 3-Clause": [
                "redistribution and use in source and binary forms",
                "neither the name of",
                "all rights reserved"
            ],

            "BSD 2-Clause": [
                "redistribution and use in source and binary forms",
                "this list of conditions and the following disclaimer"
            ],

            "GPL v3": [
                "gnu general public license",
                "version 3"
            ],

            "GPL v2": [
                "gnu general public license",
                "version 2"
            ],

            "LGPL": [
                "gnu lesser general public license"
            ],

            "MPL 2.0": [
                "mozilla public license",
                "version 2.0"
            ],

            "ISC": [
                "isc license"
            ],

            "Unlicense": [
                "this is free and unencumbered software released into the public domain"
            ]
        }

        scores = {}

        for license_name in license_keywords:
            scores[license_name] = 0

        for file in Path(repository_path).rglob("*"):

            if not file.is_file():
                continue

            filename = file.name.lower()

            if filename not in license_files:
                continue

            try:
                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).lower()

            except Exception:
                continue

            for license_name, keywords in license_keywords.items():

                for keyword in keywords:

                    if keyword in content:
                        scores[license_name] += 1

        highest_score = max(scores.values())

        if highest_score == 0:
            return "Unknown"

        return max(scores, key=scores.get)