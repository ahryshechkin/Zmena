class ScoredLink:
    def __init__(self, score, link):
        self.score = score
        self.link = link


    def __lt__(self, other):
        return self.score < other.score


    def __repr__(self):
        return f"ScoredLink(score={self.score},link={repr(self.link)})"
