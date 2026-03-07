from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Scenario:
    sce_id: str
    name: str
    before: list[str]
    after: list[str]
    expected: list[str]


class ScenarioCatalog:
    def __init__(self):
        self.root_dir = Path(__file__).resolve().parents[1] / "scenarios"

    def build_scenario_from(self, path):
        sce_id, name = path.name.split("_", maxsplit=2)[1:]
        before = (path / "before.sql").read_text(encoding="utf-8")
        after = (path / "after.sql").read_text(encoding="utf-8")
        expected = (path / "expected.txt").read_text(encoding="utf-8")

        return Scenario(
            sce_id=sce_id,
            name=name,
            before=before.splitlines(),
            after=after.splitlines(),
            expected=expected.splitlines(),
        )

    def get(self, sce_id):
        for path in self.root_dir.iterdir():
            if sce_id in path.name:
                return self.build_scenario_from(path)

        return None

    def get_many(self, sce_ids):
        scenarios = list()

        for path in self.root_dir.iterdir():
            if any(sce_id in path.name for sce_id in sce_ids):
                scenario = self.build_scenario_from(path)
                scenarios.append(scenario)

        return scenarios

    def get_all(self):
        scenarios = list()

        for path in self.root_dir.iterdir():
            scenario = self.build_scenario_from(path)
            scenarios.append(scenario)

        return scenarios

    def print_scenarios(self):
        for path in self.root_dir.iterdir():
            prefix, sce_id, name = path.name.upper().split("_", maxsplit=2)
            print(f"{prefix}-{sce_id} - {name}")
