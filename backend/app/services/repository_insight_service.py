class RepositoryInsightService:

    def generate_insights(
        self,
        analysis_result: dict
    ):

        strengths = []
        weaknesses = []

        testing = analysis_result.get("testing_framework")
        cicd = analysis_result.get("cicd")
        docker = analysis_result.get("docker")
        license_info = analysis_result.get("license")
        database = analysis_result.get("database")
        security = analysis_result.get("security")
        code_quality = analysis_result.get("code_quality")

        # -------------------------
        # Strength Detection
        # -------------------------

        if testing:
            strengths.append(
                "Testing framework is configured."
            )

        if cicd != "Not Detected":
            strengths.append(
                "CI/CD pipeline is configured."
            )

        if docker != "Not Detected":
            strengths.append(
                "Docker support is available."
            )

        if isinstance(license_info, dict):

            if license_info.get("name") != "Unknown":

                strengths.append(
                    "Repository contains a software license."
                )

        # -------------------------
        # Weakness Detection
        # -------------------------

        if database == "Unknown":

            weaknesses.append(
                "No database was detected."
            )

        if docker == "Not Detected":

            weaknesses.append(
                "Docker support is missing."
            )

        if security:

            if security.get("risk_count", 0) > 0:

                weaknesses.append(
                    f"{security['risk_count']} security risk(s) detected."
                )

        if code_quality:

            if code_quality.get("debug_count", 0) > 0:

                weaknesses.append(
                    f"{code_quality['debug_count']} debug statements found."
                )
        # -------------------------
        # Overall Health
        # -------------------------

        if len(weaknesses) == 0:

            overall_health = "Excellent"

        elif len(weaknesses) <= 2:

            overall_health = "Good"

        elif len(weaknesses) <= 4:

            overall_health = "Fair"

        else:

            overall_health = "Poor"

        # -------------------------
        # Next Priority
        # -------------------------

        if database == "Unknown":

            next_priority = (
                "Configure a database for persistent storage."
            )

        elif security and security.get("risk_count", 0) > 0:

            next_priority = (
                "Resolve the detected security issues."
            )

        elif docker == "Not Detected":

            next_priority = (
                "Add Docker support for easier deployment."
            )

        elif code_quality and code_quality.get("debug_count", 0) > 0:

            next_priority = (
                "Remove debug statements before production."
            )

        else:

            next_priority = (
                "Repository is well structured. Continue improving code quality."
            )
        return {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "overall_health": overall_health,
            "next_priority": next_priority
        }   