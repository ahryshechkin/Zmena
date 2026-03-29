class Evidence:
    def __init__(self, heuristic_label, hypothesis, score):
        self.heuristic_label = heuristic_label
        self.hypothesis = hypothesis
        self.score = score

    def __repr__(self):
        return f"Evidence(heuristic={self.heuristic_label},score={self.score})"
