class Evidence:
    def __init__(self, hypothesis, signal, weight, reason):
        self.hypothesis = hypothesis
        self.signal = signal
        self.weight = weight
        self.reason = reason

    def __repr__(self):
        return f"Evidence(signal={self.signal},weight={self.weight},reason={self.reason})"

    def score(self):
        return self.signal * self.weight

    def describe(self):
        return self.reason
