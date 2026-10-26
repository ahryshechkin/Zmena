from zmena.domain.migration_forge.dialects.dialect import Dialect
from zmena.domain.migration_forge.kinds.dialect import DialectKind
from zmena.domain.migration_forge.scripts.postgresql.add_column import AddColumnScript
from zmena.domain.migration_forge.statements.add_column import AddColumnStatement


class PostgreSQLDialect(Dialect):
    def __init__(self):
        super().__init__(DialectKind.POSTGRESQL)

    def script_for(self, statement):
        scripts = {AddColumnStatement: AddColumnScript}

        script = scripts.get(type(statement))

        return script(statement)
