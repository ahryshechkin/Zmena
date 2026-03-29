from zmena.domain.model.lexeme import Lexeme
from zmena.domain.types.side import Side

from .base import Brick


class BrickLeft(Brick):
    def __init__(self, offset, hunk):
        lexeme = Lexeme(hunk.left_line(offset))
        super().__init__(
            hunk.kind(),
            Side.LEFT,
            hunk.fingerprint(),
            hunk.left_lineno(offset),
            lexeme.name(),
            lexeme.type(),
            lexeme.constraint(),
        )
