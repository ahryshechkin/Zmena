class RevisionPaths:
    def __init__(self, paths):
        self.paths = paths

    def filter(self, criteria):
        selected_paths = self.paths
        for criterion in criteria:
            selected_paths = criterion.apply(selected_paths)

        return selected_paths
