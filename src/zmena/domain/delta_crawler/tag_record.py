class TagRecord:
    def __init__(self, line):
        self.line = line

    def __repr__(self):
        return f"TagRecord(line={self.line})"

    def name(self):
        return self.line.strip().split(maxsplit=1)[0]

    def annotation(self):
        return self.line.strip().split(maxsplit=1)[1]
