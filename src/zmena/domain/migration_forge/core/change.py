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
        if self.before and self.after:
            return self.before.data_type != self.after.data_type
        return False

    def has_name_change(self):
        if self.before and self.after:
            return self.before.name != self.after.name
        return False

    def has_nullability_change(self):
        if self.before and self.after:
            return self.before.nullable != self.after.nullable
        return False
