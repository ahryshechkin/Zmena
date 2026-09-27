class EvidenceView:
    def __init__(self, evidence):
        self.evidence = evidence

    def detail(self):
        return f"{abs(self.evidence.score):<5}{self.evidence.reason}"

    def polarity(self):
        return "+" if self.evidence.score >= 0 else "-"
