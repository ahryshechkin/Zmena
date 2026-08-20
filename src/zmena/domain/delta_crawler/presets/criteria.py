from zmena.domain.delta_crawler.criteria.excluded_extensions import ExcludedExtensionsCriterion
from zmena.domain.delta_crawler.kinds.preset_kind import PresetKind
from zmena.domain.delta_crawler.presets.preset import Preset


class CriterionPreset(Preset):
    def __init__(self):
        super().__init__(PresetKind.CRITERIA)
        # self.excluded_directories = ExcludedDirectoriesCriterion(["sql"])
        self.excluded_extensions = ExcludedExtensionsCriterion(["sql"])
        # self.included_directories = IncludedDirectoriesCriterion([".sql"])
        # self.included_extensions = IncludedExtensionsCriterion([".sql"])

    def default(self):
        return [
            # self.excluded_directories,
            self.excluded_extensions,
            # self.included_directories,
            # self.included_extensions,
        ]
