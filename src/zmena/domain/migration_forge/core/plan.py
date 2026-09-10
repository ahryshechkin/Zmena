from zmena.domain.migration_forge.statements.add_column import AddColumnStatement
from zmena.domain.migration_forge.statements.alter_data_type import AlterDataTypeStatement
from zmena.domain.migration_forge.statements.drop_column import DropColumnStatement
from zmena.domain.migration_forge.statements.drop_not_null import DropNotNullStatement
from zmena.domain.migration_forge.statements.rename_column import RenameColumnStatement
from zmena.domain.migration_forge.statements.set_not_null import SetNotNullStatement


class Plan:
    def __init__(self, change):
        self.change = change

    def __repr__(self):
        return "Plan"

    def derive(self):
        before, after = self.change.snapshots()
        statements = []

        if self.change.is_add():
            statements.append(AddColumnStatement(after.name, after.data_type, after.nullable))

        if self.change.is_drop():
            statements.append(DropColumnStatement(before.name))

        if self.change.has_name_change():
            statements.append(RenameColumnStatement(before.name, after.name))

        if self.change.has_data_type_change():
            statements.append(AlterDataTypeStatement(after.name, after.data_type))

        if self.change.has_nullability_change():
            if before.nullable:
                statements.append(SetNotNullStatement(after.name))
            else:
                statements.append(DropNotNullStatement(after.name))

        return statements
