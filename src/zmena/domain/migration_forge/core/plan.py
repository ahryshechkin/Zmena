from zmena.domain.migration_forge.actions.add_column import AddColumn
from zmena.domain.migration_forge.actions.alter_data_type import AlterDataType
from zmena.domain.migration_forge.actions.drop_column import DropColumn
from zmena.domain.migration_forge.actions.rename_column import RenameColumn


class Plan:
    def __init__(self, change):
        self.change = change

    def derive(self):
        before, after = self.change.snapshots()
        actions = []

        if self.change.is_add():
            actions.append(AddColumn(after))

        if self.change.is_drop():
            actions.append(DropColumn(before))

        if self.change.has_name_change():
            actions.append(RenameColumn(before, after))

        if self.change.has_data_type_change():
            actions.append(AlterDataType(before, after))

        if self.change.has_nullability_change():
            actions.append()

        return actions
