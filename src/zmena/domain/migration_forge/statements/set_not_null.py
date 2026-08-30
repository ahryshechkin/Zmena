from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind


@dataclass(frozen=True)
class SetNotNullStatement:
    name: str

    def __post_init__(self):
        super().__init__(StatementKind.SET_NOT_NULL)
