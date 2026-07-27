import shutil
import stat
from pathlib import Path


class FSCommand:
    def __init__(self, path):
        self.path = path

    def mkdir(self):
        Path(self.path).mkdir(parents=True, exist_ok=True)

    def rmdir(self):
        def force_remove(func, p, _):
            Path.chmod(p, stat.S_IWRITE)
            func(p)

        shutil.rmtree(Path(self.path), onerror=force_remove)

    def copy(self, src):
        shutil.copytree(src, self.path, dirs_exist_ok=True)
