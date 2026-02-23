from pathlib import Path

from .scenario import Scenario


class ScenarioCatalog:
    def __init__(self):
        self.root_dir = Path(__file__).resolve().parents[1] / "scenarios"


    def scenario(self, sce_id):
        for path in self.root_dir.iterdir():
            if sce_id in path.name:
                before = (path / "before.sql").read_text(encoding="utf-8")
                after = (path / "after.sql").read_text(encoding="utf-8")
                expected = (path / "expected.txt").read_text(encoding="utf-8")

                return Scenario(
                    before=before.splitlines(),
                    after=after.splitlines(),
                    expected=expected.splitlines(),
                )

        return None


    def scenarios(self, sce_ids):
        scenarios = list()

        for path in self.root_dir.iterdir():
            if any(sce_id in path.name for sce_id in sce_ids):
                before = (path / "before.sql").read_text(encoding="utf-8")
                after = (path / "after.sql").read_text(encoding="utf-8")
                expected = (path / "expected.txt").read_text(encoding="utf-8")

                scenarios.append(Scenario(
                    before=before.splitlines(),
                    after=after.splitlines(),
                    expected=expected.splitlines(),
                ))

        return scenarios


    def all(self):
        pass