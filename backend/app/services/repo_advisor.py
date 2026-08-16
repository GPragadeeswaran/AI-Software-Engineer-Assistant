class RepoAdvisor:

    def generate_recommendations(
        self,
        docker,
        database,
        dependencies,
        security,
        code_quality
    ):

        recommendations = []

        # Docker
        if docker == "Not Detected":
            recommendations.append({
                "priority": "Medium",
                "title": "Add Docker Support",
                "reason": "Docker improves deployment consistency and simplifies application setup."
            })

        # Database
        if database == "Unknown":
            recommendations.append({
                "priority": "High",
                "title": "Configure a Database",
                "reason": "No database was detected. Most production applications require persistent storage."
            })  

        # Dependencies
        if dependencies["total_dependencies"] == 0:
            recommendations.append({
                "priority": "Medium",
                "title": "Declare Project Dependencies",
                "reason": "No dependencies were detected. Ensure dependency files are properly configured."
            })  

        # Security
        if security["risk_count"] > 0:
            recommendations.append({
                "priority": "High",
                "title": "Resolve Security Risks",
                "reason": f"{security['risk_count']} potential security issue(s) detected."
            })

        # Code Quality
        if code_quality["todo_count"] > 0:
            recommendations.append({
                "priority": "Low",
                "title": "Resolve TODO Comments",
                "reason": f"{code_quality['todo_count']} TODO comments found."
            })

        if code_quality["debug_count"] > 0:
            recommendations.append({
                "priority": "Low",
                "title": "Remove Debug Statements",
                "reason": f"{code_quality['debug_count']} debug statements detected."
            })

            priority_order = {
                "High": 1,
                "Medium": 2,
                "Low": 3
            }

            recommendations.sort(
                key=lambda recommendation: priority_order.get(
                    recommendation["priority"],
                    999
                )
            )

        return recommendations