from pathlib import Path


class ProjectDirectory:
    def __init__(self, start=None):
        self.start = start or Path(__file__).resolve().parent

    def root_dir(self):
        msg = "Project root directory not found"

        for current in [self.start, *self.start.parents]:
            if (current / "pyproject.toml").exists():
                return current

        raise RuntimeError(msg)

    def cmt_dir(self):
        return self.root_dir() / "catalog/cmt"

    def sce_dir(self):
        return self.root_dir() / "catalog/sce"
