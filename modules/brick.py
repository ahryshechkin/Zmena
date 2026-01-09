class Brick:
    def __init__(self, tag, index, side, lineno, lexeme):
        self.tag = tag
        self.uid = index
        self.side = side
        self.lineno = lineno
        self.name = lexeme.name()
        self.type = lexeme.type()
        self.constraint = lexeme.constraint()


    def __str__(self):
        constraint = self.constraint if self.constraint else ""
        return (
            f"{self.tag:>7} | {self.uid:>8} | {self.side} | {self.name:>7} | "
            f"{self.type:>13} | {constraint:>10} |"
        )


class LeftBrick(Brick):
    def __init__(self, tag, index, lineno, lexeme):
        super().__init__(tag, index, "L", lineno, lexeme)


class RightBrick(Brick):
    def __init__(self, tag, index, lineno, lexeme):
        super().__init__(tag, index, "R", lineno, lexeme)
