from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind
from zmena.domain.migration_forge.statements.statement import Statement


@dataclass
class AlterDataTypeStatement(Statement):
    name: str
    data_type: str

    def __repr__(self):
        return f"AlterDataTypeStatement(name={self.name},data_type={self.data_type})"

    def __post_init__(self):
        super().__init__(StatementKind.ALTER_DATA_TYPE)
