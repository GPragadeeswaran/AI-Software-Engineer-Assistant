class ScoreDetector:

    @staticmethod
    def initialize_scores(keywords: dict):

        scores = {}

        for technology in keywords:
            scores[technology] = 0

        return scores

    @staticmethod
    def get_best_match(scores: dict):

        highest_score = max(scores.values())

        if highest_score == 0:
            return "Unknown"

        return max(scores, key=scores.get)