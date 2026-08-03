class DeltaCrawlerPipeline:
    def __init__(self, commit_from, commit_to):
        self.commit_from = commit_from
        self.commit_to = commit_to

    def __repr__(self):
        return f"DeltaCrawlerPipeline(commit_from={self.commit_from},commit_to={self.commit_to})"

    def run(self, command):
        changed_paths = command.diff(self.commit_from, self.commit_to)
        for path in changed_paths:
            before = command.show(self.commit_from, path)
            after = command.show(self.commit_to, path)
            print(before)
            print(after)
