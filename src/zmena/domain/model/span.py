class Span:
    def __init__(self, lines, low, high):
        self.lines = lines
        self.low = low
        self.high = high

    def __repr__(self):
        return f"Span(lines={len(self.lines)},low={self.low},high={self.high})"

    def fingerprint(self):
        return f"{str(self.low).zfill(2)}{str(self.high).zfill(2)}"

    def lineno(self, offset):
        return self.low + offset

    def line(self, offset):
        return self.lines[self.low + offset]

    def range(self):
        return self.high - self.low
