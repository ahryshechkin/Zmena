from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind
from zmena.domain.migration_forge.statements.statement import Statement


@dataclass
class AddColumnStatement(Statement):
    name: str
    data_type: str
    nullable: bool

    def __repr__(self):
        return (
            f"AddColumnStatement("
            f"name={self.name},data_type={self.data_type},nullable={self.nullable}"
            f")"
        )

    def __post_init__(self):
        super().__init__(StatementKind.ADD_COLUMN)
