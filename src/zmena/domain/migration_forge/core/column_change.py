from zmena.domain.migration_forge.kinds.column_change_kind import ColumnChangeKind


class ColumnChange:
    def __init__(self, kind, before, after):
        self.kind = kind
        self.before = before
        self.after = after

    def __repr__(self):
        return f"ColumnChange(kind={self.kind})"

    def is_add(self):
        return self.kind == ColumnChangeKind.ADD

    def is_drop(self):
        return self.kind == ColumnChangeKind.DROP

    def is_modify(self):
        return self.kind == ColumnChangeKind.MODIFY

    def is_unchanged(self):
        return self.kind == ColumnChangeKind.UNCHANGED

    def has_data_type_change(self):
        pass

    def has_name_change(self):
        pass

    def has_nullability_change(self):
        pass

    def has_position_change(self):
        pass
