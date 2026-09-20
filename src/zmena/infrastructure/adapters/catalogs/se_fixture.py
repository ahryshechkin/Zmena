import json

from zmena.application.handoffs.report_hub.snapshots.fragment import FragmentSnapshot
from zmena.application.handoffs.test_suite.snapshots.link import LinkSnapshot
from zmena.infrastructure.project_directory import ProjectDirectory


class SEFixtureCatalog:
    def __init__(self):
        self.directory = ProjectDirectory()

    def build_fixture_from(self, path):
        with (path / "expected.json").open(encoding="utf-8") as file:
            items = json.load(file)

        links = []
        for item in items:
            link = LinkSnapshot(
                left=FragmentSnapshot(**item["left"]), right=FragmentSnapshot(**item["right"])
            )
            links.append(link)

        return links

    def get(self, sce_id):
        for path in self.directory.se_fixtures().iterdir():
            if sce_id in path.name:
                return self.build_fixture_from(path)

        return None
