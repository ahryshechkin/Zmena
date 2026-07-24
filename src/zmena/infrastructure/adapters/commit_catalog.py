from pathlib import Path


class CommitCatalog:
    def __init__(self):
        self.root_dir = Path(__file__).resolve().parents[4] / "catalog/cmt"
