class EvaluationContext:
    def __init__(self, heuristics):
        self.heuristics = heuristics

    def __repr__(self):
        return f"EvaluationContext(heuristics={len(self.heuristics)})"

    def reassess(self, candidates):
        return candidates
