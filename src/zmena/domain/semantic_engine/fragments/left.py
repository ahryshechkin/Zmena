from zmena.domain.semantic_engine.core.column_spec import ColumnSpec
from zmena.domain.semantic_engine.fragments.fragment import Fragment
from zmena.domain.semantic_engine.types.side import Side


class LeftFragment(Fragment):
    def __init__(self, offset, hunk):
        column_spec = ColumnSpec(hunk.left_line(offset))
        super().__init__(
            hunk.kind(),
            hunk.fingerprint(),
            hunk.left_lineno(offset),
            Side.LEFT,
            column_spec.name(),
            column_spec.data_type(),
            column_spec.constraint(),
        )
