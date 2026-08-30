from dataclasses import dataclass

from zmena.domain.migration_forge.kinds.statement import StatementKind


@dataclass(frozen=True)
class AlterDataTypeStatement:
    name: str
    old_data_type: str
    new_data_type: str

    def __post_init__(self):
        super().__init__(StatementKind.ALTER_DATA_TYPE)
