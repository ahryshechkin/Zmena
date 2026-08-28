from zmena.domain.migration_forge.operations.add_column import AddColumn
from zmena.domain.migration_forge.operations.alter_data_type import AlterDataType
from zmena.domain.migration_forge.operations.drop_column import DropColumn
from zmena.domain.migration_forge.operations.rename_column import RenameColumn


class Migration:
    def plan(self, change):
        if change.is_add():
            return [AddColumn(change.after.name, change.after.data_type, change.after.nullable)]

        if change.is_drop():
            return [DropColumn(change.before.name)]

        operations = []
        if change.has_name_change():
            operations.append(RenameColumn(change.before.name, change.after.name))
        if change.has_data_type_change():
            operations.append(
                AlterDataType(change.before.name, change.before.data_type, change.after.data_type)
            )

        return operations
