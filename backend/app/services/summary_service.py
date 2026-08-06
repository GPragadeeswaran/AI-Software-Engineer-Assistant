class SummaryService:

    def generate_summary(
        self,
        metadata: dict,
        architecture: dict,
        api_framework: dict,
        authentication: dict,
        testing: dict,
        cicd: str,
        license_name: dict
    ):

        summary = (
            f"This repository is a "
            f"{metadata['primary_language']} project "
            f"built using {api_framework['name']}. "
            f"It follows a {architecture['name']} architecture. "
            f"It uses {authentication['name']} authentication. "
            f"Testing is implemented using {testing['name']}. "
            f"CI/CD is configured with {cicd}. "
            f"The project is licensed under {license_name['name']}."
        )

        return summary