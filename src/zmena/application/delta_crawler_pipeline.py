from zmena.infrastructure.adapters.git_command import GitCommand
from zmena.infrastructure.project_directory import ProjectDirectory


class DeltaCrawlerPipeline:
    def __init__(self):
        self.directory = ProjectDirectory()

    def __repr__(self):
        return "DeltaCrawlerPipeline"

    def run(self):
        git = GitCommand(self.directory.test_repo())
        changed_paths = git.diff("3986206", "765d324")
        for path in changed_paths:
            desc = git.show("765d324", path)
            print(desc)
