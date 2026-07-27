import shutil
import stat
from pathlib import Path


class FSCommand:
    def mkdir(self, path):
        Path(path).mkdir(parents=True, exist_ok=True)

    def rmdir(self, path):
        def force_remove(func, p, _):
            Path.chmod(p, stat.S_IWRITE)
            func(p)

        shutil.rmtree(Path(path), onerror=force_remove)

    def copy(self, src, dst):
        shutil.copytree(src, dst, dirs_exist_ok=True)
