from zmena.domain.migration_forge.statements.add_column import AddColumnStatement
from zmena.domain.migration_forge.statements.alter_data_type import AlterDataTypeStatement
from zmena.domain.migration_forge.statements.drop_column import DropColumnStatement
from zmena.domain.migration_forge.statements.drop_not_null import DropNotNullStatement
from zmena.domain.migration_forge.statements.rename_column import RenameColumnStatement
from zmena.domain.migration_forge.statements.set_not_null import SetNotNullStatement


class Inference:
    def __init__(self, change):
        self.change = change

    def __repr__(self):
        return f"Inference(name={self.change.name()})"

    def derive(self):
        tab_name = self.change.name()
        before, after = self.change.snapshots()
        statements = []

        if self.change.is_add():
            statements.append(
                AddColumnStatement(tab_name, after.name, after.data_type, after.nullable)
            )

        if self.change.is_drop():
            statements.append(DropColumnStatement(tab_name, before.name))

        if self.change.has_name_change():
            statements.append(RenameColumnStatement(tab_name, before.name, after.name))

        if self.change.has_data_type_change():
            statements.append(AlterDataTypeStatement(tab_name, after.name, after.data_type))

        if self.change.has_nullability_change():
            if before.nullable:
                statements.append(SetNotNullStatement(tab_name, after.name))
            else:
                statements.append(DropNotNullStatement(tab_name, after.name))

        return statements
