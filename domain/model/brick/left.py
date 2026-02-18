from domain.services import Side

from .base import Brick
from ..lexeme import Lexeme


class BrickLeft(Brick):
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
