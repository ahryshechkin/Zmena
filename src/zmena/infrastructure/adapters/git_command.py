import subprocess


class GitCommand:
    def __init__(self, path):
        self.path = path

    def init_repo(self):
        subprocess.run([r"C:\Program Files\Git\bin\git.exe", "init"], check=True)

    def add_files(self):
        pass
