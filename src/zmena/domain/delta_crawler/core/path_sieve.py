from zmena.domain.delta_crawler.presets.criteria import CriterionPreset


class PathSieve:
    def __init__(self, entries):
        self.entries = entries
        self.preset = CriterionPreset()

    def __repr__(self):
        return f"PathSieve(entries={len(self.entries)})"

    def filter(self):
        selected_entries = self.entries
        for criterion in self.preset.default():
            selected_entries = criterion.apply(selected_entries)

        return selected_entries
