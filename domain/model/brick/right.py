from domain.services import Side

from .base import Brick
from ..lexeme import Lexeme


class BrickRight(Brick):
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
