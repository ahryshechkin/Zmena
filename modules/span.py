class Span:
    def __init__(self, lines, low, high):
        self.lines = lines
        self.low = low
        self.high = high


    def lineno(self, index):
        return self.low + index


    def line(self, index):
        return self.lines[self.low + index]


    def range(self):
        return self.high - self.low


    def index(self):
        return f"{self.low}{self.high}"
