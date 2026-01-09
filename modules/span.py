class Span:
    def __init__(self, lines, low, high):
        self.lines = lines
        self.low = low
        self.high = high


    def uid(self):
        return f"{self.low}{self.high}"


    def lineno(self, offset):
        return self.low + offset


    def line(self, offset):
        return self.lines[self.low + offset]


    def range(self):
        return self.high - self.low
