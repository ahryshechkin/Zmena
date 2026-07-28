from pathlib import Path


class ProjectDirectory:
    ROOT_DIR_NOT_FOUND_MESSAGE = "Project root directory not found"

    def __init__(self, start=None):
        self.start = start or Path(__file__).resolve().parent

    def root_dir(self):
        for current in [self.start, *self.start.parents]:
            if (current / "pyproject.toml").exists():
                return current

        raise FileNotFoundError(self.ROOT_DIR_NOT_FOUND_MESSAGE)

    def cmt_dir(self):
        return self.root_dir() / "catalog/cmt"

    def sce_dir(self):
        return self.root_dir() / "catalog/sce"

    def test_repo_dir(self):
        return self.root_dir() / "tests/integration/test_repo"

    def demo_repo_dir(self):
        return self.root_dir() / "tests/integration/demo_repo"
