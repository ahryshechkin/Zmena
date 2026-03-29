from zmena.domain.model.lexeme import Lexeme
from zmena.domain.types.side import Side

from .base import Brick


class BrickRight(Brick):
    def __init__(self, offset, hunk):
        lexeme = Lexeme(hunk.right_line(offset))
        super().__init__(
            hunk.tag(),
            Side.RIGHT,
            hunk.fingerprint(),
            hunk.right_lineno(offset),
            lexeme.name(),
            lexeme.type(),
            lexeme.constraint(),
        )
