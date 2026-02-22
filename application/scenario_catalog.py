from pathlib import Path

from .scenario import Scenario

class ScenarioCatalog:
    def __init__(self):
        self.root_dir = Path(__file__).resolve().parents[1] / "scenarios"


    def get(self, sce_id):
        for path in self.root_dir.iterdir():
            if sce_id in path.name:
                before = (path / "before.sql").read_text(encoding="utf-8")
                after = (path / "after.sql").read_text(encoding="utf-8")

                return Scenario(
                    before=before.strip().splitlines(),
                    after=after.strip().splitlines(),
                )

        return None
