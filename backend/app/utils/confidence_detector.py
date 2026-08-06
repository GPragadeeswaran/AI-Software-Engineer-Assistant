class ConfidenceDetector:

    @staticmethod
    def calculate(scores: dict):

        highest_score = max(scores.values())

        if highest_score == 0:
            return 0

        total_score = sum(scores.values())

        # How dominant is the winner?
        dominance = (highest_score / total_score) * 100

        # How much evidence do we have?
        evidence = min((highest_score / 10) * 100, 100)

        # Final confidence
        confidence = (dominance + evidence) / 2

        return round(confidence)