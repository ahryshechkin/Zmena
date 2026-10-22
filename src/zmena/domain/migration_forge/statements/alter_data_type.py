from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind
from zmena.domain.migration_forge.statements.statement import Statement


@dataclass
class AlterDataTypeStatement(Statement):
    tab_name: str
    col_name: str
    data_type: str

    def __repr__(self):
        return (
            f"AlterDataTypeStatement("
            f"tab_name={self.tab_name},col_name={self.col_name},data_type={self.data_type}"
            f")"
        )

    def __post_init__(self):
        super().__init__(StatementKind.ALTER_DATA_TYPE)
