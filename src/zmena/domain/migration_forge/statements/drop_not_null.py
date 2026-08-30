from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind
from zmena.domain.migration_forge.statements.statement import Statement


@dataclass
class DropNotNullStatement(Statement):
    name: str

    def __post_init__(self):
        super().__init__(StatementKind.DROP_NOT_NULL)
