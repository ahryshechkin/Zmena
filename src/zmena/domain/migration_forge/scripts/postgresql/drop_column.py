from zmena.domain.migration_forge.kinds.script import ScriptKind
from zmena.domain.migration_forge.scripts.script import Script


class DropColumnScript(Script):
    def __init__(self, statement):
        super().__init__(ScriptKind.DROP_COLUMN, statement)

    def assemble(self):
        tab_name = self.statement.tab_name
        col_name = self.statement.col_name

        return f"ALTER TABLE {tab_name} DROP COLUMN {col_name};"
