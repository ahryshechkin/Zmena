from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind


@dataclass(frozen=True)
class DropNotNullStatement:
    name: str

    def __post_init__(self):
        super().__init__(StatementKind.DROP_NOT_NULL)
