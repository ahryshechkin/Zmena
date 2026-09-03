from zmena.infrastructure.project_directory import ProjectDirectory


class FixtureSECatalog:
    def __init__(self):
        self.directory = ProjectDirectory()

    def build_fixture_from(self, path):
        return (path / "expected.txt").read_text(encoding="utf-8").splitlines()

    def get(self, sce_id):
        for path in self.directory.fixtures_se().iterdir():
            if sce_id in path.name:
                return self.build_fixture_from(path)

        return None
