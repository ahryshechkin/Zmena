import json

from zmena.domain.migration_forge.statements.add_column import AddColumnStatement
from zmena.domain.migration_forge.statements.alter_data_type import AlterDataTypeStatement
from zmena.domain.migration_forge.statements.drop_column import DropColumnStatement
from zmena.domain.migration_forge.statements.drop_not_null import DropNotNullStatement
from zmena.domain.migration_forge.statements.rename_column import RenameColumnStatement
from zmena.domain.migration_forge.statements.set_not_null import SetNotNullStatement
from zmena.infrastructure.project_directory import ProjectDirectory

STATEMENT_KINDS = {
    "AddColumnStatement": AddColumnStatement,
    "AlterDataTypeStatement": AlterDataTypeStatement,
    "DropColumnStatement": DropColumnStatement,
    "DropNotNullStatement": DropNotNullStatement,
    "RenameColumnStatement": RenameColumnStatement,
    "SetNotNullStatement": SetNotNullStatement,
}


class MFFixtureCatalog:
    def __init__(self):
        self.directory = ProjectDirectory()

    def build_fixture_from(self, path):
        with (path / "expected.json").open(encoding="utf-8") as file:
            items = json.load(file)

        statements = []
        for item in items:
            statement_class = STATEMENT_KINDS[item.pop("kind")]
            statement = statement_class(**item)
            statements.append(statement)

        return statements

    def get(self, sce_id):
        for path in self.directory.mf_fixtures().iterdir():
            if sce_id in path.name:
                return self.build_fixture_from(path)

        return None
