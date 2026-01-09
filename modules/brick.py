from modules.constant import Side
from modules.lexeme import Lexeme


class Brick:
    def __init__(self, tag, uid, side, lineno, name, data_type, constraint):
        self.tag = tag
        self.uid = uid
        self.side = side
        self.lineno = lineno
        self.name = name
        self.type = data_type
        self.constraint = constraint



    def __str__(self):
        constraint = self.constraint if self.constraint else ""
        return (
            f"{self.tag:>7} | {self.uid:>8} | "
            f"{self.side.value} | {self.name:>7} | "
            f"{self.type:>13} | {constraint:>10} |"
        )


class LeftBrick(Brick):
    def __init__(self, offset, hunk):
        lexeme = Lexeme(hunk.left_line(offset))
        super().__init__(
            hunk.tag(),
            hunk.uid(),
            Side.LEFT,
            hunk.right_lineno(offset),
            lexeme.name(),
            lexeme.type(),
            lexeme.constraint()
        )


class RightBrick(Brick):
    def __init__(self, offset, hunk):
        lexeme = Lexeme(hunk.right_line(offset))
        super().__init__(
            hunk.tag(),
            hunk.uid(),
            Side.RIGHT,
            hunk.right_lineno(offset),
            lexeme.name(),
            lexeme.type(),
            lexeme.constraint()
        )
