from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind


@dataclass(frozen=True)
class AddColumnStatement:
    name: str
    data_type: str
    nullable: bool

    def __post_init__(self):
        super().__init__(StatementKind.ADD_COLUMN)
