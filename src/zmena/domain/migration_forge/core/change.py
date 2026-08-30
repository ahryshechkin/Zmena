from zmena.domain.migration_forge.kinds.column_change_kind import ColumnChangeKind


class Change:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def __repr__(self):
        return "Change"

    def snapshots(self):
        return self.before, self.after

    def is_add(self):
        return self.kind == ColumnChangeKind.ADD

    def is_drop(self):
        return self.kind == ColumnChangeKind.DROP

    def has_data_type_change(self):
        return self.before.data_type != self.after.data_type

    def has_name_change(self):
        return self.before.name != self.after.name

    def has_nullability_change(self):
        return self.before.nullable != self.after.nullable

    def has_position_change(self):
        return self.before.position != self.after.position
