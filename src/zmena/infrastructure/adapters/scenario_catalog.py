from pathlib import Path

from zmena.application import Scenario


class ScenarioCatalog:
    def __init__(self):
        self.root_dir = Path(__file__).resolve().parents[4] / "scenarios"

    def __repr__(self):
        return f"ScenarioCatalog(root_dir={self.root_dir})"

    def build_scenario_from(self, path):
        sce_id, name = path.name.split("_", maxsplit=2)[1:]
        before = (path / "before.sql").read_text(encoding="utf-8")
        after = (path / "after.sql").read_text(encoding="utf-8")
        expected = (path / "expected.txt").read_text(encoding="utf-8")

        before = before if sce_id == "771" else before.splitlines()
        after = after if sce_id == "771" else after.splitlines()

        return Scenario(
            sce_id=sce_id,
            name=name,
            before=before,
            after=after,
            expected=expected.splitlines(),
        )

    def get(self, sce_id):
        for path in self.root_dir.iterdir():
            if sce_id in path.name:
                return self.build_scenario_from(path)

        return None

    def get_many(self, sce_ids):
        scenarios = []

        for path in self.root_dir.iterdir():
            if any(sce_id in path.name for sce_id in sce_ids):
                scenario = self.build_scenario_from(path)
                scenarios.append(scenario)

        return scenarios

    def get_all(self):
        scenarios = []

        for path in self.root_dir.iterdir():
            scenario = self.build_scenario_from(path)
            scenarios.append(scenario)

        return scenarios
