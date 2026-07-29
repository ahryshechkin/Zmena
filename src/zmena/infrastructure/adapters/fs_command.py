import shutil
import stat
from pathlib import Path


class FSCommand:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def __repr__(self):
        return f"FSCommand(root_dir={self.root_dir})"

    def mkdir(self):
        Path(self.root_dir).mkdir(parents=True, exist_ok=True)

    def rmdir(self):
        def force_remove(func, p, _):
            Path.chmod(p, stat.S_IWRITE)
            func(p)

        shutil.rmtree(Path(self.root_dir), onerror=force_remove)

    def copy(self, src):
        shutil.copytree(src, self.root_dir, dirs_exist_ok=True)
