from modules.constant import Side, Tag
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
            f"{self.tag:>7} | {self.side.value:>4} | "
            f"{self.segment:>8} | {self.position:>8} | "
            f"{self.name:<7} | {self.type:<13} | {constraint:>10} |"
        )


    def compare_by_name(self, brick):
        return self.name == brick.name


    def compare_by_position(self, brick):
        return self.position == brick.position


    def is_delete(self):
        return self.tag == Tag.DELETE and self.side == Side.LEFT


    def is_insert(self):
        return self.tag == Tag.INSERT and self.side == Side.RIGHT


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
