from zmena.domain.migration_forge.kinds.script import ScriptKind
from zmena.domain.migration_forge.scripts.script import Script


class RenameColumnScript(Script):
    def __init__(self, statement):
        super().__init__(ScriptKind.RENAME_COLUMN, statement)

    def assemble(self):
        tab_name = self.statement.tab_name
        old_name = self.statement.old_name
        new_name = self.statement.new_name

        return f"ALTER TABLE {tab_name} RENAME COLUMN {old_name} TO {new_name};"
