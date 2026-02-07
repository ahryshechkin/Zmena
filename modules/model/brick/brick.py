from modules.constant import Side, Tag
from modules.model.lexeme import Lexeme


class Brick:
    def __init__(self, tag, side, segment, position, name, data_type, constraint):
        self.tag = tag
        self.side = side
        self.segment = segment
        self.position = position
        self.name = name
        self.data_type = data_type
        self.constraint = constraint


    def __str__(self):
        constraint = self.constraint if self.constraint else ""
        return (
            f"{self.tag.value:>7} | {self.side.value:>4} | "
            f"{self.segment:>8} | {self.position:>8} | "
            f"{self.name:<7} | {self.data_type:<13} | {constraint:>10} |"
        )


    def __repr__(self):
        return (
            f"Brick("
            f"tag={self.tag.value},side={self.side.value},"
            f"segment={self.segment},position={self.position},"
            f"name={self.name},data_type={self.data_type},"
            f"constraint={self.constraint})"
        )


    def compare_by_name(self, brick):
        return self.name == brick.name


    def compare_by_position(self, brick):
        return self.position == brick.position


    def compare_by_signature(self, brick):
        return (
            self.segment == brick.segment and
            self.data_type == brick.data_type and
            self.constraint == brick.constraint
        )


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

class StubBrick(Brick):
    def __init__(self, side):
        super().__init__(Tag.STUB, side, "", "", "", "", None)
