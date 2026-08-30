from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind
from zmena.domain.migration_forge.statements.statement import Statement


@dataclass
class AlterDataTypeStatement(Statement):
    name: str
    old_data_type: str
    new_data_type: str

    def __post_init__(self):
        super().__init__(StatementKind.ALTER_DATA_TYPE)
