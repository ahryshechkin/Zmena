import subprocess


class GitCommand:
    def __init__(self, path):
        self.path = path

    def init(self):
        cmds = ["git", "init"]
        subprocess.run(cmds, cwd=self.path, check=True, text=True)  # noqa: S603

    def add(self):
        cmds = ["git", "add", "."]
        subprocess.run(cmds, cwd=self.path, check=True, text=True)  # noqa: S603

    def diff(self):
        pass

    def commit(self, comment):
        cmds = ["git", "commit", "-m", comment]
        subprocess.run(cmds, cwd=self.path, check=True, text=True)  # noqa: S603
