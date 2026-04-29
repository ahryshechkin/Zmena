from zmena.domain.model.column_spec import ColumnSpec
from zmena.domain.model.fragments.fragment import Fragment
from zmena.domain.types.side import Side


class LeftFragment(Fragment):
    def __init__(self, offset, hunk):
        column_spec = ColumnSpec(hunk.left_line(offset))
        super().__init__(
            hunk.kind(),
            Side.LEFT,
            hunk.fingerprint(),
            hunk.left_lineno(offset),
            column_spec.name(),
            column_spec.data_type(),
            column_spec.constraint(),
        )
