from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind
from zmena.domain.migration_forge.statements.statement import Statement


@dataclass
class AddColumnStatement(Statement):
    tab_name: str
    col_name: str
    data_type: str
    nullable: bool

    def __repr__(self):
        return (
            f"AddColumnStatement("
            f"tab_name={self.tab_name},col_name={self.col_name},"
            f"data_type={self.data_type},nullable={self.nullable}"
            f")"
        )

    def __post_init__(self):
        super().__init__(StatementKind.ADD_COLUMN)
