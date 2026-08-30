from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statements import StatementKind
from zmena.domain.migration_forge.statements.statement import Statement


@dataclass
class RenameColumnStatement(Statement):
    old_name: str
    new_name: str

    def __post_init__(self):
        super().__init__(StatementKind.RENAME_COLUMN)
