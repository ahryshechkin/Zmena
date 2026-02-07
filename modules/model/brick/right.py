from modules.constant import Side
from modules.model.lexeme import Lexeme

from .base import Brick


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
