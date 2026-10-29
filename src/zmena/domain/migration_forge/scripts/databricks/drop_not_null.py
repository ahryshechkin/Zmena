from zmena.domain.migration_forge.kinds.script import ScriptKind
from zmena.domain.migration_forge.scripts.script import Script


class DropNotNullScript(Script):
    def __init__(self, statement):
        super().__init__(ScriptKind.DROP_NOT_NULL, statement)

    def assemble(self):
        tab_name = self.statement.tab_name
        col_name = self.statement.col_name

        return f"ALTER TABLE {tab_name} ALTER COLUMN {col_name} DROP NOT NULL;"
