from zmena.domain.model.column_spec import ColumnSpec
from zmena.domain.types.side import Side

from .fragment import Fragment


class RightFragment(Fragment):
    def __init__(self, offset, hunk):
        column_spec = ColumnSpec(hunk.right_line(offset))
        super().__init__(
            hunk.kind(),
            Side.RIGHT,
            hunk.fingerprint(),
            hunk.right_lineno(offset),
            column_spec.name(),
            column_spec.type(),
            column_spec.constraint(),
        )
