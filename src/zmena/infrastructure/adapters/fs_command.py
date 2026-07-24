import shutil
from pathlib import Path


class FSCommand:
    def mkdir(self, path):
        Path(path).mkdir(parents=True, exist_ok=True)

    def rmdir(self, path):
        shutil.rmtree(Path(path))

    def copy(self, src, dst):
        shutil.copytree(src, dst, dirs_exist_ok=True)
