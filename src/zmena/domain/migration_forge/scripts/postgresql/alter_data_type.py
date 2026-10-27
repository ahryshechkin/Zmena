from zmena.domain.migration_forge.kinds.script import ScriptKind
from zmena.domain.migration_forge.scripts.script import Script


class AlterDataTypeScript(Script):
    def __init__(self, statement):
        super().__init__(ScriptKind.ALTER_DATA_TYPE, statement)

    def assemble(self):
        tab_name = self.statement.tab_name
        col_name = self.statement.col_name
        data_type = self.statement.data_type

        return f"ALTER TABLE {tab_name} ALTER COLUMN {col_name} TYPE {data_type};"
