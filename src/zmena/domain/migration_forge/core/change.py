class Change:
    def __init__(self, before, after):
        self.before = before
        self.after = after

    def __repr__(self):
        return "Change"

    def snapshots(self):
        return self.before, self.after

    def is_add(self):
        return self.before is None

    def is_drop(self):
        return self.after is None

    def has_data_type_change(self):
        return self.before.data_type != self.after.data_type

    def has_name_change(self):
        return self.before.name != self.after.name

    def has_nullability_change(self):
        return self.before.nullable != self.after.nullable
