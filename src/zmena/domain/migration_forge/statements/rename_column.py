from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind


@dataclass(frozen=True)
class RenameColumnStatement:
    old_name: str
    new_name: str

    def __post_init__(self):
        super().__init__(StatementKind.RENAME_COLUMN)
