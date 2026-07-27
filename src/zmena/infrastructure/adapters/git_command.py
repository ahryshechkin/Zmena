import subprocess


class GitCommand:
    def __init__(self, path):
        self.path = path

    def init(self):
        cmds = ["git", "init"]
        subprocess.run(cmds, check=True)  # noqa: S603

    def add(self):
        cmds = ["git", "add", "."]
        subprocess.run(cmds, check=True)  # noqa: S603

    def diff(self):
        pass

    def commit(self):
        cmds = ["git", "commit", "-m", "Add files"]
        subprocess.run(cmds, check=True)  # noqa: S603
