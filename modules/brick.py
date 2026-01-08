class Brick:
    def __init__(self, tag, index, side, lineno, lexeme):
        self.tag = tag
        self.index = index.get()
        self.side = side
        self.lineno = lineno
        self.name = lexeme.name()
        self.type = lexeme.type()
        self.constraint = lexeme.constraint()


    def __str__(self):
        constraint = self.constraint if self.constraint else ""
        return (
            f"{self.tag:>7} | {self.index:>8} | {self.side} | {self.name:>7} | "
            f"{self.type:>13} | {constraint:>10} |"
        )
