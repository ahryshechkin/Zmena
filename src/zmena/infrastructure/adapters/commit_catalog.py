from zmena.infrastructure.adapters.fs_command import FSCommand
from zmena.infrastructure.adapters.git_command import GitCommand
from zmena.infrastructure.project_directory import ProjectDirectory


class CommitCatalog:
    def __init__(self):
        self.directory = ProjectDirectory()

    def __repr__(self):
        return f"CommitCatalog(root_dir={self.directory.cmt()})"

    def build_demo_repo(self):
        fs = FSCommand(self.directory.demo_repo())
        git = GitCommand(self.directory.demo_repo())

        fs.mkdir()
        git.init()

        for path in self.directory.cmt().iterdir():
            comment = f"feat: {' '.join(path.name.split('_')[2:])}"
            fs.copy(src=path)
            git.add()
            git.commit(comment)

    def cleanup_demo_repo(self):
        fs = FSCommand(self.directory.demo_repo())
        fs.rmdir()

    def build_test_repo(self):
        fs = FSCommand(self.directory.test_repo())
        git = GitCommand(self.directory.test_repo())

        fs.mkdir()
        git.init()

        for path in self.directory.cmt().iterdir():
            comment = f"feat: {' '.join(path.name.split('_')[2:])}"
            fs.copy(src=path)
            git.add()
            git.commit(comment)

    def cleanup_test_repo(self):
        fs = FSCommand(self.directory.test_repo())
        fs.rmdir()
