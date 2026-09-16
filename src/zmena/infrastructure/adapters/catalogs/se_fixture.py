import json

from zmena.domain.semantic_engine.snapshots.fragment import FragmentSnapshot
from zmena.domain.semantic_engine.snapshots.lightweight_link import LightweightLinkSnapshot
from zmena.infrastructure.project_directory import ProjectDirectory


class SEFixtureCatalog:
    def __init__(self):
        self.directory = ProjectDirectory()

    def build_fixture_from(self, path):
        with (path / "expected.json").open(encoding="utf-8") as file:
            items = json.load(file)

        links = []
        for item in items:
            link = LightweightLinkSnapshot(
                left=FragmentSnapshot(**item["left"]), right=FragmentSnapshot(**item["right"])
            )
            links.append(link)

        return links

    def get(self, sce_id):
        for path in self.directory.se_fixtures().iterdir():
            if sce_id in path.name:
                return self.build_fixture_from(path)

        return None
