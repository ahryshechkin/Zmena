from zmena.domain.migration_forge.kinds.script import ScriptKind
from zmena.domain.migration_forge.scripts.script import Script


class AddColumnScript(Script):
    def __init__(self, statement):
        super().__init__(ScriptKind.ADD_COLUMN, statement)

    def assemble(self):
        tab_name = self.statement.tab_name
        col_name = self.statement.col_name
        data_type = self.statement.data_type
        nullable = "NULL" if self.statement.nullable else "NOT NULL"

        return f"ALTER TABLE {tab_name} ADD COLUMN {col_name} {data_type} {nullable};"
