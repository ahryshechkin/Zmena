class EvidenceView:
    def __init__(self, score, reason):
        self.score = score
        self.reason = reason

    def detail(self):
        return f"{abs(self.score):<5}{self.reason}"

    def polarity(self):
        return "+" if self.score >= 0 else "-"
