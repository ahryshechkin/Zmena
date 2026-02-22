from pathlib import Path

from .scenario import Scenario


class ScenarioCatalog:
    def __init__(self):
        self.root_dir = Path(__file__).resolve().parents[1] / "scenarios"


    def get(self, sce_ids):
        scenarios = list()

        for path in self.root_dir.iterdir():
            if any(sce_id in path.name for sce_id in sce_ids):
                before = (path / "before.sql").read_text(encoding="utf-8")
                after = (path / "after.sql").read_text(encoding="utf-8")

                scenarios.append(Scenario(
                    before=before.strip().splitlines(),
                    after=after.strip().splitlines(),
                ))

        return scenarios
