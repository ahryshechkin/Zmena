class Brick:
    def __init__(self, tag, index, side, lineno, lexeme):
        self.tag = tag
        self.index = index
        self.side = side
        self.lineno = lineno
        self.name = lexeme.name()
        self.type = lexeme.type()
        self.constraint = lexeme.constraint()