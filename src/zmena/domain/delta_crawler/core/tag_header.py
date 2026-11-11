class TagHeader:
    def __init__(self, line):
        self.line = line

    def __repr__(self):
        return f"TagHeader(line={self.line})"

    def name(self):
        return self.line.strip().split(maxsplit=1)[0]

    def summary(self):
        return self.line.strip().split(maxsplit=1)[1]
