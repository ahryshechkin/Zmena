import json

from zmena.application.edges.test_suite.records.fragment import FragmentRecord
from zmena.application.edges.test_suite.records.link import LinkRecord
from zmena.infrastructure.project_directory import ProjectDirectory


class SEFixtureCatalog:
    def __init__(self):
        self.directory = ProjectDirectory()

    def __repr__(self):
        return f"FixtureCatalog(root_dir={self.directory.se_fixtures()})"

    def build_fixture_from(self, path):
        with (path / "expected.json").open(encoding="utf-8") as file:
            items = json.load(file)

        links = []
        for item in items:
            link = LinkRecord(
                left=FragmentRecord(**item["left"]), right=FragmentRecord(**item["right"])
            )
            links.append(link)

        return links

    def get(self, sce_id):
        for path in self.directory.se_fixtures().iterdir():
            if sce_id in path.name:
                return self.build_fixture_from(path)

        return None
