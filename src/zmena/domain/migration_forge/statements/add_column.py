from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind
from zmena.domain.migration_forge.statements.statement import Statement


@dataclass
class AddColumnStatement(Statement):
    name: str
    data_type: str
    nullable: bool

    def __post_init__(self):
        super().__init__(StatementKind.ADD_COLUMN)
