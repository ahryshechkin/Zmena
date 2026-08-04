import subprocess


class GitCommand:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def __repr__(self):
        return f"GitCommand(root_dir={self.root_dir})"

    def init(self):
        args = ["git", "init"]
        subprocess.run(args, cwd=self.root_dir, check=True, text=True)  # noqa: S603

    def add(self):
        args = ["git", "add", "."]
        subprocess.run(args, cwd=self.root_dir, check=True, text=True)  # noqa: S603

    def commit(self, comment):
        args = ["git", "commit", "-m", comment]
        subprocess.run(args, cwd=self.root_dir, check=True, text=True)  # noqa: S603

    def tag(self, label):
        args = ["git", "tag", "-a", f"v0.1.{label}", "-m", f"Release version 0.1.{label}"]
        subprocess.run(args, cwd=self.root_dir, check=True, text=True)  # noqa: S603

    def diff(self, commit_from, commit_to):
        args = ["git", "diff", "--name-only", commit_from, commit_to]
        result = subprocess.run(args, cwd=self.root_dir, check=True, text=True, capture_output=True)  # noqa: S603
        return result.stdout.splitlines()

    def show(self, commit, path):
        args = ["git", "show", f"{commit}:{path}"]
        result = subprocess.run(args, cwd=self.root_dir, check=True, text=True, capture_output=True)  # noqa: S603
        return result.stdout
