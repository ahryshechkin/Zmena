from zmena.domain.delta_crawler.presets.criteria import CriterionPreset


class RevisionPaths:
    def __init__(self, paths):
        self.paths = paths
        self.preset = CriterionPreset()

    def filter(self):
        selected_paths = self.paths
        for criterion in self.preset.default():
            selected_paths = criterion.apply(selected_paths)

        return selected_paths
