from zmena.domain.migration_forge.core.column_change import ColumnChange
from zmena.domain.migration_forge.kinds.column_change_kind import ColumnChangeKind


class ColumnEvolution:
    def __repr__(self):
        return "ColumnEvolution"

    def between(self, before, after):
        if before is None:
            return ColumnChange(ColumnChangeKind.ADD, None, after)

        if after is None:
            return ColumnChange(ColumnChangeKind.DROP, before, None)

        if before == after:
            return ColumnChange(ColumnChangeKind.UNCHANGED, before, after)

        return ColumnChange(ColumnChangeKind.MODIFY, before, after)
