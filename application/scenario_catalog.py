from pathlib import Path


class ScenarioCatalog:
    def __init__(self):
        self.root_dir = Path(__file__).resolve().parents[1] / "scenarios"
