import subprocess


class GitCommand:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def __repr__(self):
        return f"GitCommand(root_dir={self.root_dir})"

    def init(self):
        cmds = ["git", "init"]
        subprocess.run(cmds, cwd=self.root_dir, check=True, text=True)  # noqa: S603

    def add(self):
        cmds = ["git", "add", "."]
        subprocess.run(cmds, cwd=self.root_dir, check=True, text=True)  # noqa: S603

    def diff(self):
        pass

    def commit(self, comment):
        cmds = ["git", "commit", "-m", comment]
        subprocess.run(cmds, cwd=self.root_dir, check=True, text=True)  # noqa: S603
