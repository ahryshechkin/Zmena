from zmena.domain.migration_forge.dialects.dialect import Dialect
from zmena.domain.migration_forge.kinds.dialect import DialectKind
from zmena.domain.migration_forge.scripts.postgresql.add_column import AddColumnScript
from zmena.domain.migration_forge.scripts.postgresql.alter_data_type import AlterDataTypeScript
from zmena.domain.migration_forge.scripts.postgresql.drop_column import DropColumnScript
from zmena.domain.migration_forge.scripts.postgresql.drop_not_null import DropNotNullScript
from zmena.domain.migration_forge.scripts.postgresql.rename_column import RenameColumnScript
from zmena.domain.migration_forge.scripts.postgresql.set_not_null import SetNotNullScript
from zmena.domain.migration_forge.statements.add_column import AddColumnStatement
from zmena.domain.migration_forge.statements.alter_data_type import AlterDataTypeStatement
from zmena.domain.migration_forge.statements.drop_column import DropColumnStatement
from zmena.domain.migration_forge.statements.drop_not_null import DropNotNullStatement
from zmena.domain.migration_forge.statements.rename_column import RenameColumnStatement
from zmena.domain.migration_forge.statements.set_not_null import SetNotNullStatement


class PostgreSQLDialect(Dialect):
    def __init__(self):
        super().__init__(DialectKind.POSTGRESQL)

    def script_for(self, statement):
        scripts = {
            AddColumnStatement: AddColumnScript,
            AlterDataTypeStatement: AlterDataTypeScript,
            DropColumnStatement: DropColumnScript,
            DropNotNullStatement: DropNotNullScript,
            RenameColumnStatement: RenameColumnScript,
            SetNotNullStatement: SetNotNullScript,
        }

        script = scripts.get(type(statement))

        return script(statement)
