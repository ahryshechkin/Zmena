from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind
from zmena.domain.migration_forge.statements.statement import Statement


@dataclass
class DropNotNullStatement(Statement):
    tab_name: str
    col_name: str

    def __repr__(self):
        return f"DropNotNullStatement(tab_name={self.tab_name},col_name={self.col_name})"

    def __post_init__(self):
        super().__init__(StatementKind.DROP_NOT_NULL)
