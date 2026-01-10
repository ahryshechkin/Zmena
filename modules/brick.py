from modules.constant import Side
from modules.lexeme import Lexeme


class Brick:
    def __init__(self, tag, side, segment, position, name, data_type, constraint):
        self.tag = tag
        self.side = side
        self.segment = segment
        self.position = position
        self.name = name
        self.type = data_type
        self.constraint = constraint


    def __str__(self):
        constraint = self.constraint if self.constraint else ""
        return (
            f"{self.tag:>7} | {self.side.value} | "
            f"{self.segment:>8} | {self.position:>3} | "
            f"{self.name:>7} | {self.type:>13} | {constraint:>10} |"
        )


class LeftBrick(Brick):
    def __init__(self, offset, hunk):
        lexeme = Lexeme(hunk.left_line(offset))
        super().__init__(
            hunk.tag(),
            Side.LEFT,
            hunk.uid(),
            hunk.left_lineno(offset),
            lexeme.name(),
            lexeme.type(),
            lexeme.constraint()
        )


class RightBrick(Brick):
    def __init__(self, offset, hunk):
        lexeme = Lexeme(hunk.right_line(offset))
        super().__init__(
            hunk.tag(),
            Side.RIGHT,
            hunk.uid(),
            hunk.right_lineno(offset),
            lexeme.name(),
            lexeme.type(),
            lexeme.constraint()
        )
