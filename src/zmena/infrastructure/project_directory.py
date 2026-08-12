from pathlib import Path


class ProjectDirectory:
    ROOT_DIR_NOT_FOUND_MESSAGE = "Project root directory not found"

    def __init__(self, start=None):
        self.start = start or Path(__file__).resolve().parent

    def __repr__(self):
        return f"ProjectDirectory(start={self.start})"

    def root(self):
        for current in [self.start, *self.start.parents]:
            if (current / "pyproject.toml").exists():
                return current

        raise FileNotFoundError(self.ROOT_DIR_NOT_FOUND_MESSAGE)

    def cmt(self):
        return self.root() / "catalog/cmt"

    def sce(self):
        return self.root() / "catalog/sce"

    def test_repo(self):
        return self.root() / "tests/integration/test_repo"

    def demo_repo(self):
        return self.root() / "tests/integration/demo_repo"
