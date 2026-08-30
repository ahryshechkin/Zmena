from zmena.domain.semantic_engine.core.column_spec import ColumnSpec
from zmena.domain.semantic_engine.fragments.fragment import Fragment
from zmena.domain.semantic_engine.kinds.side import SideKind


class LeftFragment(Fragment):
    def __init__(self, offset, hunk):
        column_spec = ColumnSpec(hunk.left_line(offset))
        super().__init__(
            hunk.kind(),
            hunk.fingerprint(),
            hunk.left_lineno(offset),
            SideKind.LEFT,
            column_spec.name(),
            column_spec.data_type(),
            column_spec.constraint(),
        )
