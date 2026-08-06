class SuggestionService:

    def generate_suggestions(
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

        suggestions = []

        # README
        if not metadata["readme"]["exists"]:
            suggestions.append("Add a README file.")

        # Architecture
        if architecture["name"] == "Unknown":
            suggestions.append("Improve the project structure for architecture detection.")

        # Database
        if database == "Unknown":
            suggestions.append("Configure a database for the project.")

        # API Framework
        if api_framework["name"] == "Unknown":
            suggestions.append("Use a recognized API framework.")

        # Authentication
        if authentication["name"] == "Unknown":
            suggestions.append("Implement an authentication mechanism.")

        # Testing
        if testing_framework["name"] == "Unknown":
            suggestions.append("Add automated tests.")

        # Docker
        if docker == "Not Detected":
            suggestions.append("Add Docker support.")

        # CI/CD
        if cicd == "Not Detected":
            suggestions.append("Configure a CI/CD pipeline.")

        # License
        if license_type["name"] == "Unknown":
            suggestions.append("Add an open-source license.")

        if not suggestions:
            suggestions.append("No major improvements detected.")

        return suggestions