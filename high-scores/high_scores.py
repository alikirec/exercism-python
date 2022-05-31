class HighScores:
    def __init__(self, scores):
        self.scores = scores.copy()
        self.sorted_scores = scores.copy()
        self.sorted_scores.sort(reverse=True)


    def latest(self):
        """
        returns the latest score
        """
        return self.scores[-1]


    def personal_best(self):
        """
        returns top score
        """
        return self.sorted_scores[0]


    def personal_top_three(self):
        """
        returns personal top 3 scores
        """
        return self.sorted_scores[:3]
