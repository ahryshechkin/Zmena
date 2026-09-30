import json

from zmena.application.edges.test_suite.records.statement import StatementRecord
from zmena.infrastructure.project_directory import ProjectDirectory


class MFFixtureCatalog:
    def __init__(self):
        self.directory = ProjectDirectory()

    def __repr__(self):
        return f"FixtureCatalog(root_dir={self.directory.mf_fixtures()})"

    def build_fixture_from(self, path):
        with (path / "expected.json").open(encoding="utf-8") as file:
            items = json.load(file)

        statements = []
        for item in items:
            statement = StatementRecord(kind=item.pop("kind"), attrs={**item})
            statements.append(statement)

        return statements

    def get(self, sce_id):
        for path in self.directory.mf_fixtures().iterdir():
            if sce_id in path.name:
                return self.build_fixture_from(path)

        return None
