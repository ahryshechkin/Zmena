class Evidence:
    def __init__(self, heuristic, hypothesis, score):
        self.heuristic = heuristic
        self.hypothesis = hypothesis
        self.score = score

    def __repr__(self):
        return f"Evidence(heuristic={self.heuristic},score={self.score})"
